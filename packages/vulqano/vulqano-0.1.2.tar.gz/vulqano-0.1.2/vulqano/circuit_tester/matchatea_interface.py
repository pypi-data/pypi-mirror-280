# This code is part of vulqano.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Here we define the functions to run the quantum trajectories and the simulation
"""
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals

from copy import deepcopy
import numpy as np
from tqdm import tqdm

# try to import qmatchatea
try:
    from qmatchatea import QCBackend
except ImportError:
    QCBackend = None
try:
    from qmatchatea.py_emulator import QCEmulator
except ImportError:
    QCEmulator = None

from qtealeaves.tensors import TensorBackend
from .read_qasm import read_qasm_function

__all__ = ["qmatchatea_simulation"]


def qmatchatea_simulation(
    filename,
    operations,
    conv_params,
    num_trajectories=1000,
    backend=QCBackend(),
    tensor_backend=TensorBackend(),
    initialize="random_basis",
):
    """
    Run several simulations of a qasm file named `filename` using
    quantum matcha tea starting from random basis states for
    `num_trajectories` times.
    It computes the fidelity `|<psi|U U°|psi>|^2` with U being the noiseless
    version of U°, and |psi> a random state at a given bond dimension

    **Arguments**

    filename : str
        Name of the qasm file containing the circuit to run
    operations : DiscreteOperations
        The operations available in the circuit
    num_trajectories: int, optional
        Number of trajectories

    **Returns**

    np.ndarray[float]
        The numpy array of the fidelities
    np.ndarray[float]
        The numpy array of the infidelities from tensor network truncation
    """

    if QCBackend is None or QCEmulator is None:
        raise ImportError("Please install qmatchatea.")

    # Read only once noiseless circuit
    noiseless_operations = deepcopy(operations)
    noiseless_operations.id_infidelity = 0
    noiseless_circuit = read_qasm_function(filename, noiseless_operations)
    xx_gate = tensor_backend.tensor_cls.from_elem_array(
        np.array([[0.0, 1.0], [1.0, 0.0 + 0j]])
    )

    num_sites = noiseless_circuit.num_sites
    fidelities = np.zeros(num_trajectories)
    tn_infid = np.zeros(num_trajectories)

    for qt_idx in tqdm(range(num_trajectories)):
        # Read the noisy circuit, generating the error
        noisy_circ = read_qasm_function(filename, operations)

        # Initialize the emulators randomly (but with same state)
        if initialize == "random_basis":
            noiseless_emulator = QCEmulator(
                num_sites,
                convergence_parameters=conv_params,
                local_dim=2,
                tensor_backend=tensor_backend,
                qc_backend=backend,
                initialize="random",
            )
            noiseless_emulator.emulator.apply_one_site_operator(
                xx_gate, np.random.randint(0, num_sites)
            )
        else:
            noiseless_emulator = QCEmulator(
                num_sites,
                convergence_parameters=conv_params,
                local_dim=2,
                tensor_backend=tensor_backend,
                qc_backend=backend,
                initialize="random",
            )
        noisy_emulator = QCEmulator.from_tensor_list(
            deepcopy(noiseless_emulator.emulator.to_tensor_list()),
            conv_params=conv_params,
            tensor_backend=tensor_backend,
            qc_backend=backend,
        )
        # Run the emulations
        noisless_svd_cuts, _, _ = noiseless_emulator.run_from_qcirc(noiseless_circuit)
        noisy_svd_cuts, _, _ = noisy_emulator.run_from_qcirc(noisy_circ)

        noiseless_fid = 1 - np.prod(1 - np.array(noisless_svd_cuts))
        if noiseless_fid > 1e-5:
            raise RuntimeError(
                f"Tensor networks truncation of {noiseless_fid} on noiseless circuit"
            )
        noisy_fid = 1 - np.prod(1 - np.array(noisy_svd_cuts))
        if noisy_fid > 1e-5:
            print(f"Tensor networks truncation of {noisy_fid} on noisy circuit")

        noisy_emulator.emulator.normalize()
        # Compute the overlap
        ovlp = noiseless_emulator.emulator.dot(noisy_emulator.emulator)
        if ovlp > 1:
            ovlp = 2 - ovlp
        fidelities[qt_idx] = np.abs(ovlp) ** 2
        tn_infid[qt_idx] = noisy_fid

    return fidelities, tn_infid
