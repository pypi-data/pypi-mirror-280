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
Main module for compiling quantum circuits using various optimization techniques
based on many-body embedding.
"""
try:
    from multiprocess import Pool

    MP_AVAILABLE = True
except ImportError:
    MP_AVAILABLE = False

from vulqano.utils import save_to_json
from vulqano.markoviandynamics import simulated_annealing
from vulqano.quantumdynamics import quantum_circuit_dynamics

__all__ = [
    "compiler",
]


def compiler(method, input_circuit, machine, instructions, n_cpus, output_folder):
    """
    Main function for the many-body compilation of quantum circuit.

    **Arguments**

    method : str
        Many-body optimization method used by the compiler.
    input_circuit : vulqano.states.AbstractCircuitState
        The circuit state (many-body classical state) representing te circuit
        to optimize.
    machine : dictionary
        hamiltonian_operator : list of (np.array of strings, float, mask)
            Abstract description of the Hamiltonian. The energy is obtained by
            counting how many times each subcircuit hamiltonian_operator[i][0]
            appears on a region A of the circuit suck that that
            hamiltonian_operator[i][2] is True for all (t,q) in A.
            The counted number is multiplied by the weight hamiltonian_operator[i][1].
        gates : set
            Gates enabled on the machine (virtual gates included).
    instructions : dict or list of dict
        Set of instructions specific for the optimization method.
    n_cpus : int
        Number of CPUs involved in the parallelization.
    output_folder : str
        Name of the folder where the raw data results are saved.

    **Returns**

    results
        Specific output of the selected optimization method.
    """

    if method == "simulated_annealing":
        if n_cpus > 1 and MP_AVAILABLE:
            with Pool(n_cpus) as pool:
                results = pool.starmap(
                    simulated_annealing,
                    [
                        (input_circuit, machine, instructions)
                        for _ in range((instructions["iterations"]))
                    ],
                )
        elif n_cpus == 1:
            results = [
                simulated_annealing(input_circuit, machine, instructions)
                for _ in range(instructions["iterations"])
            ]
        else:
            raise ImportError(
                "Install python module multiprocess (not multiprocessing) to allow parallelization."
            )

        for counter, result in enumerate(results):
            save_to_json(result, output_folder, "sampling_number_" + str(counter))

        return results

    if method == "quantum_annealing":
        if n_cpus != 1:
            print(
                "Quantum simulation is parallelized at Fortran level. ",
                "Parallelization is active if you have compiled QuantumTea with MPI enabled.",
            )

        result = quantum_circuit_dynamics(
            input_circuit, machine, instructions[0], instructions[1]
        )

        save_to_json(
            result,
            output_folder,
            "experiment_description",
        )
        return result

    raise ValueError(
        "The method "
        + method
        + " is not supported. Supported methods are: "
        + "{simulated_annealing, quantum_annealing}."
    )
