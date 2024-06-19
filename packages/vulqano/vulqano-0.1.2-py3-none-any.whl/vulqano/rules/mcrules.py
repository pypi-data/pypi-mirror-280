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
Transform the abstract transformation rules in Markov chain tranformation rules.

The difference between abstract rules and Markov chain rules is that in abstract
rules the gates are encoded as strings, while in Markov chain rules the gates are
labeled by integers. This different encoding allows to more quickly check whether
the rule applies to a circuit state.
"""
from vulqano.rules.abstractdiscreterules import (
    DiscreteTransformationRule,
    generate_discrete_abstract_rules,
)
from vulqano.rules.abstractcontinuousrules import (
    ContinuousTransformationRule,
    generate_continuous_abstract_rules,
)
from vulqano.gates.discretegates import (
    gate_labels_to_ints as discrete_array_strings_to_ints,
)
from vulqano.gates.continuousgates import (
    gate_labels_to_ints as continuous_array_strings_to_ints,
)


__all__ = [
    "generate_discrete_mcrules",
    "generate_continuous_mcrules",
]


class DiscreteMCRule(DiscreteTransformationRule):
    """
    Markov chain transformation rule that links equivalent subcircuits involving
    discrete gates.

    **Arguments**

    discrete_abstract_rule : DiscreteTransformationRule
        DiscreteTransformationRule to be converted to a DiscreteMCRule.

    **Attributes**

    state_a : np.array of ints
        Array representing the first subcircuit.
    state_b : np.array of ints
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

    def __init__(self, discrete_abstract_rule):
        super().__init__(
            discrete_abstract_rule.state_a,
            discrete_abstract_rule.state_b,
            discrete_abstract_rule.class_index,
        )
        self.state_a = discrete_array_strings_to_ints(self.state_a)
        self.state_b = discrete_array_strings_to_ints(self.state_b)


class ContinuousMCRule(ContinuousTransformationRule):
    """
    Markov chain transformation rule that links equivalent subcircuits involving
    continuous gates.

    **Arguments**

    continuous_abstract_rule : DiscreteTransformationRule
        DiscreteTransformationRule to be converted to a DiscreteMCRule.


    **Attributes**

    state_a : np.array of strings
        Array representing the first subcircuit.
    state_b : np.array of strings
        Array representing the second subcircuit.
    shape : tuple of ints
        Shape of the subcircuits involved in the rule
    any_mask : numpy mask
        True in correspondence of "any" gates.
    amplitudes_condition : np_array -> bool
        True if the rule can be applied.
    rot_transformation_func : np_array -> np.array
        A function for transforming rotation amplitudes.
    test_rot_amplitudes : np.array
        np.array of parameters used to completely specify an input circuit to test
        the validity of the rule.
    class_index : int
        Rules are grouped in classes, class_index labels the class of the rule.
    counters : (int, int)
        The first int keeps track of how many times the rule has been applied
        by replacing a subcircuit state_a with a subcircuit state_b. The second
        int is zero for continuous rules.
    involved_gates : set of strings
        Gates involved in the rule.
    """

    def __init__(self, continuous_abstract_rule):
        super().__init__(
            continuous_abstract_rule.state_a,
            continuous_abstract_rule.state_b,
            continuous_abstract_rule.class_index,
            continuous_abstract_rule.amplitudes_condition,
            continuous_abstract_rule.rot_transformation_func,
            continuous_abstract_rule.test_rot_amplitudes,
        )

        self.state_a = continuous_array_strings_to_ints(self.state_a)
        self.state_b = continuous_array_strings_to_ints(self.state_b)


def generate_discrete_mcrules(gates, dim, rules_classes="all", generators="std"):
    """
    Yields discrete Markov chain rules.

    **Arguments**

    gates : set
        The set of gates involved in the transformation rules.
    dim : int
        Number of dimensions of the qubits lattice.
    rules_classes : "all" or list of ints, optional
        A list of the ints identifying the rule classes that we want to generate.
        Default is "all" and generates all the rule classes.
    generators : "std" or list of generators, optional
        The list of generators producing the rules to be used. Default is "std",
        in this case a standard list of rules is used.
    """
    for discrete_abstract_rule in generate_discrete_abstract_rules(
        gates, dim, rules_classes=rules_classes, verify=False, generators=generators
    ):
        yield DiscreteMCRule(discrete_abstract_rule)


def generate_continuous_mcrules(gates, dim, rules_classes="all", generators="std"):
    """
    Yields continuous Markov chain rules.

    **Arguments**

    gates : set
        The set of gates involved in the transformation rules.
    dim : int
        Number of dimensions of the qubits lattice.
    rules_classes : "all" or list of ints, optional
        A list of the ints identifying the rule classes that we want to generate.
        Default is "all" and generates all the rule classes.
    generators : "std" or list of generators, optional
        The list of generators producing the rules to be used. Default is "std",
        in this case a standard list of rules is used.
    """
    for continuous_abstract_rule in generate_continuous_abstract_rules(
        gates, dim, rules_classes=rules_classes, verify=False, generators=generators
    ):
        yield ContinuousMCRule(continuous_abstract_rule)
