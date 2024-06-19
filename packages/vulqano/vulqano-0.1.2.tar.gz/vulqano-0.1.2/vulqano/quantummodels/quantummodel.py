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

We map the circuit in a (1+1) dimensional qudits lattice. The first coordinate labels
the time-step, the other coordinates label the qubit where a gate is executed, the state of
each qudit represents the corrisponding executed gate.
"""


from itertools import product
import numpy as np
import qtealeaves as qtl
from qtealeaves import modeling
from vulqano.rules.abstractdiscreterules import generate_discrete_abstract_rules
from vulqano.quantummodels.localquantumops import TNGateOperators


__all__ = [
    "get_quantum_compilation_model",
]


def get_quantum_compilation_model(
    input_circuit,
    machine,
    qcd_instructions,
    shape,
):
    """
    Maps the compilation problem into a quantum many-body system to simulate with qtealeaves.

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
                - H_ext = sum_i |idle><idle| is a 1-local Hamiltonian acting on
                the sites of the lattice that does not correspond to a circuit site.
                - H_initial is 1-local Hamiltonian having the initial circuit as ground
                state.
                - H_driving is the Hamiltonian that drives the evolution by creating
                superpositions of equivalent circuit..
                - H_final is the Hamiltonian that encodes the infidelity function.

    """

    def generate_op_names_array(arr_a, arr_b):
        """
        Take two matrix of gates [[GATEa_00, GATEa_01...]] and [[GATEb_00, GATEb_01...]]
        and returns a matrix of operators labels of the form
        [[GATEa_00->GATEb_00, GATEa_01->GATEb_01...]]

        **Arguments**

        arr_a : np.array of strings
            First matrix of gates.
        arr_b : np.array of strings
            Second matrix of gates.

        **Returns**

        arr_out : np.array of strings
            A matrix of operators labels like
            [[GATEa_00->GATEb_00, GATEa_01->GATEb_01...]]

        """
        arr_out = np.full(arr_a.shape, "any->any", dtype=object)
        for idx, gate_a in np.ndenumerate(arr_a):
            arr_out[idx] = gate_a + "->" + arr_b[idx]
        return arr_out

    def mask_conversion(mask_in, op_shape):
        """
        Convert a Vulqano operator mask (i.e., the operator can be applied to a
        rectangular region [x0:x1,y0:y1] iff np.any(mask[x0:x1,y0:y1]) is true)
        to a QunatumTEA callable operator mask (i.e., the operator can be applied
        to a rectangular region [x0:x1,y0:y1] iff mask[x0,y0] is true).
        If the input cirvuit volume is not a power of two, also enlarge the mask
        by adding false values.

        **Arguments**

        mask_in : np.array of bools
            Vulqano operator mask.
        op_shape : (times, qubits)
            Shape of the operator.

        **Returns**

        mask_function : callable
            QunatumTEA operator mask.

        """
        mask_out = np.full(shape, False)
        for time in range(mask_in.shape[0] + 1 - op_shape[0]):
            for qubit in range(mask_in.shape[1] + 1 - op_shape[1]):
                if np.all(
                    mask_in[time : time + op_shape[0], qubit : qubit + op_shape[1]]
                ):
                    mask_out[time, qubit] = True

        def mask_function(parameters, mask_out=mask_out):
            return mask_out

        return mask_function

    def build_external_hamiltonian(model):
        """
        Build an Hamiltonian that sets as idle all the lattice sites that are
        external to the ciruit area.

        **Arguments**

        model : qtealeaves.modeling.QuantumModel
            QuantumModel describing the evolution Hamiltonian.

        **Returns**

        None.

        """
        external_mask = np.full(shape, True)
        external_mask[: input_circuit.times, : input_circuit.qubits[0]] = np.full(
            (input_circuit.times, input_circuit.qubits[0]), False
        )

        def mask(parameters, external_mask=external_mask):
            return external_mask

        model += modeling.LocalTerm("idle->idle", mask=mask, prefactor=-1)

    def build_initial_hamiltonian(model, strength):
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
        mask = np.full(shape, False)
        for time, qubit in product(
            range(input_circuit.times), range(input_circuit.qubits[0])
        ):
            mask[time, qubit] = True
            operator_names = (
                input_circuit.vector[time, qubit]
                + "->"
                + input_circuit.vector[time, qubit]
            )
            model += modeling.LocalTerm(
                operator_names,
                strength=strength,
                prefactor=-1,
                mask=mask_conversion(mask, (1, 1)),
            )
            mask[time, qubit] = False

    def build_driving_hamiltonian(model, strength):
        """
        Build the driving Hamiltonian with the transitions that link equivalent
        circuits, add this Hamiltonian to the model.

        **Arguments**

        model : qtealeaves.modeling.QuantumModel
            QuantumModel describing the evolution Hamiltonian.
        strength : string
            Name of the coupling associated to the Hamiltonian.

        **Returns**

        None.

        """
        mask_all = np.full((input_circuit.times, input_circuit.qubits[0]), True)
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
                    np.product(abstract_rule.shape)
                    <= qcd_instructions["max_rules_volume"]
                )
            ):
                mask = mask_conversion(mask_all, abstract_rule.state_a.shape)
                operator_names_1 = generate_op_names_array(
                    abstract_rule.state_a, abstract_rule.state_b
                )
                operator_names_2 = generate_op_names_array(
                    abstract_rule.state_b, abstract_rule.state_a
                )
                if operator_names_1.shape[0] * operator_names_1.shape[1] == 1:
                    model += modeling.LocalTerm(
                        operator_names_1[0, 0], strength=strength, mask=mask
                    )
                    model += modeling.LocalTerm(
                        operator_names_2[0, 0], strength=strength, mask=mask
                    )
                else:
                    model += modeling.BlockTerm2D(
                        operator_names_1, strength=strength, mask=mask, has_obc=False
                    )
                    model += modeling.BlockTerm2D(
                        operator_names_2, strength=strength, mask=mask, has_obc=False
                    )

    def build_infidelity_hamiltonian(model, strength):
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
        for operator, weight, mask in machine["hamiltonian"]:
            if (operator.shape[0] <= input_circuit.times) and (
                operator.shape[1] <= input_circuit.qubits[0]
            ):
                operator_names = generate_op_names_array(operator, operator)
                if operator_names.shape[0] * operator_names.shape[1] == 1:
                    model += modeling.LocalTerm(
                        operator_names[0, 0],
                        strength=strength,
                        prefactor=weight,
                        mask=mask_conversion(mask, operator.shape),
                    )
                else:
                    model += modeling.BlockTerm2D(
                        operator_names,
                        strength=strength,
                        prefactor=weight,
                        mask=mask_conversion(mask, operator.shape),
                        has_obc=False,
                    )

    # ---------------- Define operators ----------------
    my_ops = TNGateOperators(["idle"] + machine["gates"])

    # ---------------- Define observables ----------------
    my_obs = qtl.observables.TNObservables()
    for gate in ["idle", "busy"] + machine["gates"]:
        my_obs += qtl.observables.TNObsLocal("<" + gate + ">", gate + "->" + gate)

    # ---------------- Build the model ----------------

    model = modeling.QuantumModel(2, "L", name="Circuit_optimization_mapping")
    build_external_hamiltonian(model)
    build_initial_hamiltonian(model, "alpha")
    build_driving_hamiltonian(model, "beta")
    build_infidelity_hamiltonian(model, "gamma")

    return (shape, my_ops, my_obs, model)
