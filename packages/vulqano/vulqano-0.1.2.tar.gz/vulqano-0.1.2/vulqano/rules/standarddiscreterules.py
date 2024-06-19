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
Define the generators for a set of standard rules involving non-parametric gates.
"""

from itertools import product
from vulqano.gates.discretegates import (
    ROT_GATES,
    SQ_GATES,
    ROT_SUMS,
)

__all__ = [
    "STD_DISCRETE_RULES_GENERATORS",
    "rz_rz_rules",
    "h_rules",
    "h_rz_rules",
    "cz_ann_rules",
    "rz_cz_rules",
    "rz_cz_h_rules",
    "swap_ann_rules",
    "swap_sqg_rules",
    "swap_cz_rules",
    "swap_cz_h_rules",
]


def rz_rz_rules():
    """
    Yields transformation rules between RZ gates
    """
    rot_gates = list(enumerate(ROT_GATES))
    for gate in product(rot_gates, rot_gates):
        if gate[0][0] < gate[1][0]:
            yield (
                [[gate[0][1]], [gate[1][1]]],
                [[gate[1][1]], [gate[0][1]]],
            )
    for rot_sum in ROT_SUMS:
        yield (
            [[rot_sum[0]], [rot_sum[1]]],
            [[rot_sum[2]], [rot_sum[3]]],
        )


def h_rules():
    """
    Yields transformation rules between H gates.
    """
    yield ([["idle"], ["H"]], [["H"], ["idle"]])
    yield ([["H"], ["H"]], [["idle"], ["idle"]])


def h_rz_rules():
    """
    Yields transformation rules between RZ and H gates.
    """
    # H S H = S H S
    yield (
        [["H"], ["S"], ["H"]],
        [["Sdg"], ["H"], ["Sdg"]],
    )
    yield (
        [["H"], ["Sdg"], ["H"]],
        [["S"], ["H"], ["S"]],
    )
    # H R H Z = Z H Rd H
    yield (
        [["H"], ["T"], ["H"], ["Z"]],
        [["Z"], ["H"], ["Tdg"], ["H"]],
    )
    yield (
        [["H"], ["Tdg"], ["H"], ["Z"]],
        [["Z"], ["H"], ["T"], ["H"]],
    )
    yield (
        [["H"], ["S"], ["H"], ["Z"]],
        [["Z"], ["H"], ["Sdg"], ["H"]],
    )
    yield (
        [["H"], ["Sdg"], ["H"], ["Z"]],
        [["Z"], ["H"], ["S"], ["H"]],
    )
    yield (
        [["H"], ["Z"], ["H"], ["Z"]],
        [["Z"], ["H"], ["Z"], ["H"]],
    )


def cz_ann_rules():
    """
    Yields transformation rules between CZ gates.
    """
    yield (
        [["CZ", "busy"], ["CZ", "busy"]],
        [["idle", "idle"], ["idle", "idle"]],
    )
    yield (
        [["CZ", "busy", "idle"], ["idle", "CZ", "busy"]],
        [["idle", "CZ", "busy"], ["CZ", "busy", "idle"]],
    )
    yield (
        [[["CZ", "busy"], ["any", "idle"]], [["idle", "CZ_r"], ["any", "busy"]]],
        [[["idle", "CZ_r"], ["any", "busy"]], [["CZ", "busy"], ["any", "idle"]]],
    )
    yield (
        [[["any", "CZ_r"], ["idle", "busy"]], [["any", "idle"], ["CZ", "busy"]]],
        [[["any", "idle"], ["CZ", "busy"]], [["any", "CZ_r"], ["idle", "busy"]]],
    )
    yield (
        [[["idle", "any"], ["CZ", "busy"]], [["CZ_r", "any"], ["busy", "idle"]]],
        [[["CZ_r", "any"], ["busy", "idle"]], [["idle", "any"], ["CZ", "busy"]]],
    )
    yield (
        [[["CZ_r", "idle"], ["busy", "any"]], [["CZ", "busy"], ["idle", "any"]]],
        [[["CZ", "busy"], ["idle", "any"]], [["CZ_r", "idle"], ["busy", "any"]]],
    )


def rz_cz_rules():
    """
    Yields transformation rules between RZ and CZ gates.
    """
    for gate in product(ROT_GATES, ROT_GATES):
        yield (
            [["CZ", "busy"], [gate[0], gate[1]]],
            [[gate[0], gate[1]], ["CZ", "busy"]],
        )
    rot_gates = list(enumerate(ROT_GATES))
    for gate in product(rot_gates, rot_gates):
        if gate[0][0] < gate[1][0]:
            yield (
                [[gate[0][1], "any"], ["CZ", "busy"], [gate[1][1], "any"]],
                [[gate[1][1], "any"], ["CZ", "busy"], [gate[0][1], "any"]],
            )
            yield (
                [["any", gate[0][1]], ["CZ", "busy"], ["any", gate[1][1]]],
                [["any", gate[1][1]], ["CZ", "busy"], ["any", gate[0][1]]],
            )
    for rot_sum in ROT_SUMS:
        yield (
            [[rot_sum[0], "any"], ["CZ", "busy"], [rot_sum[1], "any"]],
            [[rot_sum[2], "any"], ["CZ", "busy"], [rot_sum[3], "any"]],
        )
        yield (
            [["any", rot_sum[0]], ["CZ", "busy"], ["any", rot_sum[1]]],
            [["any", rot_sum[2]], ["CZ", "busy"], ["any", rot_sum[3]]],
        )


def rz_cz_h_rules():
    """
    Yields transformation rules between RZ, CZ and H gates.
    """
    rot_gates = list(enumerate(ROT_GATES))
    for gate in product(rot_gates, rot_gates):
        if gate[0][0] < gate[1][0]:
            yield (
                [
                    ["any", gate[0][1]],
                    ["any", "H"],
                    ["CZ", "busy"],
                    ["any_rot", "H"],
                    ["any_rot", "any_rot"],
                    ["any_rot", "H"],
                    ["CZ", "busy"],
                    ["any", "H"],
                    ["any", gate[1][1]],
                ],
                [
                    ["any", gate[1][1]],
                    ["any", "H"],
                    ["CZ", "busy"],
                    ["any_rot", "H"],
                    ["any_rot", "any_rot"],
                    ["any_rot", "H"],
                    ["CZ", "busy"],
                    ["any", "H"],
                    ["any", gate[0][1]],
                ],
            )
            yield (
                [
                    [gate[0][1], "any"],
                    ["H", "any"],
                    ["CZ", "busy"],
                    ["H", "any_rot"],
                    ["any_rot", "any_rot"],
                    ["H", "any_rot"],
                    ["CZ", "busy"],
                    ["H", "any"],
                    [gate[1][1], "any"],
                ],
                [
                    [gate[1][1], "any"],
                    ["H", "any"],
                    ["CZ", "busy"],
                    ["H", "any_rot"],
                    ["any_rot", "any_rot"],
                    ["H", "any_rot"],
                    ["CZ", "busy"],
                    ["H", "any"],
                    [gate[0][1], "any"],
                ],
            )
    for rot_sum in ROT_SUMS:
        yield (
            [
                ["any", rot_sum[0]],
                ["any", "H"],
                ["CZ", "busy"],
                ["any_rot", "H"],
                ["any_rot", "any_rot"],
                ["any_rot", "H"],
                ["CZ", "busy"],
                ["any", "H"],
                ["any", rot_sum[1]],
            ],
            [
                ["any", rot_sum[2]],
                ["any", "H"],
                ["CZ", "busy"],
                ["any_rot", "H"],
                ["any_rot", "any_rot"],
                ["any_rot", "H"],
                ["CZ", "busy"],
                ["any", "H"],
                ["any", rot_sum[3]],
            ],
        )
        yield (
            [
                [rot_sum[0], "any"],
                ["H", "any"],
                ["CZ", "busy"],
                ["H", "any_rot"],
                ["any_rot", "any_rot"],
                ["H", "any_rot"],
                ["CZ", "busy"],
                ["H", "any"],
                [rot_sum[1], "any"],
            ],
            [
                [rot_sum[2], "any"],
                ["H", "any"],
                ["CZ", "busy"],
                ["H", "any_rot"],
                ["any_rot", "any_rot"],
                ["H", "any_rot"],
                ["CZ", "busy"],
                ["H", "any"],
                [rot_sum[3], "any"],
            ],
        )


def swap_ann_rules():
    """
    Yields transformation rules between SWAP gates.
    """
    yield (
        [["SWAP", "busy"], ["SWAP", "busy"]],
        [["idle", "idle"], ["idle", "idle"]],
    )
    yield (
        [["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"]],
        [["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"]],
    )

    yield (
        [
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
        ],
        [
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
        ],
    )

    yield (
        [
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
        ],
        [
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
        ],
    )

    yield (
        [
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
        ],
        [
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
        ],
    )

    yield (
        [
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
        ],
        [
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
        ],
    )


def swap_sqg_rules():
    """
    Yields transformation rules between SEAP and single qubit gates.
    """
    for gate in product(SQ_GATES, SQ_GATES):
        yield (
            [["SWAP", "busy"], [gate[0], gate[1]]],
            [[gate[1], gate[0]], ["SWAP", "busy"]],
        )


def swap_cz_rules():
    """
    Yields transformation rules between CZ and SWAP gates.
    """
    yield (
        [["CZ", "busy"], ["SWAP", "busy"]],
        [["SWAP", "busy"], ["CZ", "busy"]],
    )
    yield (
        [["CZ", "busy", "idle"], ["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"]],
        [["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"], ["idle", "CZ", "busy"]],
    )

    yield (
        [
            [["CZ", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
        ],
        [
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "CZ_r"], ["any", "busy"]],
        ],
    )

    yield (
        [
            [["any", "CZ_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
        ],
        [
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["CZ", "busy"]],
        ],
    )

    yield (
        [
            [["idle", "any"], ["CZ", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
        ],
        [
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
            [["CZ_r", "any"], ["busy", "idle"]],
        ],
    )

    yield (
        [
            [["CZ_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
        ],
        [
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["CZ", "busy"], ["idle", "any"]],
        ],
    )

    yield (
        [["idle", "CZ", "busy"], ["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"]],
        [["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"], ["CZ", "busy", "idle"]],
    )

    yield (
        [
            [["idle", "CZ_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
        ],
        [
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["CZ", "busy"], ["any", "idle"]],
        ],
    )

    yield (
        [
            [["any", "idle"], ["CZ", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
        ],
        [
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "CZ_r"], ["idle", "busy"]],
        ],
    )

    yield (
        [
            [["CZ_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
        ],
        [
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["CZ", "busy"]],
        ],
    )

    yield (
        [
            [["CZ", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
        ],
        [
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
            [["CZ_r", "idle"], ["busy", "any"]],
        ],
    )


def swap_cz_h_rules():
    """
    Yields transformation rules between CZ and H gates.
    """
    yield (
        [["CZ", "busy"], ["H", "H"], ["CZ", "busy"], ["H", "H"]],
        [["SWAP", "busy"], ["H", "H"], ["CZ", "busy"], ["idle", "idle"]],
    )
    yield (
        [["H", "H"], ["CZ", "busy"], ["H", "H"], ["CZ", "busy"]],
        [["idle", "idle"], ["CZ", "busy"], ["H", "H"], ["SWAP", "busy"]],
    )


STD_DISCRETE_RULES_GENERATORS = [
    rz_rz_rules,
    h_rules,
    h_rz_rules,
    cz_ann_rules,
    rz_cz_rules,
    rz_cz_h_rules,
    swap_ann_rules,
    swap_sqg_rules,
    swap_cz_rules,
    swap_cz_h_rules,
]
