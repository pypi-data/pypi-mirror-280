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
Define and generate abstract transformation rules linking equivalent subcircuits
that involve continous gates.

Note that, differently from discrete rules, the inverse of a continuous rule is
defined separately.

A rule is described by a list -> state_a, state_b, amplitudes_condition,
rot_transformation_func, test_rot_amplitudes.

    - state_a and state_b is couple of equivalent subcircuits as in abstractdiscreterules.
    - amplitudes_condition is a function that check the parameters of the gates
    in the input circuit, if the rule can be applied returns True.
    - rot_transformation_func returns the transformed parameters after the transition.
    - test_rot_amplitudes is a numpy np.array of parameters used to completely specify
    an input circuit to test the validity of the rule.
"""

import copy
from math import pi as PI
import numpy as np
from scipy.spatial.transform import Rotation as R
from vulqano.states import AbstractCircuitState
from vulqano.utils import (
    check_circuit_equivalence,
)
from vulqano.gates.continuousgates import GATES_DICTIONARY
from vulqano.rules.standardcontinuousrules import (
    STD_CONTINUOUS_RULES_GENERATORS,
)

__all__ = [
    "ContinuousTransformationRule",
    "generate_continuous_abstract_rules",
]


PERIOD = 2 * PI  # THE PERIODICITY OF RX, RZ (UP TO A GLOBAL PHASE) AND CP IS 2PI.

ROT_EXCANGE_QUANTA = [
    PI,
    PI / 2,
    -PI / 2,
    PI / 4,
    -PI / 4,
    PI / 8,
    -PI / 8,
]  # Simmetric for invertible rules.


def euler_zxz_to_xzx(rot_amplitudes_array):
    """
    Convert Euler angles (a,b,c) corresponding to the axis system axis ZXZ to
    Euler angles (a',b',c') corresponding to the axis system axis XZX, such that

                  Rz(a)Rx(b)Rz(c) = Rx(a')Rz(b')Rx(c')

    Parameters
    ----------
    rot_amplitudes_array : np.array
        Euler angles (a,b,c) corresponding to the axis system axis ZXZ.

    Returns
    -------
    np.array
        Euler angles (a',b',c') corresponding to the axis system axis XZX

    """
    return (
        np.reshape(
            R.from_euler("zxz", rot_amplitudes_array.flat).as_euler("xzx"),
            rot_amplitudes_array.shape,
        )
        % PERIOD
    )


def euler_xzx_to_zxz(rot_amplitudes_array):
    """
    Convert Euler angles (a,b,c) corresponding to the axis system axis XZX to
    Euler angles (a',b',c') corresponding to the axis system axis ZXZ, such that

                  Rx(a)Rz(b)Rx(c) = Rz(a')Rx(b')Rz(c')

    Parameters
    ----------
    rot_amplitudes_array : np.array
        Euler angles (a,b,c) corresponding to the axis system axis XZX.

    Returns
    -------
    np.array
        Euler angles (a',b',c') corresponding to the axis system axis ZXZ
    """
    return (
        np.reshape(
            R.from_euler("xzx", rot_amplitudes_array.flat).as_euler("zxz"),
            rot_amplitudes_array.shape,
        )
        % PERIOD
    )


class ContinuousTransformationRule:
    """
    Abstract continuous transformation rules linking equivalent subcircuits.

    **Arguments**

    state_a : np.array of strings
        Array representing the first subcircuit gates.
    state_b : np.array of strings
        Array representing the second subcircuit gates.
    class_index : int
        Rules are grouped in classes, class_index labels the class of the rule.
    amplitudes_condition : np_array -> bool
        True if the rule can be applied.
    rot_transformation_func : np_array -> np.array
        A function for transforming rotation amplitudes.
    test_rot_amplitudes : np.array
        test_rot_amplitudes is a numpy np.array of parameters used to completely
        specify an input circuit to test the validity of the rule.
    verify : bool
        If true, the rule is checked. Default is False.

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

    def __init__(
        self,
        state_a,
        state_b,
        class_index,
        amplitudes_condition,
        rot_transformation_func,
        test_rot_amplitudes,
        verify=False,
    ):
        self.state_a = state_a
        self.state_b = state_b
        self.class_index = class_index
        self.amplitudes_condition = amplitudes_condition
        self.rot_transformation_func = rot_transformation_func
        self.test_rot_amplitudes = np.array(test_rot_amplitudes, dtype=float)
        self.shape = self.state_a.shape
        self.any_mask = np.equal(
            self.state_a, np.full(self.state_a.shape, "any", dtype=object)
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
                    "INVALID RULE: the circuits\n" + str(self) + "\nare not equivalent."
                )

    def __str__(self):
        """
        Generates a pictorial representation of the transformation rule.

        **Returns**

         : str
            A pictorial representation of the transformation rule.
        """
        return (
            str(self.state_a)
            + "\n<====>\n"
            + str(self.state_b)
            + "\n\n"
            + str(self.test_rot_amplitudes)
            + "\n<====>\n"
            + str(self.rot_transformation_func(self.test_rot_amplitudes))
        )

    def verify(self):
        """
        Verify the equivalence between the subcircuits linked by the rule.

        **Returns**

        check_result : bool
            True if the rule is valid (equivalent subcircuit).
        """
        rot_amplitudes_in = self.test_rot_amplitudes
        if not self.amplitudes_condition(rot_amplitudes_in):
            raise ValueError(
                "RULE: the circuits\n"
                + str(self)
                + "\ncan not be tested with these rotation amplitudes."
            )

        rot_amplitudes_out = self.rot_transformation_func(np.copy(rot_amplitudes_in))
        for idx, gate in np.ndenumerate(self.state_b):
            if not GATES_DICTIONARY[gate]["is_parametric"]:
                if rot_amplitudes_out[idx] != 0:
                    raise ValueError(
                        "The rule\n"
                        + str(self)
                        + "\n associates a non zero parameter to a non-parametric gate."
                    )

        first_circuit_vector = copy.deepcopy(self.state_a)
        second_circuit_vector = copy.deepcopy(self.state_b)

        gates_replacements = ["RX", "RZ", "RX", "RZ", "RX", "RZ", "RX", "RZ"]
        amplitudes_replacements = [1, 2, 3, 1, 2, 3, 1, 2]

        counter = 0
        for idx, is_any in np.ndenumerate(self.any_mask):
            if is_any:
                first_circuit_vector[idx] = gates_replacements[counter]
                second_circuit_vector[idx] = gates_replacements[counter]
                rot_amplitudes_in[idx] = amplitudes_replacements[counter]
                rot_amplitudes_out[idx] = amplitudes_replacements[counter]
                counter += 1

        input_circuit = AbstractCircuitState(
            first_circuit_vector, "c0", rot_amplitudes_array=rot_amplitudes_in
        )
        output_circuit = AbstractCircuitState(
            second_circuit_vector, "c1", rot_amplitudes_array=rot_amplitudes_out
        )
        check_result = check_circuit_equivalence(input_circuit, output_circuit)

        return check_result


def rotate_state(state_vector, rot_amplitudes=None):
    """
    Rotate a state:  [A, B, C] -> [[A, B, C]] and replaces eventual two-qubits
    gates with their rotated form.


    **Arguments**


    state_vector : np.array
        State to be rotated (GATES description)
    rot_amplitudes : np.array or None, optional.
        State to be rotated (parameters description). Default is None.

    **Returns**

    state_vector : np.array
        Rotated state (GATES description)
    rot_amplitudes : np.array or None
        Rotated state (parameters description)

    """
    state_vector = np.transpose(state_vector, (0, 2, 1))
    for idx, gate in np.ndenumerate(state_vector):
        if GATES_DICTIONARY[gate]["Connectivity"] == [1]:
            state_vector[idx] += "_r"
    if rot_amplitudes is not None:
        rot_amplitudes = np.transpose(rot_amplitudes, (0, 2, 1))
    return (state_vector, rot_amplitudes)


def generate_continuous_abstract_rules(
    gates, dim, rules_classes="all", verify=False, generators="std"
):
    """
    Returns a list of continuous transformation rules.

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

    if generators == "std":
        generators = STD_CONTINUOUS_RULES_GENERATORS

    rules = []
    if rules_classes == "all":
        rules_classes = list(range(len(generators)))

    if set(rules_classes).issubset(set(range(len(generators)))) is not True:
        raise ValueError(
            "rules_classes must be a list of int from 0 to "
            + str(len(generators))
            + ' or "all".'
        )

    for class_index in rules_classes:
        for rule in generators[class_index]():
            state_a = np.array(rule[0], dtype=object)
            state_b = np.array(rule[1], dtype=object)
            test_rot_amplitudes = np.array(rule[4])
            if len(state_a.shape) == dim:
                abstract_rule = ContinuousTransformationRule(
                    np.copy(state_a),
                    np.copy(state_b),
                    class_index,
                    rule[2],
                    rule[3],
                    test_rot_amplitudes,
                    verify=verify,
                )
                if abstract_rule.involved_gates.issubset(gates_extended):
                    rules.append(abstract_rule)

            if len(state_a.shape) == 2 and dim == 3:
                # [A, B, C] -> [[A, B, C]]
                state_a = np.expand_dims(state_a, 1)
                state_b = np.expand_dims(state_b, 1)
                test_rot_amplitudes = np.expand_dims(test_rot_amplitudes, 1)
                abstract_rule = ContinuousTransformationRule(
                    np.copy(state_a),
                    np.copy(state_b),
                    class_index,
                    rule[2],
                    rule[3],
                    np.copy(test_rot_amplitudes),
                    verify=verify,
                )
                if abstract_rule.involved_gates.issubset(gates_extended):
                    rules.append(abstract_rule)

                if state_a.shape[-1] > 1:
                    # [[A, B, C]] -> [[A], [B], [C]]
                    state_a, test_rot_amplitudes = rotate_state(
                        state_a, test_rot_amplitudes
                    )
                    state_b, _ = rotate_state(state_b)
                    abstract_rule = ContinuousTransformationRule(
                        np.copy(state_a),
                        np.copy(state_b),
                        class_index,
                        rule[2],
                        rule[3],
                        np.copy(test_rot_amplitudes),
                        verify=verify,
                    )
                    if abstract_rule.involved_gates.issubset(gates_extended):
                        rules.append(abstract_rule)
    return rules


def unit_test_2d():
    """
    Unit test to check if all the 2d rules are valid.

    **Returns**

       : bool
    True if all the rules are valid.

    """
    generate_continuous_abstract_rules(
        {
            "RX",
            "RZ",
            "CP",
            "SWAP",
        },
        2,
        verify=True,
    )
    return True


def unit_test_3d():
    """
    Unit test to check if all the 2d rules are valid.

    **Returns**

       : bool
    True if all the rules are valid.

    """
    generate_continuous_abstract_rules(
        {
            "RX",
            "RZ",
            "CP",
            "CP_r",
            "SWAP",
            "SWAP_r",
        },
        3,
        verify=True,
    )
    return True


if __name__ == "__main__":
    print(unit_test_2d())
    print(unit_test_3d())
