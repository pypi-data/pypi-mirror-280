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
Collection of dictionaries for an abstract description of continuous (parametric) gates.

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
    is_parametric : bool
        True for parametric gates.


NOTE : parametric gates with perdiodicity T are represented with parameter in [0, T)

"""

import math
import numpy as np
import matplotlib
from matplotlib import colors

__all__ = [
    "GATES_DICTIONARY",
    "gate_labels_to_ints",
    "gate_ints_to_labels",
    "SQ_GATES",
]


# Gates definitions

GATES_DICTIONARY = {}

color_rescaling = (
    lambda value: 0.25 + 1.5 * value if value < 0.5 else 1.75 - 1.5 * value
)

GATES_DICTIONARY["idle"] = {
    "Connectivity": [],
    "Qasm": None,
    "Color": lambda theta: colors.to_rgb("white"),
    "is_parametric": False,
}

GATES_DICTIONARY["RZ"] = {
    "Connectivity": [],
    "Qasm": lambda theta, qubit, target_qubit: "rz("
    + str(theta)
    + ") q["
    + str(qubit)
    + "];\n",
    "Color": lambda theta: matplotlib.cm.get_cmap("Purples")(
        color_rescaling(theta / (2 * math.pi))
    )[:3],
    "is_parametric": True,
}

GATES_DICTIONARY["RX"] = {
    "Connectivity": [],
    "Qasm": lambda theta, qubit, target_qubit: "rx("
    + str(theta)
    + ") q["
    + str(qubit)
    + "];\n",
    "Color": lambda theta: matplotlib.cm.get_cmap("Blues")(
        color_rescaling(theta / (2 * math.pi))
    )[:3],
    "is_parametric": True,
}


GATES_DICTIONARY["CP"] = {
    "Connectivity": [1],
    "Qasm": lambda theta, qubit, target_qubit: "cp("
    + str(theta)
    + ") q["
    + str(qubit)
    + "], q["
    + str(target_qubit)
    + "];\n",
    "Color": lambda theta: matplotlib.cm.get_cmap("Oranges")(
        color_rescaling(theta / (2 * math.pi))
    )[:3],
    "is_parametric": True,
}

GATES_DICTIONARY["CP_r"] = {
    "Connectivity": [1, 0],
    "Qasm": lambda theta, qubit, target_qubit: "cp("
    + str(theta)
    + ") q["
    + str(qubit)
    + "], q["
    + str(target_qubit)
    + "];\n",
    "Color": lambda theta: matplotlib.cm.get_cmap("Reds")(
        color_rescaling(theta / (2 * math.pi))
    )[:3],
    "is_parametric": True,
}

GATES_DICTIONARY["SWAP"] = {
    "Connectivity": [1],
    "Qasm": lambda theta, qubit, target_qubit: "swap q["
    + str(qubit)
    + "], q["
    + str(target_qubit)
    + "];\n",
    "Color": lambda theta: colors.to_rgb("green"),
    "is_parametric": False,
}

GATES_DICTIONARY["SWAP_r"] = {
    "Connectivity": [1, 0],
    "Qasm": lambda theta, qubit, target_qubit: "swap q["
    + str(qubit)
    + "], q["
    + str(target_qubit)
    + "];\n",
    "Color": lambda theta: colors.to_rgb("limegreen"),
    "is_parametric": False,
}

GATES_DICTIONARY["busy"] = {
    "Connectivity": [],
    "Qasm": None,
    "Color": lambda theta: colors.to_rgb("grey"),
    "is_parametric": False,
}


GATES_DICTIONARY["lock"] = {
    "Connectivity": [],
    "Qasm": None,
    "Color": lambda theta: colors.to_rgb("black"),
    "is_parametric": False,
}

GATES_DICTIONARY["any"] = {
    "Connectivity": [],
    "Qasm": None,
    "Color": lambda theta: colors.to_rgb("black"),
    "is_parametric": False,
}


GATES_TO_LABELS = {}
LABELS_TO_GATES = {}
for gate_number, gate_name in enumerate(GATES_DICTIONARY.keys()):
    GATES_TO_LABELS[gate_name] = gate_number
    LABELS_TO_GATES[gate_number] = gate_name


SQ_GATES = ["idle"]
for key, value in GATES_DICTIONARY.items():
    if (value["Connectivity"] == []) and (value["Qasm"] is not None):
        SQ_GATES.append(key)


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
