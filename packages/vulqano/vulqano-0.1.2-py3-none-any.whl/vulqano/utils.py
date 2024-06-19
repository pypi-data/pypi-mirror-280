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
Here we define some support functions.
"""

import os
import hashlib
import json
import numpy as np
from qiskit import Aer
from qiskit import execute
from qiskit import QuantumCircuit
from vulqano.states import AbstractCircuitState

__all__ = [
    "check_circuit_equivalence",
    "var_to_md5",
    "save_to_json",
]


def check_circuit_equivalence(circuit_1, circuit_2):
    """
    Checks if two circuits are equivalent: ||U1 U2^(-1) - 1||_F < 10^(1-precision).
    Based on Qiskit.

    **Arguments**

    circuit_1 : AbstractCircuitState
        Matrix of the Input circuit 1.
    circuit_2 : AbstractCircuitState
        Input circuit 2.

    **Returns**

    is_equivalent : bool
        True if the two circuit are equivalent.
    """
    if (circuit_1.times != circuit_2.times) or (
        np.prod(circuit_1.qubits) != np.prod(circuit_2.qubits)
    ):
        raise ValueError(
            "Input circuits must have the same number of qubits and time steps."
        )
    if circuit_1.vector.shape[1] > 8:
        raise ValueError("Max number of qubits for this test is 8. It's expensive!")
    circuit_1 = QuantumCircuit.from_qasm_str(circuit_1.to_qasm())
    circuit_2 = QuantumCircuit.from_qasm_str(circuit_2.to_qasm())
    circuit = circuit_1.compose(circuit_2.inverse())
    l_e = (
        execute(circuit, Aer.get_backend("unitary_simulator"))
        .result()
        .get_unitary(circuit, decimals=14)
        .data
    )
    l_e_norm = np.linalg.norm(l_e * np.conjugate(l_e[0][0]) - np.identity(len(l_e)))
    is_equivalent = l_e_norm < 10 ** (-5)
    if not is_equivalent:
        print("L.E. = ", l_e_norm)
    return is_equivalent


def var_to_md5(var, digits=5):
    """
    Generates the first digits of the md5 of str(var), as a string. Useful
    for generating unique filenames.

    **Arguments**

    var : object
        Any object having a __str__ method.
    digits : int, optional
        Number of digits to be returned.

    **Returns**

        : string
        First "digits" digits of the md5 of str(var), as a string.

    """
    return str(hashlib.md5(str(var).encode()).hexdigest()[0:digits])


class VulqanoJsonEncoder(json.JSONEncoder):
    """
    A json encoder extended for vulqano with ability to
    handle common problematic classes.
    """

    # pylint: disable-next=arguments-renamed
    def default(self, obj):
        """
        Default encoding is checking for common classes with no default
        support for encoding.

        Arguments
        ---------

        obj
            Object to be encoded.
        """

        if isinstance(obj, (np.floating, np.integer)):
            return obj.item()

        if isinstance(obj, np.ndarray):
            return obj.tolist()

        if isinstance(obj, AbstractCircuitState):
            if obj.is_continuous:
                return (
                    obj.vector.tolist(),
                    obj.name,
                    obj.rot_amplitudes.tolist(),
                )
            return (
                obj.vector.tolist(),
                obj.name,
                None,
            )

        if isinstance(obj, set):
            return list(obj)

        if callable(obj):
            return "Non JSON serializable: callable"

        return super().default(obj)


def save_to_json(dictionary, path, file_name):
    """
    Saves the object var object to a Json file.

    **Arguments**

    var : object
        Object to be saved.
    path : str
        Destination path.
    name : str
        File name.

    **Returns**

    None.
    """

    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, file_name), "w+") as file:
        json.dump(dictionary, file, cls=VulqanoJsonEncoder)
