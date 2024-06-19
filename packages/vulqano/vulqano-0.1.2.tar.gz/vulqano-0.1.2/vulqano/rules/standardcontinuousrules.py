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
Define the generators for a set of standard rules involving parametric gates.
"""

from math import pi as PI
from itertools import product
import numpy as np
from scipy.spatial.transform import Rotation as R
from vulqano.gates.continuousgates import SQ_GATES


__all__ = [
    "STD_CONTINUOUS_RULES_GENERATORS",
    "rz_rules",
    "rx_rules",
    "rz_rx_rules",
    "cp_rules",
    "r_cp_rules",
    "swap_ann_rules",
    "swap_sqg_rules",
    "swap_cp_rules",
    "r_cp_swap_rules",
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


def rz_rules():
    """
    Yields transformation rules between RZ gates.
    """

    yield (
        [["RZ"]],
        [["idle"]],
        lambda rot_amplitudes_array: rot_amplitudes_array.flat[0] == 0,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0]],
    )

    yield (
        [["idle"]],
        [["RZ"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0]],
    )

    yield (
        [["idle"], ["RZ"]],
        [["RZ"], ["idle"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0], [0.5]],
    )

    yield (
        [["RZ"], ["idle"]],
        [["idle"], ["RZ"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0.5], [0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array *= 0
        return rot_amplitudes_array

    yield (
        [["RZ"], ["RZ"]],
        [["idle"], ["idle"]],
        lambda rot_amplitudes_array: np.all(rot_amplitudes_array == PI),
        rot_amplitudes_transform,
        [[PI], [PI]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = PI
        rot_amplitudes_array.flat[1] = PI
        return rot_amplitudes_array

    yield (
        [["idle"], ["idle"]],
        [["RZ"], ["RZ"]],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[0], [0]],
    )

    yield (
        [["RZ"], ["RZ"]],
        [["RZ"], ["RZ"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0.7], [0.2]],
    )

    for rot_unit in ROT_EXCANGE_QUANTA:

        def rot_amplitudes_transform(rot_amplitudes_array):
            rot_amplitudes_array.flat[0] += rot_unit
            rot_amplitudes_array.flat[1] -= rot_unit
            rot_amplitudes_array %= PERIOD
            return rot_amplitudes_array

        yield (
            [["RZ"], ["RZ"]],
            [["RZ"], ["RZ"]],
            lambda rot_amplitudes_array: True,
            rot_amplitudes_transform,
            [[0.7], [0.2]],
        )


def rx_rules():
    """
    Yields transformation rules between RX gates.
    """

    yield (
        [["RX"]],
        [["idle"]],
        lambda rot_amplitudes_array: rot_amplitudes_array.flat[0] == 0,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0]],
    )

    yield (
        [["idle"]],
        [["RX"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0]],
    )

    yield (
        [["idle"], ["RX"]],
        [["RX"], ["idle"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0], [0.5]],
    )

    yield (
        [["RX"], ["idle"]],
        [["idle"], ["RX"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0.5], [0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array *= 0
        return rot_amplitudes_array

    yield (
        [["RX"], ["RX"]],
        [["idle"], ["idle"]],
        lambda rot_amplitudes_array: np.all(rot_amplitudes_array == PI),
        rot_amplitudes_transform,
        [[PI], [PI]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = PI
        rot_amplitudes_array.flat[1] = PI
        return rot_amplitudes_array

    yield (
        [["idle"], ["idle"]],
        [["RX"], ["RX"]],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[0], [0]],
    )

    yield (
        [["RX"], ["RX"]],
        [["RX"], ["RX"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0.7], [0.2]],
    )

    for rot_unit in ROT_EXCANGE_QUANTA:

        def rot_amplitudes_transform(rot_amplitudes_array):
            rot_amplitudes_array.flat[0] += rot_unit
            rot_amplitudes_array.flat[1] -= rot_unit
            rot_amplitudes_array %= PERIOD
            return rot_amplitudes_array

        yield (
            [["RX"], ["RX"]],
            [["RX"], ["RX"]],
            lambda rot_amplitudes_array: True,
            rot_amplitudes_transform,
            [[0.7], [0.2]],
        )


def rz_rx_rules():
    """
    Yields transformation rules between RX and RZ gates.
    """

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array = np.flip(-rot_amplitudes_array, 0)
        rot_amplitudes_array %= PERIOD
        return rot_amplitudes_array

    yield (
        [["RX"], ["RZ"]],
        [["RZ"], ["RX"]],
        lambda rot_amplitudes_array: np.any(rot_amplitudes_array == PI),
        rot_amplitudes_transform,
        [[0.2], [PI]],
    )

    yield (
        [["RZ"], ["RX"]],
        [["RX"], ["RZ"]],
        lambda rot_amplitudes_array: np.any(rot_amplitudes_array == PI),
        rot_amplitudes_transform,
        [[0.3], [PI]],
    )

    yield (
        [["RX"], ["RZ"], ["RX"]],
        [["RZ"], ["RX"], ["RZ"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: euler_xzx_to_zxz(rot_amplitudes_array),
        [[0.2], [0.4], [0.6]],
    )

    yield (
        [["RZ"], ["RX"], ["RZ"]],
        [["RX"], ["RZ"], ["RX"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: euler_zxz_to_xzx(rot_amplitudes_array),
        [[0.2], [0.4], [0.6]],
    )


def cp_rules():
    """
    Yields transformation rules between CP gates.
    """

    yield (
        [["CP", "busy"]],
        [["idle", "idle"]],
        lambda rot_amplitudes_array: rot_amplitudes_array.flat[0] == 0,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0, 0]],
    )

    yield (
        [["idle", "idle"]],
        [["CP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0, 0]],
    )

    yield (
        [["CP", "busy"], ["idle", "idle"]],
        [["idle", "idle"], ["CP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0, 0], [0, 0]],
    )

    yield (
        [["idle", "idle"], ["CP", "busy"]],
        [["CP", "busy"], ["idle", "idle"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0, 0], [0, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = 0
        rot_amplitudes_array.flat[2] = 0
        return rot_amplitudes_array

    yield (
        [["CP", "busy"], ["CP", "busy"]],
        [["idle", "idle"], ["idle", "idle"]],
        lambda rot_amplitudes_array: rot_amplitudes_array.flat[0] == PI
        and rot_amplitudes_array.flat[2] == PI,
        rot_amplitudes_transform,
        [[PI, 0], [PI, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = PI
        rot_amplitudes_array.flat[2] = PI
        return rot_amplitudes_array

    yield (
        [["idle", "idle"], ["idle", "idle"]],
        [["CP", "busy"], ["CP", "busy"]],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[0, 0], [0, 0]],
    )

    yield (
        [["CP", "busy"], ["CP", "busy"]],
        [["CP", "busy"], ["CP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0.5, 0], [1.2, 0]],
    )

    yield (
        [["idle", "CP", "busy"], ["CP", "busy", "idle"]],
        [["CP", "busy", "idle"], ["idle", "CP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0, 0.5, 0], [1.5, 0, 0]],
    )

    yield (
        [[["idle", "CP_r"], ["any", "busy"]], [["CP", "busy"], ["any", "idle"]]],
        [[["CP", "busy"], ["any", "idle"]], [["idle", "CP_r"], ["any", "busy"]]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[[0, 0.5], [0, 0]], [[1.5, 0], [0, 0]]],
    )

    yield (
        [[["any", "idle"], ["CP", "busy"]], [["any", "CP_r"], ["idle", "busy"]]],
        [[["any", "CP_r"], ["idle", "busy"]], [["any", "idle"], ["CP", "busy"]]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[[0, 0], [0.5, 0]], [[0, 1.5], [0, 0]]],
    )

    yield (
        [[["CP_r", "any"], ["busy", "idle"]], [["idle", "any"], ["CP", "busy"]]],
        [[["idle", "any"], ["CP", "busy"]], [["CP_r", "any"], ["busy", "idle"]]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[[0.5, 0], [0, 0]], [[0, 0], [1.5, 0]]],
    )

    yield (
        [[["CP", "busy"], ["idle", "any"]], [["CP_r", "idle"], ["busy", "any"]]],
        [[["CP_r", "idle"], ["busy", "any"]], [["CP", "busy"], ["idle", "any"]]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[[0.5, 0], [0, 0]], [[1.5, 0], [0, 0]]],
    )

    yield (
        [["CP", "busy", "idle"], ["idle", "CP", "busy"]],
        [["idle", "CP", "busy"], ["CP", "busy", "idle"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0.5, 0, 0], [0, 1.5, 0]],
    )

    yield (
        [[["CP", "busy"], ["any", "idle"]], [["idle", "CP_r"], ["any", "busy"]]],
        [[["idle", "CP_r"], ["any", "busy"]], [["CP", "busy"], ["any", "idle"]]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[[0.5, 0], [0, 0]], [[0, 1.5], [0, 0]]],
    )

    yield (
        [[["any", "CP_r"], ["idle", "busy"]], [["any", "idle"], ["CP", "busy"]]],
        [[["any", "idle"], ["CP", "busy"]], [["any", "CP_r"], ["idle", "busy"]]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[[0, 0.5], [0, 0]], [[0, 0], [1.5, 0]]],
    )

    yield (
        [[["idle", "any"], ["CP", "busy"]], [["CP_r", "any"], ["busy", "idle"]]],
        [[["CP_r", "any"], ["busy", "idle"]], [["idle", "any"], ["CP", "busy"]]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[[0, 0], [1.5, 0]], [[0.5, 0], [0, 0]]],
    )

    yield (
        [[["CP_r", "idle"], ["busy", "any"]], [["CP", "busy"], ["idle", "any"]]],
        [[["CP", "busy"], ["idle", "any"]], [["CP_r", "idle"], ["busy", "any"]]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[[1.1, 0], [0, 0]], [[0.7, 0], [0, 0]]],
    )

    for rot_unit in ROT_EXCANGE_QUANTA:

        def rot_amplitudes_transform(rot_amplitudes_array):
            rot_amplitudes_array.flat[0] += rot_unit
            rot_amplitudes_array.flat[2] -= rot_unit
            rot_amplitudes_array %= PERIOD
            return rot_amplitudes_array

        yield (
            [["CP", "busy"], ["CP", "busy"]],
            [["CP", "busy"], ["CP", "busy"]],
            lambda rot_amplitudes_array: True,
            rot_amplitudes_transform,
            [[2, 0], [3, 0]],
        )


def r_cp_rules():
    """
    Yields transformation rules between RZ, RX and CP gates.
    """

    yield (
        [["CP", "busy"], ["RZ", "idle"]],
        [["RZ", "idle"], ["CP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[1, 0], [2, 0]],
    )

    yield (
        [["RZ", "idle"], ["CP", "busy"]],
        [["CP", "busy"], ["RZ", "idle"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[1, 0], [2, 0]],
    )

    yield (
        [["CP", "busy"], ["idle", "RZ"]],
        [["idle", "RZ"], ["CP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[1, 0], [0, 2]],
    )

    yield (
        [["idle", "RZ"], ["CP", "busy"]],
        [["CP", "busy"], ["idle", "RZ"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0, 1], [2, 0]],
    )

    yield (
        [["CP", "busy"], ["RZ", "RZ"]],
        [["RZ", "RZ"], ["CP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[1, 0], [2, 3]],
    )

    yield (
        [["RZ", "RZ"], ["CP", "busy"]],
        [["CP", "busy"], ["RZ", "RZ"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[2, 1], [3, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[2] = PERIOD - rot_amplitudes_array.flat[0]
        rot_amplitudes_array.flat[1] = PI
        rot_amplitudes_array.flat[3] = 0
        return rot_amplitudes_array

    yield (
        [["CP", "busy"], ["idle", "RX"]],
        [["RZ", "RX"], ["CP", "busy"]],
        lambda rot_amplitudes_array: rot_amplitudes_array.flat[3] == PI,
        rot_amplitudes_transform,
        [[1, 0], [0, PI]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[2] = PERIOD - rot_amplitudes_array.flat[0]
        rot_amplitudes_array.flat[1] = rot_amplitudes_array.flat[0]
        rot_amplitudes_array.flat[0] = PI
        rot_amplitudes_array.flat[3] = 0
        return rot_amplitudes_array

    yield (
        [["CP", "busy"], ["RX", "idle"]],
        [["RX", "RZ"], ["CP", "busy"]],
        lambda rot_amplitudes_array: rot_amplitudes_array.flat[2] == PI,
        rot_amplitudes_transform,
        [[1, 0], [PI, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = PERIOD - rot_amplitudes_array.flat[2]
        rot_amplitudes_array.flat[1] = 0
        rot_amplitudes_array.flat[3] = PI
        return rot_amplitudes_array

    yield (
        [["idle", "RX"], ["CP", "busy"]],
        [["CP", "busy"], ["RZ", "RX"]],
        lambda rot_amplitudes_array: rot_amplitudes_array.flat[1] == PI,
        rot_amplitudes_transform,
        [[0, PI], [1, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = PERIOD - rot_amplitudes_array.flat[2]
        rot_amplitudes_array.flat[3] = rot_amplitudes_array.flat[2]
        rot_amplitudes_array.flat[1] = 0
        rot_amplitudes_array.flat[2] = PI
        return rot_amplitudes_array

    yield (
        [["RX", "idle"], ["CP", "busy"]],
        [["CP", "busy"], ["RX", "RZ"]],
        lambda rot_amplitudes_array: rot_amplitudes_array.flat[0] == PI,
        rot_amplitudes_transform,
        [[PI, 0], [1, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[1] = 0
        rot_amplitudes_array.flat[2] = 0
        rot_amplitudes_array.flat[3] = PI
        return rot_amplitudes_array

    yield (
        [["RZ", "RX"], ["CP", "busy"]],
        [["CP", "busy"], ["idle", "RX"]],
        lambda rot_amplitudes_array: (rot_amplitudes_array.flat[1] == PI)
        and (rot_amplitudes_array.flat[0] == PERIOD - rot_amplitudes_array.flat[2]),
        rot_amplitudes_transform,
        [[1, PI], [PERIOD - 1, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = rot_amplitudes_array.flat[1]
        rot_amplitudes_array.flat[1] = 0
        rot_amplitudes_array.flat[2] = PI
        return rot_amplitudes_array

    yield (
        [["RX", "RZ"], ["CP", "busy"]],
        [["CP", "busy"], ["RX", "idle"]],
        lambda rot_amplitudes_array: (rot_amplitudes_array.flat[0] == PI)
        and (rot_amplitudes_array.flat[1] == PERIOD - rot_amplitudes_array.flat[2]),
        rot_amplitudes_transform,
        [[PI, 1], [PERIOD - 1, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = 0
        rot_amplitudes_array.flat[1] = PI
        rot_amplitudes_array.flat[3] = 0
        return rot_amplitudes_array

    yield (
        [["CP", "busy"], ["RZ", "RX"]],
        [["idle", "RX"], ["CP", "busy"]],
        lambda rot_amplitudes_array: (rot_amplitudes_array.flat[3] == PI)
        and (rot_amplitudes_array.flat[0] == PERIOD - rot_amplitudes_array.flat[2]),
        rot_amplitudes_transform,
        [[1, 0], [PERIOD - 1, PI]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = PI
        rot_amplitudes_array.flat[2] = rot_amplitudes_array.flat[3]
        rot_amplitudes_array.flat[3] = 0
        return rot_amplitudes_array

    yield (
        [["CP", "busy"], ["RX", "RZ"]],
        [["RX", "idle"], ["CP", "busy"]],
        lambda rot_amplitudes_array: (rot_amplitudes_array.flat[2] == PI)
        and (rot_amplitudes_array.flat[0] == PERIOD - rot_amplitudes_array.flat[3]),
        rot_amplitudes_transform,
        [[1, 0], [PI, PERIOD - 1]],
    )


def swap_ann_rules():
    """
    Yields transformation rules between SWAP gates.
    """

    yield (
        [["SWAP", "busy"], ["SWAP", "busy"]],
        [["idle", "idle"], ["idle", "idle"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0, 0], [0, 0]],
    )

    yield (
        [["idle", "idle"], ["idle", "idle"]],
        [["SWAP", "busy"], ["SWAP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0, 0], [0, 0]],
    )

    yield (
        [["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"]],
        [["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
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
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
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
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
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
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
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
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    yield (
        [["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"]],
        [["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    )

    yield (
        [
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
        ],
        [
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
        ],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    yield (
        [
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
        ],
        [
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    yield (
        [
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
        ],
        [
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    yield (
        [
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
        ],
        [
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
        ],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: rot_amplitudes_array,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )


def swap_sqg_rules():
    """
    Yields transformation rules between SWAP and single qubit gates.
    """

    for gate in product(SQ_GATES, SQ_GATES):
        if gate[0] != "idle":
            rot_0 = 1.0
        else:
            rot_0 = 0.0

        if gate[1] != "idle":
            rot_1 = 2.0
        else:
            rot_1 = 0.0

        yield (
            [["SWAP", "busy"], [gate[0], gate[1]]],
            [[gate[1], gate[0]], ["SWAP", "busy"]],
            lambda rot_amplitudes_array: True,
            lambda rot_amplitudes_array: np.flip(rot_amplitudes_array),
            [[0, 0], [rot_0, rot_1]],
        )

        yield (
            [[gate[1], gate[0]], ["SWAP", "busy"]],
            [["SWAP", "busy"], [gate[0], gate[1]]],
            lambda rot_amplitudes_array: True,
            lambda rot_amplitudes_array: np.flip(rot_amplitudes_array),
            [[rot_1, rot_0], [0, 0]],
        )


def swap_cp_rules():
    """
    Yields transformation rules between CP and SWAP gates.
    """
    yield (
        [["CP", "busy"], ["SWAP", "busy"]],
        [["SWAP", "busy"], ["CP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[1, 0], [0, 0]],
    )

    yield (
        [["SWAP", "busy"], ["CP", "busy"]],
        [["CP", "busy"], ["SWAP", "busy"]],
        lambda rot_amplitudes_array: True,
        lambda rot_amplitudes_array: np.flip(rot_amplitudes_array, 0),
        [[0, 0], [1, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[7] = rot_amplitudes_array.flat[0]
        rot_amplitudes_array.flat[0] = 0
        return rot_amplitudes_array

    yield (
        [["CP", "busy", "idle"], ["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"]],
        [["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"], ["idle", "CP", "busy"]],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[1, 0, 0], [0, 0, 0], [0, 0, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[9] = rot_amplitudes_array.flat[0]
        rot_amplitudes_array.flat[0] = 0
        return rot_amplitudes_array

    yield (
        [
            [["CP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
        ],
        [
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "CP_r"], ["any", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[1, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[10] = rot_amplitudes_array.flat[1]
        rot_amplitudes_array.flat[1] = 0
        return rot_amplitudes_array

    yield (
        [
            [["any", "CP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
        ],
        [
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["CP", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 1], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[8] = rot_amplitudes_array.flat[2]
        rot_amplitudes_array.flat[2] = 0
        return rot_amplitudes_array

    yield (
        [
            [["idle", "any"], ["CP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
        ],
        [
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
            [["CP_r", "any"], ["busy", "idle"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [1, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[8] = rot_amplitudes_array.flat[0]
        rot_amplitudes_array.flat[0] = 0
        return rot_amplitudes_array

    yield (
        [
            [["CP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
        ],
        [
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["CP", "busy"], ["idle", "any"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[1, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[1] = rot_amplitudes_array.flat[6]
        rot_amplitudes_array.flat[6] = 0
        return rot_amplitudes_array

    yield (
        [["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"], ["CP", "busy", "idle"]],
        [["idle", "CP", "busy"], ["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"]],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[1] = rot_amplitudes_array.flat[8]
        rot_amplitudes_array.flat[8] = 0
        return rot_amplitudes_array

    yield (
        [
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["CP", "busy"], ["any", "idle"]],
        ],
        [
            [["idle", "CP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[1, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[2] = rot_amplitudes_array.flat[9]
        rot_amplitudes_array.flat[9] = 0
        return rot_amplitudes_array

    yield (
        [
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "CP_r"], ["idle", "busy"]],
        ],
        [
            [["any", "idle"], ["CP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 1], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = rot_amplitudes_array.flat[10]
        rot_amplitudes_array.flat[10] = 0
        return rot_amplitudes_array

    yield (
        [
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["CP", "busy"]],
        ],
        [
            [["CP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [1, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = rot_amplitudes_array.flat[8]
        rot_amplitudes_array.flat[8] = 0
        return rot_amplitudes_array

    yield (
        [
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
            [["CP_r", "idle"], ["busy", "any"]],
        ],
        [
            [["CP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[1, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = rot_amplitudes_array.flat[7]
        rot_amplitudes_array.flat[7] = 0
        return rot_amplitudes_array

    yield (
        [["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"], ["idle", "CP", "busy"]],
        [["CP", "busy", "idle"], ["idle", "SWAP", "busy"], ["SWAP", "busy", "idle"]],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = rot_amplitudes_array.flat[9]
        rot_amplitudes_array.flat[9] = 0
        return rot_amplitudes_array

    yield (
        [
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "CP_r"], ["any", "busy"]],
        ],
        [
            [["CP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 1], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[1] = rot_amplitudes_array.flat[10]
        rot_amplitudes_array.flat[10] = 0
        return rot_amplitudes_array

    yield (
        [
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["CP", "busy"]],
        ],
        [
            [["any", "CP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [1, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[2] = rot_amplitudes_array.flat[8]
        rot_amplitudes_array.flat[8] = 0
        return rot_amplitudes_array

    yield (
        [
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
            [["CP_r", "any"], ["busy", "idle"]],
        ],
        [
            [["idle", "any"], ["CP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[1, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[0] = rot_amplitudes_array.flat[8]
        rot_amplitudes_array.flat[8] = 0
        return rot_amplitudes_array

    yield (
        [
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["CP", "busy"], ["idle", "any"]],
        ],
        [
            [["CP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[1, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[6] = rot_amplitudes_array.flat[1]
        rot_amplitudes_array.flat[1] = 0
        return rot_amplitudes_array

    yield (
        [["idle", "CP", "busy"], ["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"]],
        [["SWAP", "busy", "idle"], ["idle", "SWAP", "busy"], ["CP", "busy", "idle"]],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[8] = rot_amplitudes_array.flat[1]
        rot_amplitudes_array.flat[1] = 0
        return rot_amplitudes_array

    yield (
        [
            [["idle", "CP_r"], ["any", "busy"]],
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
        ],
        [
            [["SWAP", "busy"], ["any", "idle"]],
            [["idle", "SWAP_r"], ["any", "busy"]],
            [["CP", "busy"], ["any", "idle"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 1], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[9] = rot_amplitudes_array.flat[2]
        rot_amplitudes_array.flat[2] = 0
        return rot_amplitudes_array

    yield (
        [
            [["any", "idle"], ["CP", "busy"]],
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
        ],
        [
            [["any", "SWAP_r"], ["idle", "busy"]],
            [["any", "idle"], ["SWAP", "busy"]],
            [["any", "CP_r"], ["idle", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[0, 0], [1, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[10] = rot_amplitudes_array.flat[0]
        rot_amplitudes_array.flat[0] = 0
        return rot_amplitudes_array

    yield (
        [
            [["CP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
        ],
        [
            [["idle", "any"], ["SWAP", "busy"]],
            [["SWAP_r", "any"], ["busy", "idle"]],
            [["idle", "any"], ["CP", "busy"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[1, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )

    def rot_amplitudes_transform(rot_amplitudes_array):
        rot_amplitudes_array.flat[8] = rot_amplitudes_array.flat[0]
        rot_amplitudes_array.flat[0] = 0
        return rot_amplitudes_array

    yield (
        [
            [["CP", "busy"], ["idle", "any"]],
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
        ],
        [
            [["SWAP_r", "idle"], ["busy", "any"]],
            [["SWAP", "busy"], ["idle", "any"]],
            [["CP_r", "idle"], ["busy", "any"]],
        ],
        lambda rot_amplitudes_array: True,
        rot_amplitudes_transform,
        [[[1, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    )


def r_cp_swap_rules():
    """
    Yields transformation rules between RZ, RX and CP gates to synthetize SWAP.
    """

    array_in = np.array([PI, 0, 3 * PI / 2, PI / 2, PI, 0, PI / 2, 3 * PI / 2])
    array_out = np.array([3 * PI / 2, PI / 2, 0, 0, PI, 0, 0, 0])
    yield (
        [["CP", "busy"], ["RX", "RX"], ["CP", "busy"], ["RX", "RX"]],
        [["RX", "RX"], ["SWAP", "busy"], ["CP", "busy"], ["idle", "idle"]],
        lambda rot_amplitudes_array: np.all(
            rot_amplitudes_array == array_in.reshape(rot_amplitudes_array.shape)
        ),
        lambda rot_amplitudes_array: array_out.reshape(rot_amplitudes_array.shape),
        [[PI, 0], [3 * PI / 2, PI / 2], [PI, 0], [PI / 2, 3 * PI / 2]],
    )

    array_in = np.array([PI, 0, PI / 2, 3 * PI / 2, PI, 0, 3 * PI / 2, PI / 2])
    array_out = np.array([PI / 2, 3 * PI / 2, 0, 0, PI, 0, 0, 0])
    yield (
        [["CP", "busy"], ["RX", "RX"], ["CP", "busy"], ["RX", "RX"]],
        [["RX", "RX"], ["SWAP", "busy"], ["CP", "busy"], ["idle", "idle"]],
        lambda rot_amplitudes_array: np.all(
            rot_amplitudes_array == array_in.reshape(rot_amplitudes_array.shape)
        ),
        lambda rot_amplitudes_array: array_out.reshape(rot_amplitudes_array.shape),
        [[PI, 0], [PI / 2, 3 * PI / 2], [PI, 0], [3 * PI / 2, PI / 2]],
    )

    array_in = np.array([3 * PI / 2, PI / 2, 0, 0, PI, 0, 0, 0])
    array_out = np.array([PI, 0, 3 * PI / 2, PI / 2, PI, 0, PI / 2, 3 * PI / 2])
    yield (
        [["RX", "RX"], ["SWAP", "busy"], ["CP", "busy"], ["idle", "idle"]],
        [["CP", "busy"], ["RX", "RX"], ["CP", "busy"], ["RX", "RX"]],
        lambda rot_amplitudes_array: np.all(
            rot_amplitudes_array == array_in.reshape(rot_amplitudes_array.shape)
        ),
        lambda rot_amplitudes_array: array_out.reshape(rot_amplitudes_array.shape),
        [[3 * PI / 2, PI / 2], [0, 0], [PI, 0], [0, 0]],
    )

    array_in = np.array([PI / 2, 3 * PI / 2, 0, 0, PI, 0, 0, 0])
    array_out = np.array([PI, 0, PI / 2, 3 * PI / 2, PI, 0, 3 * PI / 2, PI / 2])
    yield (
        [["RX", "RX"], ["SWAP", "busy"], ["CP", "busy"], ["idle", "idle"]],
        [["CP", "busy"], ["RX", "RX"], ["CP", "busy"], ["RX", "RX"]],
        lambda rot_amplitudes_array: np.all(
            rot_amplitudes_array == array_in.reshape(rot_amplitudes_array.shape)
        ),
        lambda rot_amplitudes_array: array_out.reshape(rot_amplitudes_array.shape),
        [[PI / 2, 3 * PI / 2], [0, 0], [PI, 0], [0, 0]],
    )


STD_CONTINUOUS_RULES_GENERATORS = [
    rz_rules,
    rx_rules,
    rz_rx_rules,
    cp_rules,
    r_cp_rules,
    swap_ann_rules,
    swap_sqg_rules,
    swap_cp_rules,
    r_cp_swap_rules,
]
