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
Build the matrix representation of quadratic operators g_i^dag g_j for each gate,
where g_i is an annihilation operator.
"""


from collections import OrderedDict
from itertools import product
import numpy as np
import qtealeaves as qtl
from vulqano.gates.discretegates import ROT_GATES


__all__ = [
    "build_annihil_op",
    "TNGateOperators",
    "TNTimeStepOperators",
]


def build_annihil_op(index, local_dim):
    """
    Build the matrix representation of the annihilation operator for the gate
    labeled by the index.

    **Arguments**

    index : int
        Boson favour label
    local_dim : int
        DImension of the local Hilber space

    **Returns**

    tmp : np.array
        Matrix representation of the annihiling operator.

    """
    tmp = np.zeros((local_dim, local_dim))
    tmp[0, index] = 1
    return tmp


class TNGateOperators(qtl.operators.TNOperators):
    """
    Class for the definition of a set of local gate operators g_i^dag g_j.

    **Arguments**

    gates : list of str
        The list of gates involved in the circuit, included the identity.
        Idenity has to be the first gate.
    folder_operators : str, optional
        DESCRIPTION. The default is "TNGateOperators".
    """

    def __init__(
        self,
        gates,
        folder_operators="TNGateOperators",
    ):
        if gates[0] != "idle":
            raise ValueError("The first gate must be the identity")
        gates += ["busy"]

        self.folder_operators = folder_operators
        self.local_dim = len(gates)

        annihilators = {}
        for ii, gate in enumerate(gates):
            annihilators[gate] = build_annihil_op(ii, self.local_dim)

        self.ops = OrderedDict()
        self.ops["id"] = np.eye(self.local_dim)

        gates_couples = product(gates, gates)

        for gate1, gate2 in gates_couples:
            self.ops[gate1 + "->" + gate2] = (
                annihilators[gate2].conj().T.dot(annihilators[gate1])
            )

        self.ops["any->any"] = sum(self.ops[gate + "->" + gate] for gate in gates)

        self.ops["any_rot->any_rot"] = sum(
            self.ops[gate + "->" + gate]
            for gate in set(ROT_GATES).intersection(set(gates))
        )


class TNTimeStepOperators(qtl.operators.TNOperators):
    """
    Class for the definition of a set of time step configuration transitions of the
    form g_i^dag g_j.

    **Arguments**

    time_step_configurations : list of str
        List of possible time-step configurations to be represented as
        states in a local Hilbert space.
        Each time step configuration is represented by a string like "g1|...|gn".
    time_step_transformations : list of str
        The list of transformations between time steps to be encoded as operators.
        Each transformation is represented by a string like "g1|...|gn->g'1|...|g'n".
    folder_operators : str, optional
        Folder where the operators are saved by qtealeaves. The default is "TNTimeStepOperators".
    """

    def __init__(
        self,
        time_step_configurations,
        time_step_transformations,
        folder_operators="TNTimeStepOperators",
    ):
        self.folder_operators = folder_operators
        self.local_dim = len(time_step_configurations)

        annihilators = {}
        for ii, config in enumerate(time_step_configurations):
            annihilators[config] = build_annihil_op(ii, self.local_dim)

        self.ops = OrderedDict()
        self.ops["id"] = np.eye(self.local_dim)

        for transformation in time_step_transformations:
            (configuration_in, configuration_out) = transformation.split("->")
            self.ops[transformation] = np.zeros((self.local_dim, self.local_dim))
            for new_configuration_in, new_configuration_out in self.expand_identities(
                time_step_configurations, configuration_in, configuration_out
            ):
                self.ops[transformation] += (
                    annihilators[new_configuration_in]
                    .conj()
                    .T.dot(annihilators[new_configuration_out])
                )

    @staticmethod
    def expand_identities(
        time_step_configurations, configuration_in, configuration_out
    ):
        """
        Given two terms of a transformation, if these terms contain the "any" gate,
        expand the terms over all the possible configurations of the time step
        that are compatible.

        **Arguments**

        time_step_configurations : list of strings
            List of possible time step configurations represented by strings like
            "g1|...|gn".
        configuration_in : string
            Input time step configuration represented by a string like "g1|...|gn".
        configuration_out : string
            Transformed time step configuration represented by a string like "g'1|...|g'n".

        **Yields**

        new_configuration_in : string
            Input time step configuration where each "any" gate has been replaced
            in a way such that the new configuration is in time_step_configurations.
        new_configuration_out : string
            Transformed time step configuration where each "any" gate has been replaced
            in a way such that the new configuration is in time_step_configurations.
        """
        splitted_configuration_in = configuration_in.split("|")
        splitted_configuration_out = configuration_out.split("|")
        if "any" in configuration_in:
            for possible_configuration in time_step_configurations:
                possible_configuration = possible_configuration.split("|")
                if all(
                    gate in ("any", possible_configuration[ii])
                    for ii, gate in enumerate(splitted_configuration_in)
                ):
                    new_configuration_in = [
                        gate if gate != "any" else possible_configuration[ii]
                        for ii, gate in enumerate(splitted_configuration_in)
                    ]
                    new_configuration_out = [
                        gate if gate != "any" else possible_configuration[ii]
                        for ii, gate in enumerate(splitted_configuration_out)
                    ]
                    yield "|".join(new_configuration_in), "|".join(
                        new_configuration_out
                    )
        else:
            yield configuration_in, configuration_out
