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
Here we define the function that performs optimization based on quantum dynamics
of a state that encodes a superposition of circuits (e.g. quantum annealing).

The dynamics is simulated using qtealeaves.
"""


import os
import shutil
import math
from time import perf_counter as tictoc
import numpy as np
import qtealeaves as qtl
from qtealeaves.tooling.hilbert_curvature import HilbertCurveMap
from vulqano.version import __version__
from vulqano.utils import check_circuit_equivalence
from vulqano.states.abstractcircuitstate import AbstractCircuitState
from vulqano.rules.sym4rules import SYM_4_RULES_GENERATORS
from vulqano.quantummodels.quantummodel import get_quantum_compilation_model
from vulqano.quantummodels.collapsedquantummodel import (
    CollapseMap,
    get_collapsed_quantum_compilation_model,
)


__all__ = [
    "CircuitsFromTN",
    "quantum_circuit_dynamics",
]


class CircuitsFromTN:
    """
    Class to read a distribution of quantum circuit from a TN state of
    qtealeaves.


    **Arguments**

    filename : str
        Name of the source file where the TTN is stored.
    gates : list of strings sorted alphabetically
        If the circuit is not collapsed, list of gates involved in the circuit,
        with idle and busy excluded. If the circuit is collapsed, list of
        supergates representing the possible local states.
    shape : tuple of ints
        Shape of the lattice where the circuit is encoded, including fictitious
        sites added to fit in a TTN.
    real_shape : tuple of ints
        Shape of the circuit encoded in the lattice, excluding fictitious
        sites added to fit in a TTN.
    collapse_map : None or quantummodels.collapsedquantummodel.CollapseMap
        None if the circuit is not collapsed, else CollapseMap object encoding
        the supergate to time-step translation.
    max_data_site : int, optional
        Maximum number of distribution elements to be stored. Default is 1000.
    min_prob : int, optional
        Minimal probability for a sampled circuit to be stored. Default is 0.0001.

    **Attributes**

    circuits_and_probabilities : list of (AbstractCircuitState, float)
        Sampled circuits with the associated probabilities.
    sampled_probability : float
        Total probability sampled. If the stored sampling is complete, this value
        is 1.
    """

    def __init__(
        self,
        filename,
        gates,
        shape,
        real_shape,
        collapse_map,
        num_samples=1000,
        max_data_size=1000,
        min_prob=10 ** (-4),
    ):
        if "ttn" in filename:
            psi = qtl.emulator.TTN.read(filename, qtl.tensors.TensorBackend())
        elif "mps" in filename:
            psi = qtl.emulator.MPS.read(filename, qtl.tensors.TensorBackend())
        else:
            raise IOError(f"File {filename} is not a readable tensor network file")
        probs = psi.meas_unbiased_probabilities(
            num_samples, do_return_samples=False, precision=15
        )

        circuits_and_probabilities = []

        if collapse_map is not None:
            supergatesgates = collapse_map.collapsed_gates
            for measured_state, upper_lower in probs.items():
                lower, upper = upper_lower
                probability = float(upper - lower)
                if "," in measured_state:
                    measured_state = measured_state.split(",")
                supergates_list = [supergatesgates[int(ii)] for ii in measured_state]
                state = np.array(collapse_map.decollapse_state(supergates_list))
                state = AbstractCircuitState(
                    state[: real_shape[0], : real_shape[1]],
                    "Circuit from ttn -  probability = " + str(probability),
                )
                circuits_and_probabilities.append((state, probability))

        else:
            gates = ["idle"] + gates + ["busy"]
            backmapping_vector_observable = HilbertCurveMap(
                2, shape
            ).backmapping_vector_observable
            for measured_state, upper_lower in probs.items():
                lower, upper = upper_lower
                probability = float(upper - lower)
                if probability > min_prob:
                    gates_list = [gates[int(ii)] for ii in measured_state]
                    state = backmapping_vector_observable(np.array(gates_list))
                    state = AbstractCircuitState(
                        state[: real_shape[0], : real_shape[1]],
                        "Circuit from ttn -  probability = " + str(probability),
                    )
                    circuits_and_probabilities.append((state, probability))

        circuits_and_probabilities.sort(key=lambda x: -x[1])

        self.circuits_and_probabilities = circuits_and_probabilities[:max_data_size]
        self.sampled_probability = sum(
            circuit_and_probability[1]
            for circuit_and_probability in circuits_and_probabilities
        )

    def get_classical_energy_statistics(self, hamiltonian):
        """
        Returns the statistics associated to a classical observable (energy),
        in terms of values vs probabilities.

        **Parameters**

        hamiltonian : list of (np.array of strings, float, mask)
            Abstract description of the Hamiltonian. The energy is obtained by
            counting how many times each subcircuit hamiltonian_operator[i][0]
            is applied on a site of the circuit state such that
            hamiltonian_operator[i][2](t,q) is True. The counted number is multiplied
            by the weight hamiltonian_operator[i][1].

        **Returns**

        energy_vs_probability : dictionary
            A dictionary that associates to each energy a probability of being
            measured.
        """
        energy_vs_probability = {}

        for circuit, probability in self.circuits_and_probabilities:
            energy = float(circuit.get_energy(hamiltonian))
            if energy in energy_vs_probability:
                energy_vs_probability[energy] += probability
            else:
                energy_vs_probability[energy] = probability

        return energy_vs_probability

    def get_equivalence_ratio_and_best_state(
        self, input_circuit, hamiltonian, max_iter=100
    ):
        """
        Generates the probability of sampling a circuit that is equivalent to
        the input circuit, and the sapled equivalent circuit qith minimum energy.

        **Parameters**

        input_circuit : AbstractCircuitState
            Input circuit that must be equivalent to the sampled circuits.
        hamiltonian : list of (np.array of strings, float, mask)
            Abstract description of the Hamiltonian. The energy is obtained by
            counting how many times each subcircuit hamiltonian_operator[i][0]
            is applied on a site of the circuit state such that
            hamiltonian_operator[i][2](t,q) is True. The counted number is multiplied
            by the weight hamiltonian_operator[i][1].
        max_iter : int, optional
            Max number of circuit for which the equivalence has to be checked.
            The default is 100.

        **Returns**

        equivalent_probability : float
            Sampled probability of getting an equivalent circuit.
        not_equivalent_probability : float
            Sampled probability of getting a non equivalent circuit.
        best_state : AbstractCircuitState
            Equivalent sampled circuit that minimizes the energy. The associated
            probability and energy are encoded in best_state.name .

        """
        equivalent_probability = 0
        not_equivalent_probability = 0
        iter_num = 0
        best = {
            "circuit": None,
            "energy": 10 ** (12),
            "probability": 0,
        }
        for circuit, probability in self.circuits_and_probabilities:
            if iter_num < max_iter:
                if check_circuit_equivalence(circuit, input_circuit):
                    equivalent_probability += probability
                    energy = circuit.get_energy(hamiltonian)
                    if energy < best["energy"]:
                        best = {
                            "circuit": circuit,
                            "energy": energy,
                            "probability": probability,
                        }
                else:
                    not_equivalent_probability += probability
            iter_num += 1
        best_state = best["circuit"]
        best_state.name = (
            "QA lowest energy equivalent state - E = "
            + str(np.round(best["energy"], 5))
            + " - P = "
            + str(np.round(best["probability"], 5))
        )
        return equivalent_probability, not_equivalent_probability, best_state


def quantum_circuit_dynamics(
    input_circuit,
    machine,
    qcd_instructions,
    simulation_instructions,
    max_results_size=100,
    del_data=False,
):
    """
    Evolve a state representing a quantum circuit qith a quantum dynamics.
    The dynamics is simualted with QuantumTEA.

    **Arguments**

    input_circuit : AbstractCircuitState
        Classical circuit state, the initial state of the dynamics.
    machine : dictionary
        hamiltonian_operator : list of (np.array of strings, float, mask)
            Abstract description of the Hamiltonian. The energy is obtained by
            counting how many times each subcircuit hamiltonian_operator[i][0]
            appears on a region A of the circuit suck that that
            hamiltonian_operator[i][2] is True for all (t,q) in A.
            The counted number is multiplied by the weight hamiltonian_operator[i][1].
        gates : set
            Gates enabled on the machine (virtual gates included).
    qcd_instructions : dictionary
        annealing_T : float
            Annealing time.
        rules_classes : str or list of ints, optional
            A list of the ints identifying the rule classes that we want to generate.
            Default is "all" and generates all the rule classes.
        generators : "std" or list of generators, optional
            The list of generators producing the rules to be used. Default is "std",
            in this case a standard list of rules is used.
        annealing_schedule : char, optional
            Pulse schedule for the annealing process. Default is A.
        max_rules_volume : int, optional
            Maximum volume allowed for the rules to be included in the driving
            Hamiltonian. Default is 100.
    simulation_instructions : dictionary
        simulation_name : str
            Name identifiung the folder of simulation input and output.
        delta_t : float
            Time step duration for the simualtion.
        max_bond_dimension : int
            Max bond dimension for TN simulation.
        svd_mode : char, optional
            Singular value decomposition mode. Default is "V".
            See Quantum Tea Leaves for more informations.
        time_evolution_mode : int, optional
            Time evolution mode. Default is 5.
            See Quantum Tea Leaves for more informations.
        mpo_mode : int, optional
            Matrix product operators mode. Default is 4.
            See Quantum Tea Leaves for more informations.
        gs_search_iter : int, optional
            Number of iterations for the initial GS search. Default is 3.
        collapsed : bool, optional
            If true, each possible configuration of qubit lattice is represented
            by the state of a single qudit. Default is False.
        reflection_sym : bool, optional
            If true, enable reflection symmetry on the qubit axis. Default is False.
    max_results_size : int, optional
        Max size of the observable evolution in output. Default is 100.
    del_data ; bool, optional
        If true, simulation data are deleted at the end of the simulation.
        Default is false.

    **Returns**

    output_dictionary : dictionary
        qcd_parameters : dictionary
            software_version : str
                Version of the software used for the simulation.
            initial_state : CircuitState
                See Parameters
            machine : dictionary
                See Parameters
            qcd_instructions : dictionary
                See Parameters
            simulation_instructions : dictionary
                See Parameters
        qcd_results : dictionary
            computational_time : float
                total computational time of the simulated annealing.
            initial_energy : float
                Initial energy
            best_state : AbstractCircuitState
                Describes the lowest infidelity equivalent state at the end of the
                simulation.
            final_equivalence_ratio : float, float
                Salpled probability of a final circuit equivalent to the initial
                one, sampled probability of a final circuit not equivalent to the
                initial one.
            energy_evolution : numpy.array
                A matrix that associate to each time the expectation value of the
                energy at that time.
            inf_energy_evolution : list of (float, dictionary)
                A list of tuples, the first element of each tuple is the time, the
                second element is a dictionary that associates to each possible enrgy
                a probability.
            norm_evolution : list of (float, float)
                A matrix that associate to each time the total sampled probability
                of the state at that time.

    """

    if input_circuit.dim != 2:
        raise ValueError("Quantum dinamics only implemented for 1d qubit lattices")

    if input_circuit.is_continuous:
        raise ValueError("Quantum dinamics only implemented for discrete gates set.")

    if "annealing_schedule" not in qcd_instructions:
        qcd_instructions["annealing_schedule"] = "A"

    if "max_rules_volume" not in qcd_instructions:
        qcd_instructions["max_rules_volume"] = 100

    if "rules_classes" not in qcd_instructions:
        qcd_instructions["rules_classes"] = "all"

    if "generators" not in qcd_instructions:
        qcd_instructions["generators"] = "std"

    if "svd_mode" not in simulation_instructions:
        simulation_instructions["svd_mode"] = "V"

    if "gs_search_iter" not in simulation_instructions:
        simulation_instructions["gs_search_iter"] = 3

    if "time_evolution_mode" not in simulation_instructions:
        simulation_instructions["time_evolution_mode"] = 5

    if "mpo_mode" not in simulation_instructions:
        simulation_instructions["mpo_mode"] = 4

    if "collapsed" not in simulation_instructions:
        simulation_instructions["collapsed"] = False

    if "reflection_sym" not in simulation_instructions:
        simulation_instructions["reflection_sym"] = False

    if "simulation_name" not in simulation_instructions:
        simulation_instructions["simulation_name"] = "unnamed"

    if "has_checkpoints" not in simulation_instructions:
        simulation_instructions["has_checkpoints"] = True

    machine["gates"] = sorted(list(machine["gates"]))

    # ------------ Build quantum model ---------------

    times = 2 ** math.ceil(math.log2(input_circuit.times))
    if simulation_instructions["collapsed"]:
        tn_type = 6
        qubits = input_circuit.qubits[0]
        shape = (times, input_circuit.qubits[0])
        collapse_map = CollapseMap(
            machine["gates"],
            input_circuit.times,
            times,
            qubits,
            reflection_sym=simulation_instructions["reflection_sym"],
        )
        (shape, my_ops, my_obs, model,) = get_collapsed_quantum_compilation_model(
            input_circuit,
            machine,
            qcd_instructions,
            shape,
            collapse_map,
        )
    else:
        tn_type = 5
        if simulation_instructions["reflection_sym"]:
            raise NotImplementedError(
                "Reflection symmetry not yet implemented in non-collapsed symulation."
            )
        qubits = 2 ** math.ceil(math.log2(input_circuit.qubits[0]))
        shape = (times, qubits)
        collapse_map = None
        shape, my_ops, my_obs, model = get_quantum_compilation_model(
            input_circuit, machine, qcd_instructions, shape
        )

    input_folder = (
        "simulations_data/input_qcd_" + simulation_instructions["simulation_name"]
    )

    output_folder = (
        "simulations_data/output_qcd_" + simulation_instructions["simulation_name"]
    )

    print(
        "The symulation involves ",
        len(my_ops.ops),
        " local operators with local dimension",
        len(my_ops.ops["id"]),
        ".",
        "Output folder: ",
        output_folder,
    )

    if del_data:
        input_folder = "tmp/" + input_folder
        output_folder = "tmp/" + output_folder

    my_obs += qtl.observables.TNState2File(output_folder + "/system_state", "F")

    # ---------------- Define the dynamics ----------------
    annealing_t = qcd_instructions["annealing_T"]
    delta_t = simulation_instructions["delta_t"]
    steps = int(annealing_t / delta_t)
    measurement_period = int(annealing_t / (delta_t * max_results_size))
    if measurement_period == 0:
        measurement_period = 1
    quench = qtl.DynamicsQuench(
        [delta_t] * steps,
        measurement_period=measurement_period,
        time_evolution_mode=simulation_instructions["time_evolution_mode"],
    )

    if qcd_instructions["annealing_schedule"] == "A":
        quench["alpha"] = lambda tt, params: 1 - tt / params["annealing_T"]
        quench["beta"] = (
            lambda tt, params: 2 * tt / params["annealing_T"]
            if (tt < params["annealing_T"] / 2)
            else 2 - 2 * tt / params["annealing_T"]
        )
        quench["gamma"] = lambda tt, params: tt / params["annealing_T"]

    elif qcd_instructions["annealing_schedule"] == "B":
        quench["alpha"] = (
            lambda tt, params: 1 - 2 * tt / params["annealing_T"]
            if (tt < params["annealing_T"] / 2)
            else 0
        )
        quench["beta"] = (
            lambda tt, params: 2 * tt / params["annealing_T"]
            if (tt < params["annealing_T"] / 2)
            else 2 - 2 * tt / params["annealing_T"]
        )
        quench["gamma"] = (
            lambda tt, params: 0
            if (tt < params["annealing_T"] / 2)
            else -1 + 2 * tt / params["annealing_T"]
        )

    else:
        raise NotImplementedError("This annealing schedule option is not implemented.")

    params = {
        "L": shape,
        "alpha": 1.0,
        "beta": 0.0,
        "gamma": 0.0,
        "annealing_T": annealing_t,
        "annealing_schedule": qcd_instructions["annealing_schedule"],
        "Quenches": [quench],
        "exclude_from_hash": ["Quenches", "energies"],
    }

    # ---------------- Running or loading the simulation ----------------

    my_conv = qtl.convergence_parameters.TNConvergenceParameters(
        max_iter=simulation_instructions["gs_search_iter"],
        max_bond_dimension=simulation_instructions["max_bond_dimension"],
        data_type="C",
        svd_ctrl=simulation_instructions["svd_mode"],
    )

    simulation = qtl.QuantumGreenTeaSimulation(
        model,
        my_ops,
        my_conv,
        my_obs,
        tensor_backend=2,
        tn_type=tn_type,
        mpo_mode=simulation_instructions["mpo_mode"],
        folder_name_input=input_folder,
        folder_name_output=output_folder,
        store_checkpoints=simulation_instructions["has_checkpoints"],
        verbosity=0,
    )

    sim_status = simulation.status([params])

    if os.path.isfile(output_folder + "/SIM_TIME"):
        print(
            "\nThis simulation has been runned in past and is stored in "
            + output_folder
            + ". Postprocessing data...\n"
        )
        with open(output_folder + "/SIM_TIME", "r") as file:
            computational_time = float(file.read())

    elif sim_status[0] == 1:
        print("\nRunning simulation...\n")
        tic = tictoc()
        simulation.run(
            [params],
            delete_existing_folder=not simulation_instructions["has_checkpoints"],
        )
        toc = tictoc()
        computational_time = toc - tic
        with open(output_folder + "/SIM_TIME", "a") as file:
            file.write(str(computational_time))

    elif sim_status[1] == 1:
        print("\nRestarting crashed simulation...")
        print("WARNING: the computational time will restart!\n")
        tic = tictoc()
        simulation.run(
            [params],
            delete_existing_folder=not simulation_instructions["has_checkpoints"],
        )
        toc = tictoc()
        computational_time = 0
        with open(output_folder + "/SIM_TIME", "a") as file:
            file.write(str(computational_time))

    else:
        raise ValueError(
            "Simulation status is "
            + str(sim_status)
            + " and "
            + output_folder
            + "/SIM_TIME does not exist."
        )

    # ---------------- Postprocessing simulation results ----------------
    real_circuit_shape = (input_circuit.times, input_circuit.qubits[0])

    qcd_parameters = {
        "software_version": "vulqano version " + str(__version__),
        "input_circuit": input_circuit,
        "machine": machine,
        "qcd_instructions": qcd_instructions,
        "simulation_instructions": simulation_instructions,
    }
    qcd_results = {}
    qcd_results["computational_time"] = computational_time

    # Initial state
    static_obs = simulation.get_static_obs(params)
    initial_ttn_state = static_obs[output_folder + "/system_state"]
    circuits_and_probabilities = CircuitsFromTN(
        initial_ttn_state, machine["gates"], shape, real_circuit_shape, collapse_map
    ).circuits_and_probabilities
    probabilities = [
        circuit_and_probability[1]
        for circuit_and_probability in circuits_and_probabilities
    ]
    max_index = probabilities.index(max(probabilities))
    initial_circuit, max_prob = circuits_and_probabilities[max_index]
    if max_prob < 0.99:
        raise ValueError(
            "The state at the beginning of the annealing process "
            + "seems not to be a state of the computational basis."
        )
    if not np.array_equal(initial_circuit.vector, input_circuit.vector):
        raise ValueError(
            "The state at the beginning of the annealing process "
            + "does not encode the input circuit."
        )
    qcd_results["initial_energy"] = initial_circuit.get_energy(machine["hamiltonian"])

    # Energy evolution
    dynamics_obs = [
        xxx for xxx in simulation.get_dynamic_obs(params)[0] if xxx is not None
    ]
    energies = [float(entry["energy"]) for entry in dynamics_obs]
    time_steps = np.cumsum(params["Quenches"][0].get_dt_grid(params))[
        ::measurement_period
    ][: len(dynamics_obs)]

    qcd_results["energy_evolution"] = list(zip(time_steps, energies))

    # normalization, infidelity energy, infidelity energy std evolution
    ttn_states = [
        dynamics_obs[ii][output_folder + "/system_state"]
        for ii in range(len(dynamics_obs))
    ]
    norms = []
    infidelities = []
    for ttn_state in ttn_states:
        circuits_from_tn = CircuitsFromTN(
            ttn_state, machine["gates"], shape, real_circuit_shape, collapse_map
        )
        infidelities.append(
            circuits_from_tn.get_classical_energy_statistics(machine["hamiltonian"])
        )
        norms.append(circuits_from_tn.sampled_probability)
    qcd_results["norm_evolution"] = list(zip(time_steps, norms))
    qcd_results["inf_energy_evolution"] = list(zip(time_steps, infidelities))

    # Final circuit states
    final_ttn_state = dynamics_obs[-1][output_folder + "/system_state"]
    equivalent_probability, not_equivalent_probability, best_state = CircuitsFromTN(
        final_ttn_state, machine["gates"], shape, real_circuit_shape, collapse_map
    ).get_equivalence_ratio_and_best_state(
        input_circuit,
        machine["hamiltonian"],
    )
    qcd_results["final_equivalence_ratio"] = (
        equivalent_probability,
        not_equivalent_probability,
    )
    qcd_results["best_state"] = best_state

    # If the simulation data durectory is tmp, remove it
    if os.path.exists("tmp") and os.path.isdir("tmp"):
        shutil.rmtree("tmp")

    output_dictionary = {"qcd_parameters": qcd_parameters, "qcd_results": qcd_results}

    return output_dictionary


def base_unit_test(input_circuit, machine, qcd_instructions, simulation_instructions):
    """
    Define simple general scheme for unit tests of the quantum annealing.


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
    qcd_instructions : dictionary
        See .quantum_circuit_dynamics .
    simulation_instructions : dictionary
        See .quantum_circuit_dynamics .

    **Returns**

    bool
        True if each possible final circuit is equivalent to the inital one.

    """

    simulation_instructions["has_checkpoints"] = False

    output_dictionary = quantum_circuit_dynamics(
        input_circuit, machine, qcd_instructions, simulation_instructions, del_data=True
    )

    qcd_results = output_dictionary["qcd_results"]

    print("\n\nComputational time: ", qcd_results["computational_time"])
    print(
        "Probability of equivalent final circuit >= ",
        qcd_results["final_equivalence_ratio"][0],
    )
    return qcd_results["final_equivalence_ratio"][0] > 1 - 10 ** (-2)


def unit_test():
    """
    Perform a quantum annealing with a small circuit and check for the
    final circuits infidelity.

    **Returns**

    bool
        True if each possible final circuit is equivalent to the inital one.
    """
    # ---------------- Set the optimiziation problem ----------------

    input_circuit = AbstractCircuitState(
        np.array(
            [
                ["Z", "Z", "CZ", "busy"],
                ["SWAP", "busy", "Z", "idle"],
                ["Z", "idle", "CZ", "busy"],
            ]
        ),
        "input_circuit",
    )

    n_q = input_circuit.qubits[0]
    n_t = input_circuit.times - 1

    circuit_area_mask = np.concatenate(
        (
            np.full((0, n_q), False),
            np.full((n_t, n_q), True),
            np.full((1, n_q), False),
        )
    )

    machine = {
        "gates": {"Z", "CZ", "SWAP"},
        "hamiltonian": (
            (np.array([["Z"]]), 1, circuit_area_mask),
            (np.array([["idle"]]), 1, circuit_area_mask),
            (np.array([["CZ"]]), 5, circuit_area_mask),
            (np.array([["SWAP"]]), 50, circuit_area_mask),
            (np.array([["CZ", "any", "CZ"]]), 50, circuit_area_mask),
            (np.full((1, n_q), "idle"), -n_q * 1, circuit_area_mask),
            (np.array([["Z"]]), 50, np.logical_not(circuit_area_mask)),
            (np.array([["CZ"]]), 50, np.logical_not(circuit_area_mask)),
        ),
    }

    qcd_instructions = {
        "annealing_T": 0.25,
    }

    simulation_instructions = {
        "delta_t": 0.05,
        "max_bond_dimension": 5,
        "simulation_name": "unit_test",
    }

    return base_unit_test(
        input_circuit, machine, qcd_instructions, simulation_instructions
    )


def unit_test_collapsed():
    """
    Perform a collapsed quantum annealing with a small circuit and check for the
    final circuits infidelity.

    **Returns**

    bool
        True if each possible final circuit is equivalent to the inital one.
    """

    input_circuit = AbstractCircuitState(
        np.array(
            [
                ["CZ", "busy"],
                ["SWAP", "busy"],
                ["CZ", "busy"],
                ["CZ", "busy"],
                ["CZ", "busy"],
                ["SWAP", "busy"],
                ["CZ", "busy"],
            ]
        ),
        "input_circuit",
    )

    n_q = input_circuit.qubits[0]
    n_t = input_circuit.times - 1

    circuit_area_mask = np.concatenate(
        (
            np.full((0, n_q), False),
            np.full((n_t, n_q), True),
            np.full((1, n_q), False),
        )
    )

    machine = {
        "gates": {"H", "CZ", "SWAP"},
        "hamiltonian": (
            (np.array([["idle"]]), 1, circuit_area_mask),
            (np.array([["CZ"]]), 5, circuit_area_mask),
            (np.array([["SWAP"]]), 50, circuit_area_mask),
            (np.array([["CZ", "any", "CZ"]]), 50, circuit_area_mask),
            (np.full((1, n_q), "idle"), -n_q * 1, circuit_area_mask),
            (np.array([["CZ"]]), 50, np.logical_not(circuit_area_mask)),
        ),
    }

    qcd_instructions = {
        "annealing_T": 0.25,
    }

    simulation_instructions = {
        "delta_t": 0.05,
        "max_bond_dimension": 25,
        "collapsed": True,
        "simulation_name": "unit_test_collapsed",
    }

    return base_unit_test(
        input_circuit, machine, qcd_instructions, simulation_instructions
    )


def unit_test_collapsed_sym():
    """
    Perform a collapsed quantum annealing with a small circuit and check for the
    final circuits infidelity. Enable reflection symmetry over qubit axis.

    **Returns**

    bool
        True if each possible final circuit is equivalent to the inital one.
    """

    input_circuit = AbstractCircuitState(
        np.array(
            [
                ["idle", "CZ", "busy", "idle"],
                ["CZ", "busy", "CZ", "busy"],
                ["idle", "CZ", "busy", "idle"],
                ["idle", "CZ", "busy", "idle"],
                ["H", "CZ", "busy", "H"],
                ["SWAP", "busy", "SWAP", "busy"],
                ["idle", "CZ", "busy", "idle"],
            ]
        ),
        "input_circuit",
    )

    n_q = input_circuit.qubits[0]
    n_t = input_circuit.times - 1

    circuit_area_mask = np.concatenate(
        (
            np.full((0, n_q), False),
            np.full((n_t, n_q), True),
            np.full((1, n_q), False),
        )
    )

    machine = {
        "gates": {"H", "CZ", "SWAP"},
        "hamiltonian": (
            (np.array([["idle", "any", "any", "idle"]]), 2, circuit_area_mask),
            (np.array([["any", "idle", "idle", "any"]]), 2, circuit_area_mask),
            (np.array([["any", "CZ", "busy", "any"]]), 5, circuit_area_mask),
            (np.array([["CZ", "busy", "CZ", "busy"]]), 35, circuit_area_mask),
            (np.array([["any", "SWAP", "busy", "any"]]), 25, circuit_area_mask),
            (np.array([["SWAP", "busy", "SWAP", "busy"]]), 50, circuit_area_mask),
            (np.full((1, n_q), "idle"), -n_q * 1, circuit_area_mask),
            (
                np.array([["idle", "any", "any", "idle"]]),
                50,
                np.logical_not(circuit_area_mask),
            ),
            (
                np.array([["any", "idle", "idle", "any"]]),
                50,
                np.logical_not(circuit_area_mask),
            ),
            (
                np.array([["any", "CZ", "busy", "any"]]),
                50,
                np.logical_not(circuit_area_mask),
            ),
            (
                np.array([["CZ", "busy", "CZ", "busy"]]),
                50,
                np.logical_not(circuit_area_mask),
            ),
        ),
    }

    qcd_instructions = {
        "annealing_T": 0.25,
        "generators": SYM_4_RULES_GENERATORS,
    }

    simulation_instructions = {
        "delta_t": 0.05,
        "max_bond_dimension": 25,
        "collapsed": True,
        "reflection_sym": True,
        "simulation_name": "unit_test_collapsed_sym",
    }

    return base_unit_test(
        input_circuit, machine, qcd_instructions, simulation_instructions
    )


if __name__ == "__main__":
    print(unit_test())
    print(unit_test_collapsed())
    print(unit_test_collapsed_sym())
