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
Here we define the function that performs optimization based on markovian
dynamics of a circuit state (e.g. simulated annealing).
"""

from math import pi as PI
import sys
import time as timer
import numpy as np
from tqdm import tqdm
from vulqano.version import __version__
from vulqano.states.abstractcircuitstate import AbstractCircuitState
from vulqano.utils import check_circuit_equivalence
from vulqano.mcmc import MarkovChainMonteCarlo


__all__ = [
    "simulated_annealing",
]


def simulated_annealing(
    input_circuit,
    machine,
    sa_instructions,
    verbose=False,
    inspection_mode=False,
    max_result_size=10000,
):
    """
    Performs a simulated annealing of the input circuit.

    **Arguments**

    input_circuit : AbstractCircuitState
        The circuit state at the begining of the annealing process.
    machine : dictionary
        qubits : touple
            Number of qubits of the machine for each spatial axis
        hamiltonian : list of (np.array of strings, float, mask)
            Abstract description of the Hamiltonian. The energy is obtained by
            counting how many times each subcircuit hamiltonian_operator[i][0]
            appears on a region A of the circuit suck that that
            hamiltonian_operator[i][2] is True for all (t,q) in A.
            The counted number is multiplied by the weight hamiltonian_operator[i][1].
        gates : set
            Gates enabled on the machine (virtual gates included).
    sa_instructions : dictionary
        steps : int
            Number of time steps.
        t_schedule : function
            A function returning the system temperature at each step.
        rules_classes : str or list of ints, optional
            A list of the ints identifying the rule classes that we want to generate.
            Default is "all" and generates all the rule classes.
        generators : "std" or list of generators, optional
            The list of generators producing the rules to be used. Default is "std",
            in this case a standard list of rules is used.
        pulses : function, optional
            A function returning the weight of each class of transitions at each
            steps. If this key is not specified, we use equal probability.
    inspection_mode : bool, optional
        If true, after each transition the fidelity of the circuit state with
        the initial state is measured. If the fidelity is different than zero,
        an error is raised and the last transition is shown. The inspection mode
        can be applied only to states with a maximum number of 8 qubits.
    verbose : bool, optional
        If false, no message is shown. Default is False.
    max_results_size : int, optional
        Max size of the energy evolution in output. If max_results_size is smaller
        than the number of steps in the time_schedule, the energy_evolution is
        coars grained by averaging on steps windows. Default is 10000.

    **Returns**

    output_dictionary : dictionary
        sa_parameters : dictionary
            software_version : str
                Version of the software used for the simulation.
            initial_state : CircuitState
                See Parameters
            machine : dictionary
                See Parameters
            sa_instructions : dictionary
                See Parameters
        sa_results : dictionary
            computational_time : float
                total computational time of the simulated annealing.
            initial_energy : float
                Initial energy
            final_energy : float
                Final energy
            final_state : CircuitState
                The circuit state at the end of the annealing process.
            energy_statistics : numpy.array
                A matrix that associate to each temperature the average energy around
                that temperature.
            rules_statistics : dictionary
                A dictionary that associates to each rules class the number of
                times that the contained rules have been used in the mcmc.
    """

    if "rules_classes" not in sa_instructions:
        sa_instructions["rules_classes"] = "all"

    if "generators" not in sa_instructions:
        sa_instructions["generators"] = "std"

    tic = timer.time()

    # Initialize the mcmc
    current_energy = input_circuit.get_energy(machine["hamiltonian"])
    initial_energy = current_energy

    if inspection_mode:
        if np.product(input_circuit.qubits) > 8:
            raise ValueError(
                "Inspectio mode is allowed only for circuits with no more"
                + "than 8 qubits."
            )

    if verbose:
        print(
            "\nVulqano compiler version "
            + str(__version__)
            + "\n\n SIMULATED ANNEALING\n Initial energy:",
            current_energy,
            "\nEvaluating...\n",
        )
        pbar = tqdm(range(sa_instructions["steps"]), file=sys.stdout)
    else:
        pbar = range(sa_instructions["steps"])

    mcmc = MarkovChainMonteCarlo(
        input_circuit,
        machine["gates"],
        machine["hamiltonian"],
        rules_classes=sa_instructions["rules_classes"],
        generators=sa_instructions["generators"],
    )

    transitions_classes = list({rule.class_index for rule in mcmc.rules})
    if "pulses" in sa_instructions:
        pulser = sa_instructions["pulses"]
    else:

        def pulser(step):
            return np.ones(len(transitions_classes))

    # Execute the mcmc
    if max_result_size < sa_instructions["steps"]:
        steps_window_size = sa_instructions["steps"] / max_result_size
    else:
        steps_window_size = 1

    temperature_window = []
    current_energy_window = []
    window_counter = 0
    t_scheduler = sa_instructions["t_schedule"]

    energy_statistics = []
    for step in pbar:
        mcmc.temperature = t_scheduler(step)

        pulse = pulser(step)
        transitions_classes_probs = {}
        for index, transition_class in enumerate(transitions_classes):
            transitions_classes_probs[transition_class] = pulse[index]
        mcmc.transitions_classes_probs = transitions_classes_probs

        if verbose:
            pbar.set_postfix(
                {
                    "T": mcmc.temperature,
                    "E": current_energy,
                    "Map size": mcmc.map.size,
                }
            )

        if inspection_mode:
            energy_diff, last_transition = mcmc.apply_boltzmann_transition()
            if last_transition is not None:
                current_state = mcmc.state.to_abstract("current_state")
                check_result = check_circuit_equivalence(current_state, input_circuit)
                if not check_result:
                    raise ValueError(
                        "MC failed at transition:\n"
                        + str(last_transition[1][0])
                        + "\nAt region:\n"
                        + str(last_transition[0])
                        + "\nOf the state:\n"
                        + str(current_state)
                    )

        else:
            energy_diff, _ = mcmc.apply_boltzmann_transition()

        current_energy = current_energy + energy_diff
        temperature_window.append(mcmc.temperature)
        current_energy_window.append(current_energy)

        if (step + 1) // steps_window_size > window_counter:
            energy_statistics.append(
                [np.mean(mcmc.temperature), np.mean(current_energy)]
            )
            window_counter += 1
            temperature_window = []
            current_energy_window = []

    # Outputs
    if verbose:
        print("Done. Final energy = ", current_energy)

    toc = timer.time()

    rules_statistics = {}
    for rule in mcmc.rules:
        if rule.class_index in rules_statistics:
            rules_statistics[rule.class_index] += rule.counters[0] + rule.counters[1]
        else:
            rules_statistics[rule.class_index] = rule.counters[0] + rule.counters[1]

    sa_parameters = {
        "software_version": "vulqano version " + str(__version__),
        "input_circuit": input_circuit,
        "machine": machine,
        "sa_instructions": sa_instructions,
    }

    sa_results = {
        "computational_time": toc - tic,
        "initial_energy": initial_energy,
        "final_energy": current_energy,
        "output_circuit": mcmc.state.to_abstract("SA output"),
        "energy_statistics": np.array(energy_statistics),
        "rules_statistics": rules_statistics,
    }

    output_dictionary = {"sa_parameters": sa_parameters, "sa_results": sa_results}

    return output_dictionary


def base_unit_test(input_circuit, machine):
    """
    Define simple general scheme for unit tests of the simulated annealing.


    **Arguments**

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

    **Returns**

    bool
        True if the output circuit is equivalent to the input circuit and the
        difference between the initial and final energy is the sum of the energy
        differences of the MCMC steps.
    """

    steps = 2000
    max_t = 1  # ~max_gap * 100
    min_t = 0.001  # ~min_gap/10

    def t_schedule(ii):
        return max_t * ((min_t / max_t) ** (ii / steps))

    sa_instructions = {
        "steps": steps,
        "t_schedule": t_schedule,
    }

    output_dictionary = simulated_annealing(
        input_circuit,
        machine,
        sa_instructions,
        verbose=False,
        inspection_mode=False,
    )

    sa_parameters = output_dictionary["sa_parameters"]
    sa_results = output_dictionary["sa_results"]
    print(
        """\nCheck if the final circuit is equivalent to the initial one
          and the final energy is well calculated in the Markov chain."""
    )
    check_result = check_circuit_equivalence(
        sa_parameters["input_circuit"], sa_results["output_circuit"]
    )
    energy_diff = np.abs(
        sa_results["final_energy"]
        - sa_results["output_circuit"].get_energy(machine["hamiltonian"])
    )

    return check_result and (energy_diff < 10 ** (-10))


def unit_test_discrete():
    """
    Perform a simulated annealing with a small non parametric circuit to verify
    that final circuit is equivalent to the initial one and the final energy is
    well calculated in the Markov chain.

    **Returns**

    bool
        True if the final circuit is equivalent to the inital one and the final
        energy is well calculated.
    """

    input_circuit = AbstractCircuitState(
        np.array(
            [
                ["lock", "Z", "CZ", "busy"],
                ["SWAP", "busy", "Z", "idle"],
                ["Z", "idle", "CZ", "busy"],
                ["idle", "idle", "idle", "idle"],
            ]
        ),
        "input_circuit",
    )
    swap_left = 1
    swap_right = 1
    input_circuit.add_swap_area(swap_left, swap_right)
    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, input_circuit.qubits), False),
            np.full(
                np.append(
                    input_circuit.times - swap_right - swap_left, input_circuit.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, input_circuit.qubits), False),
        )
    )
    machine = {
        "gates": {"Z", "H", "CZ", "SWAP"},
        "hamiltonian": (
            (np.array([["Z"]]), 0.001, circuit_area_mask),
            (np.array([["H"]]), 0.001, circuit_area_mask),
            (np.array([["idle"]]), 0.001, circuit_area_mask),
            (np.array([["CZ"]]), 0.005, circuit_area_mask),
            (np.array([["SWAP"]]), 1, circuit_area_mask),
            (np.array([["CZ", "any", "CZ"]]), 0.5, circuit_area_mask),
            (
                np.array([["CZ", "any", "any", "CZ"]]),
                0.05,
                circuit_area_mask,
            ),
            (
                np.full(np.append(1, input_circuit.qubits), "idle"),
                -np.prod(input_circuit.qubits) * 0.001,
                circuit_area_mask,
            ),
        ),
    }

    return base_unit_test(input_circuit, machine)


def unit_test_continuous():
    """
    Perform a simulated annealing with a small parametric circuit to verify that
    the final circuit is equivalent to the initial one and the final energy is
    well calculated in the Markov chain.

    **Returns**

    bool
        True if the final circuit is equivalent to the inital one and the final
        energy is well calculated.
    """

    input_circuit = AbstractCircuitState(
        np.array(
            [
                ["RZ", "RZ", "CP", "busy"],
                ["SWAP", "busy", "RZ", "idle"],
                ["RX", "idle", "CP", "busy"],
                ["idle", "RX", "idle", "idle"],
            ]
        ),
        "input_circuit",
        rot_amplitudes_array=np.array(
            [
                [2, 5, PI, 0],
                [0, 0, 1, 0],
                [PI, 0, 6, 0],
                [0, 4, 0, 0],
            ]
        ),
    )

    swap_left = 1
    swap_right = 1
    input_circuit.add_swap_area(swap_left, swap_right)
    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, input_circuit.qubits), False),
            np.full(
                np.append(
                    input_circuit.times - swap_right - swap_left, input_circuit.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, input_circuit.qubits), False),
        )
    )
    machine = {
        "gates": {"RX", "RZ", "CP", "SWAP"},
        "hamiltonian": (
            (np.array([["RX"]]), 0.001, circuit_area_mask),
            (np.array([["RZ"]]), 0.001, circuit_area_mask),
            (np.array([["idle"]]), 0.001, circuit_area_mask),
            (np.array([["CP"]]), 0.005, circuit_area_mask),
            (np.array([["CP"]]), 0.005, circuit_area_mask),
            (np.array([["SWAP"]]), 1, circuit_area_mask),
            (np.array([["CP", "any", "CP"]]), 0.5, circuit_area_mask),
            (np.array([["CP", "any", "any", "CP"]]), 0.05, circuit_area_mask),
            (
                np.full(np.append(1, input_circuit.qubits), "idle"),
                -np.prod(input_circuit.qubits) * 0.001,
                circuit_area_mask,
            ),
        ),
    }

    return base_unit_test(input_circuit, machine)


def unit_test_discrete_3d():
    """
    Perform a simulated annealing with a small parametric circuit on a
    2d qubit lattice to verify that final circuit is equivalent to the initial
    one and the final energy is well calculated in the Markov chain.

    **Returns**

    bool
        True if the final circuit is equivalent to the inital one and the final
        energy is well calculated.
    """

    input_circuit = AbstractCircuitState(
        np.array(
            [
                [["CZ_r", "Z"], ["busy", "Z"], ["idle", "idle"], ["SWAP", "busy"]],
                [["SWAP", "busy"], ["Z", "idle"], ["idle", "idle"], ["SWAP", "busy"]],
                [["Z", "idle"], ["CZ", "busy"], ["idle", "idle"], ["SWAP", "busy"]],
                [
                    ["idle", "SWAP_r"],
                    ["idle", "busy"],
                    ["idle", "idle"],
                    ["SWAP", "busy"],
                ],
            ]
        ),
        "input_circuit",
    )
    swap_left = 1
    swap_right = 1
    input_circuit.add_swap_area(swap_left, swap_right)
    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, input_circuit.qubits), False),
            np.full(
                np.append(
                    input_circuit.times - swap_right - swap_left, input_circuit.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, input_circuit.qubits), False),
        )
    )
    machine = {
        "gates": {"Z", "H", "CZ", "SWAP", "CZ_r", "SWAP_r"},
        "hamiltonian": (
            (np.array([[["Z"]]]), 0.001, circuit_area_mask),
            (np.array([[["H"]]]), 0.001, circuit_area_mask),
            (np.array([[["idle"]]]), 0.001, circuit_area_mask),
            (np.array([[["CZ"]]]), 0.005, circuit_area_mask),
            (np.array([[["SWAP"]]]), 1, circuit_area_mask),
            (np.array([[["CZ_r"]]]), 0.005, circuit_area_mask),
            (np.array([[["SWAP_r"]]]), 1, circuit_area_mask),
            (
                np.full(np.append(1, input_circuit.qubits), "idle"),
                -np.prod(input_circuit.qubits) * 0.001,
                circuit_area_mask,
            ),
        ),
    }

    return base_unit_test(input_circuit, machine)


def unit_test_continuous_3d():
    """
    Perform a simulated annealing with a small non parametric circuit on a
    2d qubit lattice to verify that final circuit is equivalent to the initial
    one and the final energy is well calculated in the Markov chain.

    **Returns**

    bool
        True if the final circuit is equivalent to the inital one and the final
        energy is well calculated.
    """

    input_circuit = AbstractCircuitState(
        np.array(
            [
                [["CP_r", "RZ"], ["busy", "RZ"], ["idle", "idle"], ["SWAP", "busy"]],
                [["SWAP", "busy"], ["RZ", "idle"], ["idle", "idle"], ["SWAP", "busy"]],
                [["RZ", "idle"], ["CP", "busy"], ["idle", "idle"], ["SWAP", "busy"]],
                [
                    ["idle", "SWAP_r"],
                    ["idle", "busy"],
                    ["idle", "idle"],
                    ["SWAP", "busy"],
                ],
            ]
        ),
        "input_circuit",
        rot_amplitudes_array=np.array(
            [
                [[PI, PI / 2], [0, PI], [0, 0], [0, 0]],
                [[0, 0], [PI, 0], [0, 0], [0, 0]],
                [[PI, 0], [PI, 0], [0, 0], [0, 0]],
                [[0, 0], [0, 0], [0, 0], [0, 0]],
            ]
        ),
    )
    swap_left = 1
    swap_right = 1
    input_circuit.add_swap_area(swap_left, swap_right)
    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, input_circuit.qubits), False),
            np.full(
                np.append(
                    input_circuit.times - swap_right - swap_left, input_circuit.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, input_circuit.qubits), False),
        )
    )

    machine = {
        "gates": {"RZ", "RX", "CP", "SWAP", "CP_r", "SWAP_r"},
        "hamiltonian": (
            (np.array([[["RZ"]]]), 0.001, circuit_area_mask),
            (np.array([[["RX"]]]), 0.001, circuit_area_mask),
            (np.array([[["idle"]]]), 0.001, circuit_area_mask),
            (np.array([[["CP"]]]), 0.005, circuit_area_mask),
            (np.array([[["SWAP"]]]), 1, circuit_area_mask),
            (np.array([[["CP_r"]]]), 0.005, circuit_area_mask),
            (np.array([[["SWAP_r"]]]), 1, circuit_area_mask),
            (
                np.full(np.append(1, input_circuit.qubits), "idle"),
                -np.prod(input_circuit.qubits) * 0.001,
                circuit_area_mask,
            ),
        ),
    }

    return base_unit_test(input_circuit, machine)


if __name__ == "__main__":
    print("\nUnit test with non parametric circuit->\n")
    print(unit_test_discrete())
    print("\nUnit test with parametric circuit ->\n")
    print(unit_test_continuous())
    print("\nUnit test with non parametric 3d circuit->\n")
    print(unit_test_discrete_3d())
    print("\nUnit test with parametric 3d circuit->\n")
    print(unit_test_continuous_3d())
