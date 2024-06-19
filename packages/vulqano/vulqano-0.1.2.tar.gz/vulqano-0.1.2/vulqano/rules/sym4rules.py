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
Special rules for transformations of a circuit with discrete gates CZ, H and SWAP,
acting on 4 qubits with reflection invariance over the qubits axis.
"""

__all__ = ["SYM_4_RULES_GENERATORS"]


def all_rules():
    """
    Yields all the transformation rules.
    """
    # H comm
    yield (
        [["H", "any", "any", "H"], ["idle", "any", "any", "idle"]],
        [["idle", "any", "any", "idle"], ["H", "any", "any", "H"]],
    )
    yield (
        [["any", "H", "H", "any"], ["any", "idle", "idle", "any"]],
        [["any", "idle", "idle", "any"], ["any", "H", "H", "any"]],
    )

    # H ann
    yield (
        [["H", "any", "any", "H"], ["H", "any", "any", "H"]],
        [["idle", "any", "any", "idle"], ["idle", "any", "any", "idle"]],
    )
    yield (
        [["any", "H", "H", "any"], ["any", "H", "H", "any"]],
        [["any", "idle", "idle", "any"], ["any", "idle", "idle", "any"]],
    )

    # CZ comm
    yield (
        [["any", "idle", "idle", "any"], ["any", "CZ", "busy", "any"]],
        [["any", "CZ", "busy", "any"], ["any", "idle", "idle", "any"]],
    )
    yield (
        [["CZ", "busy", "CZ", "busy"], ["idle", "idle", "idle", "idle"]],
        [["idle", "idle", "idle", "idle"], ["CZ", "busy", "CZ", "busy"]],
    )
    yield (
        [["CZ", "busy", "CZ", "busy"], ["idle", "CZ", "busy", "idle"]],
        [["idle", "CZ", "busy", "idle"], ["CZ", "busy", "CZ", "busy"]],
    )

    # CZ ann
    yield (
        [["any", "CZ", "busy", "any"], ["any", "CZ", "busy", "any"]],
        [["any", "idle", "idle", "any"], ["any", "idle", "idle", "any"]],
    )
    yield (
        [["CZ", "busy", "CZ", "busy"], ["CZ", "busy", "CZ", "busy"]],
        [["idle", "idle", "idle", "idle"], ["idle", "idle", "idle", "idle"]],
    )

    # SWAP comm
    yield (
        [["any", "idle", "idle", "any"], ["any", "SWAP", "busy", "any"]],
        [["any", "SWAP", "busy", "any"], ["any", "idle", "idle", "any"]],
    )
    yield (
        [["SWAP", "busy", "SWAP", "busy"], ["idle", "idle", "idle", "idle"]],
        [["idle", "idle", "idle", "idle"], ["SWAP", "busy", "SWAP", "busy"]],
    )

    # SWAP ann
    yield (
        [["any", "SWAP", "busy", "any"], ["any", "SWAP", "busy", "any"]],
        [["any", "idle", "idle", "any"], ["any", "idle", "idle", "any"]],
    )
    yield (
        [["SWAP", "busy", "SWAP", "busy"], ["SWAP", "busy", "SWAP", "busy"]],
        [["idle", "idle", "idle", "idle"], ["idle", "idle", "idle", "idle"]],
    )

    # CZ SWAP
    yield (
        [["any", "CZ", "busy", "any"], ["any", "SWAP", "busy", "any"]],
        [["any", "SWAP", "busy", "any"], ["any", "CZ", "busy", "any"]],
    )
    yield (
        [["SWAP", "busy", "SWAP", "busy"], ["CZ", "busy", "CZ", "busy"]],
        [["CZ", "busy", "CZ", "busy"], ["SWAP", "busy", "SWAP", "busy"]],
    )

    # SWAP H
    yield (
        [["any", "H", "H", "any"], ["any", "SWAP", "busy", "any"]],
        [["any", "SWAP", "busy", "any"], ["any", "H", "H", "any"]],
    )
    yield (
        [["SWAP", "busy", "SWAP", "busy"], ["idle", "H", "H", "idle"]],
        [["H", "idle", "idle", "H"], ["SWAP", "busy", "SWAP", "busy"]],
    )
    yield (
        [["SWAP", "busy", "SWAP", "busy"], ["H", "idle", "idle", "H"]],
        [["idle", "H", "H", "idle"], ["SWAP", "busy", "SWAP", "busy"]],
    )
    yield (
        [["SWAP", "busy", "SWAP", "busy"], ["H", "H", "H", "H"]],
        [["H", "H", "H", "H"], ["SWAP", "busy", "SWAP", "busy"]],
    )

    # CZ SWAP H
    yield (
        [
            ["CZ", "busy", "CZ", "busy"],
            ["H", "H", "H", "H"],
            ["CZ", "busy", "CZ", "busy"],
            ["H", "H", "H", "H"],
        ],
        [
            ["SWAP", "busy", "SWAP", "busy"],
            ["H", "H", "H", "H"],
            ["CZ", "busy", "CZ", "busy"],
            ["idle", "idle", "idle", "idle"],
        ],
    )
    yield (
        [
            ["H", "H", "H", "H"],
            ["CZ", "busy", "CZ", "busy"],
            ["H", "H", "H", "H"],
            ["CZ", "busy", "CZ", "busy"],
        ],
        [
            ["idle", "idle", "idle", "idle"],
            ["CZ", "busy", "CZ", "busy"],
            ["H", "H", "H", "H"],
            ["SWAP", "busy", "SWAP", "busy"],
        ],
    )
    yield (
        [
            ["any", "H", "H", "any"],
            ["any", "CZ", "busy", "any"],
            ["any", "H", "H", "any"],
            ["any", "CZ", "busy", "any"],
        ],
        [
            ["any", "idle", "idle", "any"],
            ["any", "CZ", "busy", "any"],
            ["any", "H", "H", "any"],
            ["any", "SWAP", "busy", "any"],
        ],
    )
    yield (
        [
            ["any", "CZ", "busy", "any"],
            ["any", "H", "H", "any"],
            ["any", "CZ", "busy", "any"],
            ["any", "H", "H", "any"],
        ],
        [
            ["any", "SWAP", "busy", "any"],
            ["any", "H", "H", "any"],
            ["any", "CZ", "busy", "any"],
            ["any", "idle", "idle", "any"],
        ],
    )


SYM_4_RULES_GENERATORS = [
    all_rules,
]
