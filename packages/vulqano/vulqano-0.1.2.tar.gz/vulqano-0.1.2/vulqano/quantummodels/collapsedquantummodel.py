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
Here we define functions to map the compilation problem into a quantum many-body
system to simulate with qtealeaves.

In the collapsed mapping, we map the circuit in a q-dimensional qudits lattice.
The coordinate labels the time-step, and the state of each qudit represents
a possible time-step.
"""


import numpy as np
import qtealeaves as qtl
from qtealeaves import modeling
from vulqano.gates.discretegates import GATES_DICTIONARY
from vulqano.rules.abstractdiscreterules import generate_discrete_abstract_rules
from vulqano.quantummodels.localquantumops import TNTimeStepOperators


__all__ = [
    "reverse_time_step",
    "CollapseMap",
    "get_collapsed_quantum_compilation_model",
]


def reverse_time_step(state):
    """
    Reverse the order of the qubits in a time step.

    **Arguments**

    state : list of strings
        List of gate names that describe the time step.

    **Returns**

    reverse : list of strings
        List of gate names that describe the reversed time step.

    """
    reverse = state.copy()
    for ii, gate in enumerate(reverse):
        if gate == "busy":
            reverse[ii] = reverse[ii - 1]
            reverse[ii - 1] = "busy"
    reverse.reverse()
    return reverse


class CollapseMap:
    """
    Maps the circuit states and operators from a (1+1)d lattice to a 1d lattice
    by collasing the qubit axis. Each possible gates configuration of a time step is
    mapped to a single local state.

    **Arguments**

    gates : set of str
        Gates allowed on the target machine (fictitious gates such as "idle "and
        "busy" are excluded).
    circuit_times : int
        number of time steps allowed for the cicuit.
    n_t : int
        number of time steps represented in the lattice.
    n_q : int
        Number of qubits of the target machine.
    reflection_sym : bool, optional.
        If true, only the supergates that represent time-steps invariant under a
        reflection on the qubits axis are included. Default is false. WARNING:
        needs reflection invariant infidelity and transition rules.

    **Attributes**

    gates : set of str
        Gates allowed on the target machine (fictitious gates such as "idle "and
        "busy" are excluded).
    circuit_times : int
        number of time steps allowed for the cicuit.
    n_t : int
        number of time steps represented in the lattice.
    n_q : int
        Number of qubits of the target machine.
    collapsed_gates : list
        A list of each possible time-step configuration, identified by a string
        "gate_0|gate_1|...|gate_n_q".
    reflection_sym : bool
        If true, only the supergates that represent time-steps invariant under a
        reflection on the qubits axis are included.
    """

    def __init__(self, gates, circuit_times, n_t, n_q, reflection_sym=False):
        self.gates = sorted(list(set(gates).union({"idle"})))
        self.n_q = n_q
        self.n_t = n_t
        self.circuit_times = circuit_times

        for gate in self.gates:
            if gate not in GATES_DICTIONARY:
                raise ValueError("Gate " + gate + " not in GATES_DICTIONARY.")

        states = [[gate] for gate in self.gates]

        def increase(lst, is_last=False):
            if GATES_DICTIONARY[lst[-1]]["Connectivity"] == []:
                for gate in self.gates:
                    if (not is_last) or GATES_DICTIONARY[gate]["Connectivity"] == []:
                        yield lst + [gate]

            elif GATES_DICTIONARY[lst[-1]]["Connectivity"] == [1]:
                yield lst + ["busy"]
            else:
                raise NotImplementedError(
                    "The connectivity of the gate "
                    + lst[-1]
                    + " can not be managed by CollapseMap"
                )

        for _ in range(1, self.n_q - 1):
            states = [new_state for state in states for new_state in increase(state)]
        states = [
            new_state for state in states for new_state in increase(state, is_last=True)
        ]

        self.reflection_sym = reflection_sym
        if reflection_sym:
            symmetric_states = []
            for state in states:
                reverse = reverse_time_step(state)
                if state == reverse:
                    symmetric_states.append(state)
            states = symmetric_states

        collapsed_gates = ["|".join(state) for state in states]

        self.collapsed_gates = sorted(collapsed_gates)

    def collapse_substate(self, state, position=0):
        """
        Collapse a circuit or a subcircuit.

        **Arguments**

        state : matrix of strings
            Description of the local (sub) circuit to be collapsed. If the number
            of qubits of the subcircuit is smaller than the number of qubits of
            the circuit, the remaining qubits are filled with "any" (identity operator)
            gates.
        position : int, optional
            Qubit position of the subcircuit. The default is 0.

        **Returns**

        collapsed_state : list of strings
            Collapsed decsription of the state, encoded as a list of supergates names.

        """
        offset_up = ["any" for ii in range(position)]
        offset_down = ["any" for ii in range(self.n_q - position - len(state[0]))]
        collapsed_state = []
        for time_step in state:
            collapsed_state.append(offset_up + list(time_step) + offset_down)

        return collapsed_state

    def decollapse_state(self, collapsed_state):
        """
        Transform a collapsed a circuit to a non-collapsed circuit.

        **Arguments**

        collapsed_state : list of strings
            Collapsed decsription of the state, encoded as a list of supergates names.

        **Returns**

        state : matrix of strings
            Description of the circuit state in terms of gates at each qubit and time-step.
        """
        state = []
        for time_step in range(self.circuit_times):
            state.append(collapsed_state[time_step].split("|"))
        return state

    def collapse_rule(self, rule):
        """
        Generates a collapsed version of a transition rule.

        **Arguments**

        rule : instance of DiscreteTransformationRule
            Transition rule to be encoded in a set of collapsed rules.

        **Yields**

        List of collapsed rules encoding the applicat of the original rule to
        different slices of qubits.

        collapsed_state_a : list of strings or None
            Collapsed decsription of the state_a of the rule, encoded as a list
            of supergates names. If the reflection symmetry is enabled, returns
            None for non symmetric states.
        collapsed_state_b : list of strings or None
            Collapsed decsription of the state_b of the rule, encoded as a list
            of supergates names. If the reflection symmetry is enabled, returns
            None for non symmetric states.
        """
        if np.any(rule.state_a == "any_rot"):
            raise NotImplementedError(
                "Collapsing rules with 'any_rot' gate not implemented."
            )
        for position in range(1 + self.n_q - rule.shape[1]):
            collapsed_state_a = self.collapse_substate(rule.state_a, position=position)
            collapsed_state_b = self.collapse_substate(rule.state_b, position=position)
            yield (collapsed_state_a, collapsed_state_b)

    def collapse_hamiltonian_term(self, operator, prefactor, mask):
        """
        Generate a collapsed version of an Hamiltonian term.

        **Parameters**

        operator : np.array of strings
                Block of local operators, expressed as
                tensor product of the local operators.
        prefactor : float
                Coupling of the term in the Hamiltonian
        mask : mask
                The operator is applied on a region A if
                the mask is true in each site of the region.
        """
        operator = operator.astype("object")
        for ii, gate in enumerate(operator[0]):
            if GATES_DICTIONARY[gate]["Connectivity"] == [1]:
                if ii + 1 < len(operator[0]):
                    operator[0][ii + 1] = "busy"
                else:
                    operator = np.concatenate((operator, [["busy"]]), axis=1)

        for qubit in range(mask.shape[1] + 1 - operator.shape[1]):
            collapsed_operator = self.collapse_substate(operator, position=qubit)

            if self.reflection_sym and any(
                (time_step != reverse_time_step(time_step))
                for time_step in collapsed_operator
            ):
                print(
                    "WARNING: the operator ",
                    collapsed_operator,
                    "<->",
                    collapsed_operator,
                    " is not symmetric. It will not be included in the Infidelity Hamiltonian.",
                )
                yield (None, None, None)

            else:
                collapsed_mask = np.full(self.n_t, False)
                for time in range(mask.shape[0] + 1 - operator.shape[0]):
                    if np.all(
                        mask[
                            time : time + operator.shape[0],
                            qubit : qubit + operator.shape[1],
                        ]
                    ):
                        collapsed_mask[time] = True
                yield (collapsed_operator, prefactor, collapsed_mask)

    def build_external_hamiltonian(self, model):
        """
        Build an Hamiltonian that sets as idle all the lattice sites that are
        external to the ciruit area.

        **Arguments**

        model : qtealeaves.modeling.QuantumModel
            QuantumModel describing the evolution Hamiltonian.

        **Returns**

        None.

        """
        all_idle_supergate = "|".join(["idle" for ii in range(self.n_q)])
        mask_array = np.full(self.n_t, True)
        mask_array[: self.circuit_times] = np.full(self.circuit_times, False)

        def external_mask(parameters, mask_array=mask_array):
            return mask_array

        model += modeling.LocalTerm(
            all_idle_supergate + "->" + all_idle_supergate,
            mask=external_mask,
            prefactor=-1 * self.n_q,
        )

    def build_initial_hamiltonian(self, state, model, strength, position=0):
        """
        Build an Hamiltonian having the initial state as non-degenerate
        ground state, add this Hamiltonian to the model

        **Arguments**

        model : qtealeaves.modeling.QuantumModel
            QuantumModel describing the evolution Hamiltonian.
        strength : string
            Name of the coupling associated to the Hamiltonian.

        **Returns**

        None.

        """
        collapsed_state = self.collapse_substate(state, position=position)

        if self.reflection_sym and any(
            (time_step != reverse_time_step(time_step)) for time_step in collapsed_state
        ):
            raise ValueError("The initial state " + str(state) + " is not symmetric.")

        for ii, time_step in enumerate(collapsed_state):
            mask_array = np.full(self.n_t, False)
            mask_array[ii] = True

            def initial_mask(parameters, mask_array=mask_array):
                return mask_array

            model += modeling.LocalTerm(
                "|".join(time_step) + "->" + "|".join(time_step),
                strength=strength,
                prefactor=-1 * self.n_q,
                mask=initial_mask,
            )

    def build_driving_hamiltonian(self, rule, model, strength):
        """
        Build a term in the driving Hamiltonian encoding a transition
        rule, add this Hamiltonian to the model.

        **Arguments**

        rule: instance of DiscreteTransformationRule
            Transition rule to be encoded as operator.
        model : qtealeaves.modeling.QuantumModel
            QuantumModel describing the evolution Hamiltonian.
        strength : string
            Name of the coupling associated to the Hamiltonian term.

        **Returns**

        None.
        """
        for state_a, state_b in self.collapse_rule(rule):
            if self.reflection_sym and (
                any(
                    (time_step != reverse_time_step(time_step)) for time_step in state_a
                )
                or any(
                    (time_step != reverse_time_step(time_step)) for time_step in state_a
                )
            ):
                print(
                    "WARNING: the operator ",
                    state_a,
                    "<->",
                    state_b,
                    " is not symmetric. It will not be included in the Driving Hamiltonian.",
                )

            else:
                operator_name_1 = [
                    "|".join(time_step_a) + "->" + "|".join(time_step_b)
                    for (time_step_a, time_step_b) in zip(state_a, state_b)
                ]
                operator_name_2 = [
                    "|".join(time_step_b) + "->" + "|".join(time_step_a)
                    for (time_step_a, time_step_b) in zip(state_a, state_b)
                ]
                mask_array = np.full(self.n_t, False)
                mask_array[: 1 + self.circuit_times - len(state_a)] = np.full(
                    1 + self.circuit_times - len(state_a), True
                )

                def driving_mask(parameters, mask_array=mask_array):
                    return mask_array

                if len(operator_name_1) == 1:
                    model += modeling.LocalTerm(
                        operator_name_1[0], strength=strength, mask=driving_mask
                    )
                    model += modeling.LocalTerm(
                        operator_name_2[0], strength=strength, mask=driving_mask
                    )
                else:
                    model += modeling.StringTerm1D(
                        operator_name_1,
                        strength=strength,
                        mask=driving_mask,
                        has_obc=False,
                    )
                    model += modeling.StringTerm1D(
                        operator_name_2,
                        strength=strength,
                        mask=driving_mask,
                        has_obc=False,
                    )

    def build_infidelity_hamiltonian(self, hamiltonian, model, strength):
        """
        Build an Hamiltonian that extimated the circuit infidelity, add this
        Hamiltonian to the model

        **Arguments**

        model : qtealeaves.modeling.QuantumModel
            QuantumModel describing the evolution Hamiltonian.
        strength : string
            Name of the coupling associated to the Hamiltonian.

        **Returns**

        None.

        """
        for operator, prefactor, mask in hamiltonian:
            for (
                collapsed_operator,
                prefactor,
                collapsed_mask,
            ) in self.collapse_hamiltonian_term(operator, prefactor, mask):
                if collapsed_operator is not None:
                    operator_name = [
                        "|".join(time_step) + "->" + "|".join(time_step)
                        for time_step in collapsed_operator
                    ]

                    def infidelity_mask(parameters, collapsed_mask=collapsed_mask):
                        return collapsed_mask

                    if len(operator_name) == 1:
                        model += modeling.LocalTerm(
                            operator_name[0],
                            strength=strength,
                            prefactor=prefactor,
                            mask=infidelity_mask,
                        )
                    else:
                        model += modeling.StringTerm1D(
                            operator_name,
                            strength=strength,
                            prefactor=prefactor,
                            mask=infidelity_mask,
                            has_obc=False,
                        )


def get_collapsed_quantum_compilation_model(
    input_circuit,
    machine,
    qcd_instructions,
    shape,
    collapse_map,
):
    """
    Maps the compilation problem into a quantum many-body system to simulate with qtealeaves.
    In this collapsed mapping, each qudit encodes a time step of the circuit.

    **Arguments**

    input_circuit :  instance of ``AbstractCircuitState``
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
    shape : tuple of ints
        Shape of the lattice where the circuit is encoded, including fictitious
        sites added to fit in a TTN.
    collapse_map : instance of ``CollapseMap``
        Describes how each possible time step is associated to a qudit state.

    **Returns**

    shape : tuple of ints
        Shape of the lattice where the circuit is encoded, including fictitious
        sites added to fit in a TTN.
    my_ops : instance of ``qtealeaves.operators.TNOperators``
        Operators that transform a gate state into another gate state.
    my_obs : instance of ``qtealeaves.observables.TNObservables``
        Defines the observables of the simulation. For details,
        check the corresponding class.
    model : instance of ``qtealeaves.modeling.QuantumModel``
        System Hamiltonian in the form

        H = H_ext + alpha*H_initial + beta*H_driving + gamma*H_final

        where:

        -H_ext = sum_i |idle><idle|
                is a 1-local Hamiltonian acting on the sites of the lattice that does not correspond to a circuit site.
        -H_initial
                is 1-local Hamiltonian having the initial circuit as ground state.
        -H_driving
                is the Hamiltonian that drives the evolution by creating superpositions of equivalent circuit.
        -H_final
                is the Hamiltonian that encodes the infidelity function.
    """
    if input_circuit.dim != 2:
        raise NotImplementedError(
            "Collapsed quantum compilation only implemented for 1d qubits lattices."
        )

    # ---------------- Define observables ----------------
    my_obs = qtl.observables.TNObservables()
    for supergate_name in collapse_map.collapsed_gates:
        my_obs += qtl.observables.TNObsLocal(
            "<" + supergate_name + ">", supergate_name + "->" + supergate_name
        )

    # ---------------- Build the model ----------------
    model = modeling.QuantumModel(1, "L", name="Collapsed_circuit_optimization_mapping")
    collapse_map.build_external_hamiltonian(model)

    collapse_map.build_initial_hamiltonian(input_circuit.vector, model, "alpha")

    for abstract_rule in generate_discrete_abstract_rules(
        set(machine["gates"]),
        2,
        rules_classes=qcd_instructions["rules_classes"],
        generators=qcd_instructions["generators"],
    ):
        if (
            (abstract_rule.state_a.shape[0] <= input_circuit.times)
            and (abstract_rule.state_a.shape[1] <= input_circuit.qubits[0])
            and (
                np.product(abstract_rule.shape) <= qcd_instructions["max_rules_volume"]
            )
        ):
            collapse_map.build_driving_hamiltonian(abstract_rule, model, "beta")

    collapse_map.build_infidelity_hamiltonian(machine["hamiltonian"], model, "gamma")

    time_step_transformations = [
        time_step_configuration + "->" + time_step_configuration
        for time_step_configuration in collapse_map.collapsed_gates
    ]
    for elem in model.hterms:
        for op_tuple in elem.collect_operators():
            if op_tuple[0] not in time_step_transformations:
                time_step_transformations.append(op_tuple[0])

    # ---------------- Define operators ----------------
    my_ops = TNTimeStepOperators(
        collapse_map.collapsed_gates, time_step_transformations
    )

    shape = (shape[0],)

    return (shape, my_ops, my_obs, model)
