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
Collection of dictionaries for an abstract description of discrete gates.

Each key of GATES_DICTIONARY identifies the name of a gate. The corresponding
value is a dictionary that describes the gate as follows:
    Connectivity : tuple of ints
        A tuple indicating the vector from the control qubit to the target qubit
        in the lowest dimensional lattice in which the gate can be implemented.
        For 1 qubit gates is [].
    Qasm : lambda
       Returns a quasm string for the gate. None for fictitious gates.
    Color : lambda
        Returns an RGB tuple of three floats from 0 to 1 associated to the gate
        when plotting the circuit state.
    is_rot : bool
        If true, the gate represents a rotation Rz.
"""

import os
import numpy as np
from matplotlib import colors

__all__ = [
    "GATES_DICTIONARY",
    "ROT_GATES",
    "SQ_GATES",
    "ROT_SUMS",
    "R_MAX",
    "ROT_NUMBERS",
    "gate_labels_to_ints",
    "gate_ints_to_labels",
]

# Minimal z rotation angle is pi/(2**(R_MAX-2))
R_MAX = os.environ.get("R_MAX_VULQANO", 16)


# Gates definitions

GATES_DICTIONARY = {}

GATES_DICTIONARY["idle"] = {
    "Connectivity": [],
    "Qasm": None,
    "Color": lambda theta: colors.to_rgb("white"),
    "is_rot": True,
}

GATES_DICTIONARY["T"] = {
    "Connectivity": [],
    "Qasm": lambda theta, qubit, target_qubit: "t q[" + str(qubit) + "];\n",
    "Color": lambda theta: 1 - (1 - np.array(colors.to_rgb("dodgerblue"))) / 2,
    "is_rot": True,
}

GATES_DICTIONARY["Tdg"] = {
    "Connectivity": [],
    "Qasm": lambda theta, qubit, target_qubit: "tdg q[" + str(qubit) + "];\n",
    "Color": lambda theta: 1 - (1 - np.array(colors.to_rgb("purple"))) / 2,
    "is_rot": True,
}

GATES_DICTIONARY["S"] = {
    "Connectivity": [],
    "Qasm": lambda theta, qubit, target_qubit: "s q[" + str(qubit) + "];\n",
    "Color": lambda theta: colors.to_rgb("dodgerblue"),
    "is_rot": True,
}

GATES_DICTIONARY["Sdg"] = {
    "Connectivity": [],
    "Qasm": lambda theta, qubit, target_qubit: "sdg q[" + str(qubit) + "];\n",
    "Color": lambda theta: colors.to_rgb("purple"),
    "is_rot": True,
}

GATES_DICTIONARY["Z"] = {
    "Connectivity": [],
    "Qasm": lambda theta, qubit, target_qubit: "z q[" + str(qubit) + "];\n",
    "Color": lambda theta: colors.to_rgb("indigo"),
    "is_rot": True,
}

GATES_DICTIONARY["H"] = {
    "Connectivity": [],
    "Qasm": lambda theta, qubit, target_qubit: "h q[" + str(qubit) + "];\n",
    "Color": lambda theta: colors.to_rgb("gold"),
    "is_rot": False,
}

GATES_DICTIONARY["CZ"] = {
    "Connectivity": [1],
    "Qasm": lambda theta, qubit, target_qubit: "cz q["
    + str(qubit)
    + "], q["
    + str(target_qubit)
    + "];\n",
    "Color": lambda theta: colors.to_rgb("crimson"),
    "is_rot": False,
}


GATES_DICTIONARY["CZ_r"] = {
    "Connectivity": [1, 0],
    "Qasm": lambda theta, qubit, target_qubit: "cz q["
    + str(qubit)
    + "], q["
    + str(target_qubit)
    + "];\n",
    "Color": lambda theta: colors.to_rgb("magenta"),
    "is_rot": False,
}

GATES_DICTIONARY["SWAP"] = {
    "Connectivity": [1],
    "Qasm": lambda theta, qubit, target_qubit: "swap q["
    + str(qubit)
    + "], q["
    + str(target_qubit)
    + "];\n",
    "Color": lambda theta: colors.to_rgb("green"),
    "is_rot": False,
}

GATES_DICTIONARY["SWAP_r"] = {
    "Connectivity": [1, 0],
    "Qasm": lambda theta, qubit, target_qubit: "swap q["
    + str(qubit)
    + "], q["
    + str(target_qubit)
    + "];\n",
    "Color": lambda theta: colors.to_rgb("limegreen"),
    "is_rot": False,
}

GATES_DICTIONARY["busy"] = {
    "Connectivity": [],
    "Qasm": None,
    "Color": lambda theta: colors.to_rgb("grey"),
    "is_rot": False,
}


GATES_DICTIONARY["lock"] = {
    "Connectivity": [],
    "Qasm": None,
    "Color": lambda theta: colors.to_rgb("black"),
    "is_rot": False,
}

GATES_DICTIONARY["any"] = {
    "Connectivity": [],
    "Qasm": None,
    "Color": lambda theta: colors.to_rgb("black"),
    "is_rot": False,
}

GATES_DICTIONARY["any_rot"] = {
    "Connectivity": [],
    "Qasm": None,
    "Color": lambda theta: colors.to_rgb("black"),
    "is_rot": False,
}


for n in range(5, R_MAX + 1):
    GATES_DICTIONARY["RZ" + str(n)] = {
        "Connectivity": [],
        "Qasm": lambda theta, qubit, target_qubit, n=n: "rz(pi/"
        + str(2 ** (n - 2))
        + ") q["
        + str(qubit)
        + "];\n",
        "Color": lambda theta, n=n: 1
        - (1 - np.array(colors.to_rgb("dodgerblue"))) / (n - 2),
        "is_rot": True,
    }

    GATES_DICTIONARY["RZ" + str(n) + "dg"] = {
        "Connectivity": [],
        "Qasm": lambda theta, qubit, target_qubit, n=n: "rz(-pi/"
        + str(2 ** (n - 2))
        + ") q["
        + str(qubit)
        + "];\n",
        "Color": lambda theta, n=n: 1
        - (1 - np.array(colors.to_rgb("purple"))) / (n - 2),
        "is_rot": True,
    }


ROT_GATES = []
SQ_GATES = ["idle"]
for key, value in GATES_DICTIONARY.items():
    if value["is_rot"]:
        ROT_GATES.append(key)
    if (value["Connectivity"] == []) and (value["Qasm"] is not None):
        SQ_GATES.append(key)

ROT_SUMS = []
for nn in range(2, R_MAX + 1):
    if nn == 2:
        RN = "Z"
        RN_1 = "idle"
        RNDG = "Z"
        RN_1DG = "idle"
    elif nn == 3:
        RN = "S"
        RN_1 = "Z"
        RNDG = RN + "dg"
        RN_1DG = "Z"
    elif nn == 4:
        RN = "T"
        RN_1 = "S"
        RNDG = RN + "dg"
        RN_1DG = RN_1 + "dg"
    elif nn == 5:
        RN = "RZ5"
        RN_1 = "T"
        RNDG = RN + "dg"
        RN_1DG = RN_1 + "dg"
    else:
        RN = "RZ" + str(nn)
        RN_1 = "RZ" + str(nn - 1)
        RNDG = RN + "dg"
        RN_1DG = RN_1 + "dg"
    new_sums = (
        (RN, RN, RN_1, "idle"),
        (RN, RN, "idle", RN_1),
        (RNDG, RNDG, RN_1DG, "idle"),
        (RNDG, RNDG, "idle", RN_1DG),
        (RN, RNDG, "idle", "idle"),
        (RNDG, RN, "idle", "idle"),
    )
    for new_sum in new_sums:
        if new_sum not in ROT_SUMS:
            ROT_SUMS.append(new_sum)
ROT_SUMS = tuple(ROT_SUMS)

GATES_TO_LABELS = {}
LABELS_TO_GATES = {}
for gate_number, gate_name in enumerate(GATES_DICTIONARY.keys()):
    GATES_TO_LABELS[gate_name] = gate_number
    LABELS_TO_GATES[gate_number] = gate_name

ROT_NUMBERS = [GATES_TO_LABELS[k] for k in ROT_GATES]


def gate_labels_to_ints(strings_array):
    """
    Transforms the strings representation of a subcyrcuit to an ints representation,
    the translation is based on GATES_TO_LABELS.

    **Arguments**

    strings_array : np.array of strings
        Strings representation of a subcyrcuit

    **Returns**

    ints_array : : np.array of ints
        Ints representation of a subcyrcuit
    """

    ints_array = np.vectorize(GATES_TO_LABELS.get, otypes=[np.uint8])(strings_array)
    return ints_array


def gate_ints_to_labels(ints_array):
    """
    Transforms the int representation of a subcyrcuit to an strings representation,
    the translation is based on LABELS_TO_GATES.

    **Arguments**

    ints_array : : np.array of ints
        Ints representation of a subcyrcuit

    **Returns**

    strings_array : np.array of strings
        Strings representation of a subcyrcuit
    """
    strings_array = np.vectorize(LABELS_TO_GATES.get)(ints_array)
    return strings_array
