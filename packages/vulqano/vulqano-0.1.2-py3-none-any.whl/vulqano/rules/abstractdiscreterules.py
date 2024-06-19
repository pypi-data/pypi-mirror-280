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
Define and generate abstract transformation rules linking equivalent
subcircuits that involve discrete gates.

A rule is described by a couple subcircuits. Each subciruits is
described by nested lists of strings, corresponding to n-dimensional arrays
of strings. The first index labels the time-step, the other indices label the
position of the qubit in the lattice. Each string denote the name of the
corresponding gate (see vulqano.gates.discretegates). The string "any"
indicates that the corresponding gate is an arbitrary gate, while the string
"any_rot" indicates that the corresponding gate is an arbitrary R_z rotation.
"""

import copy
import numpy as np
from vulqano.states import AbstractCircuitState
from vulqano.utils import (
    check_circuit_equivalence,
)
from vulqano.gates.discretegates import (
    GATES_DICTIONARY,
)
from vulqano.rules.standarddiscreterules import STD_DISCRETE_RULES_GENERATORS
from vulqano.rules.sym4rules import SYM_4_RULES_GENERATORS

__all__ = [
    "DiscreteTransformationRule",
    "generate_discrete_abstract_rules",
]


class DiscreteTransformationRule:
    """
    Abstract discrete transformation rules linking equivalent subcircuits.

    **Arguments**

    state_a : np.array of strings
        Array representing the first subcircuit.
    state_b : np.array of strings
        Array representing the second subcircuit.
    class_index : int
        Rules are grouped in classes, class_index labels the class of the rule.
    verify : bool
        If true, the rule is checked.

    **Attributes**

    state_a : np.array of strings
        Array representing the first subcircuit.
    state_b : np.array of strings
        Array representing the second subcircuit.
    shape : tuple of ints
        Shape of the subcircuits involved in the rule
    masks : (numpy mask,numpy mask)
        The first mask is true in correspondence of "any" gates. The second mask
        is true in correspondence of "any_rot" gates.
    class_index : int
        Rules are grouped in classes, class_index labels the class of the rule.
    counters : (int, int)
        The first int keeps track of how many times the rule has been applied
        by replacing a subcircuit state_a with a subcircuit state_b. The second
        int keeps track of how many times the rule has been applied by replacing
        a subcircuit state_b with a subcircuit state_a.
    involved_gates : set of strings
        Gates involved in the rule.
    """

    def __init__(self, state_a, state_b, class_index, verify=False):
        self.state_a = state_a
        self.state_b = state_b
        self.shape = self.state_a.shape
        self.masks = (
            np.equal(self.state_a, np.full(self.state_a.shape, "any", dtype=object)),
            np.equal(
                self.state_a, np.full(self.state_a.shape, "any_rot", dtype=object)
            ),
        )
        self.class_index = class_index
        self.counters = [0, 0]
        self.involved_gates = set()
        for gate in GATES_DICTIONARY:
            if (
                np.count_nonzero(self.state_a == gate)
                + np.count_nonzero(self.state_b == gate)
            ) > 0:
                self.involved_gates.add(gate)
        if verify:
            if not self.verify():
                raise ValueError(
                    "INVALID RULE: the circuits\n" + str(self) + "are not equivalent."
                )

    def __str__(self):
        """
        Generates a pictorial representation of the transformation rule.

        **Returns**

         : str
            A pictorial representation of the transformation rule.
        """
        return str(self.state_a) + "\n<====>\n" + str(self.state_b)

    def verify(self):
        """
        Verify the equivalence between the subcircuits linked by the rule.

        **Returns**

        check_result : bool
            True if the rule is valid (equivalent subcircuit).
        """
        first_circuit_vector = copy.deepcopy(self.state_a)
        second_circuit_vector = copy.deepcopy(self.state_b)
        first_circuit_vector[self.masks[0]] = "H"
        second_circuit_vector[self.masks[0]] = "H"
        first_circuit_vector[self.masks[1]] = "S"
        second_circuit_vector[self.masks[1]] = "S"
        check_result = check_circuit_equivalence(
            AbstractCircuitState(first_circuit_vector, "c0"),
            AbstractCircuitState(second_circuit_vector, "c1"),
        )
        return check_result


def rotate_state(state_vector):
    """
    Rotate a state:  [A, B, C] -> [[A, B, C]] and replaces eventual two-qubits
    gates with their rotated form.


     **Arguments**

    state_vector : np.array
        State to be rotated (GATES description)

    **Returns**

    state_vector : np.array
        Rotated state

    """
    state_vector = np.transpose(state_vector, (0, 2, 1))
    for idx, gate in np.ndenumerate(state_vector):
        if GATES_DICTIONARY[gate]["Connectivity"] == [1]:
            state_vector[idx] += "_r"
    return state_vector


def generate_discrete_abstract_rules(
    gates, dim, rules_classes="all", verify=False, generators="std"
):
    """
    Returns a list of discrete transformation rules.

    **Arguments**

    gates : set
        The set of gates involved in the transformation rules.
    dim : int
        Number of dimensions of the qubits lattice.
    rules_classes : str or list of ints, optional
        A list of the ints identifying the rule classes that we want to generate.
        Default is "all" and generates all the rule classes.
    verify : bool, optional
        If true, each rule is tested. Default is False.
    generators : "std" or list of generators, optional
        The list of generators producing the rules to be used. Default is "std",
        in this case a standard list of rules is used.

    **Returns**

    rules : list of DiscreteTransformationRule(s)
        The generated list of transition rules.
    """

    if dim > 3:
        raise NotImplementedError("Maximum implemented lattice dimension is 2.")

    gates_extended = copy.deepcopy(gates)
    gates_extended.add("idle")
    gates_extended.add("busy")
    gates_extended.add("any")
    gates_extended.add("any_rot")

    if generators == "std":
        generators = STD_DISCRETE_RULES_GENERATORS

    rules = []
    if rules_classes == "all":
        rules_classes = list(range(len(generators)))

    if set(rules_classes).issubset(set(range(len(generators)))) is not True:
        raise ValueError(
            "rules_classes must be a list of int from 0 to "
            + str(len(generators) - 1)
            + ' or "all".'
        )

    for class_index in rules_classes:
        for rule in generators[class_index]():
            state_a = np.array(rule[0], dtype=object)
            state_b = np.array(rule[1], dtype=object)

            if len(state_a.shape) == dim:
                abstract_rule = DiscreteTransformationRule(
                    np.copy(state_a),
                    np.copy(state_b),
                    class_index,
                    verify,
                )
                if abstract_rule.involved_gates.issubset(gates_extended):
                    rules.append(abstract_rule)

            if len(state_a.shape) == 2 and dim == 3:
                # [A, B, C] -> [[A, B, C]]
                state_a = np.expand_dims(state_a, 1)
                state_b = np.expand_dims(state_b, 1)
                abstract_rule = DiscreteTransformationRule(
                    np.copy(state_a),
                    np.copy(state_b),
                    class_index,
                    verify,
                )
                if abstract_rule.involved_gates.issubset(gates_extended):
                    rules.append(abstract_rule)

                if state_a.shape[-1] > 1:
                    # [[A, B, C]] -> [[A], [B], [C]]
                    state_a = rotate_state(state_a)
                    state_b = rotate_state(state_b)
                    abstract_rule = DiscreteTransformationRule(
                        np.copy(state_a),
                        np.copy(state_b),
                        class_index,
                        verify,
                    )
                    if abstract_rule.involved_gates.issubset(gates_extended):
                        rules.append(abstract_rule)
    return rules


def unit_test_2d():
    """
    Unit test to check if all the rules are valid.

    **Returns**
       : bool
    True if all the rules are valid.

    """
    generate_discrete_abstract_rules(
        {
            "T",
            "H",
            "CZ",
            "SWAP",
            "S",
            "Z",
            "Tdg",
            "Sdg",
            "RZ5",
            "RZ5dg",
            "RZ6",
            "RZ6dg",
        },
        2,
        verify=True,
    )
    return True


def unit_test_3d():
    """
    Unit test to check if all the rules are valid.

    **Returns**
       : bool
    True if all the rules are valid.

    """
    generate_discrete_abstract_rules(
        {
            "T",
            "H",
            "CZ",
            "CZ_r",
            "SWAP",
            "SWAP_r",
            "S",
            "Z",
            "Tdg",
            "Sdg",
            "RZ5",
            "RZ5dg",
            "RZ6",
            "RZ6dg",
        },
        3,
        verify=True,
    )
    return True


def unit_test_sym4():
    """
    Unit test to check if all the rules are valid.

    **Returns**
       : bool
    True if all the rules are valid.

    """
    generate_discrete_abstract_rules(
        {
            "H",
            "CZ",
            "SWAP",
        },
        2,
        verify=True,
        generators=SYM_4_RULES_GENERATORS,
    )
    return True


if __name__ == "__main__":
    print(unit_test_2d())
    print(unit_test_3d())
