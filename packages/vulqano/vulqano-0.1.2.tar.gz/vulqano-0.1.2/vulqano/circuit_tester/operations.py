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
Operations used in the simultion of the circuit to check the effective fidelity
after the run from the compiler.
The operations have a infidelity > 0, with different values based on the
requirements of the user.

There are two possible classes for handling and generate the operations:

- ``ContinuosOperations``, for parametrized operations;
- ``DiscreteOperations``, for discrete operations.

The available operations are:

- "idle", "RZ", "RX", "CP", "CP_r", "SWAP", SWAP_r", "CPCP_XTALK";
- "I", "T", "Tdg", "S", "Sdg", "Z", "H", "CZ", "CZ_r", "SWAP", SWAP_r", "CZCZ_XTALK"
"""
# pylint: disable=too-few-public-methods


import numpy as np


try:
    import qmatchatea.circuit.operations as qmop
except ImportError:
    qmop = None


__all__ = ["DiscreteOperations", "ContinuosOperations"]


class DiscreteOperations:
    """
    Class to handle the discrete oprations of a given simulation

    **Arguments**

    id_infidelity: float
        What should be the infidelity of an identity, i.e.
        of an idle qubit. It is used as scale for the infidelity
        of all the other operations, which are defined
        as `id_infidelity*weights_dict["operation"]`.
    weights_dict: Dictionary[(str, float)]
        Dictionary with the infidelity weight of each operation.
    infidelity_method : str | callable, optional
        Way to implement the infidelity of the gate. If str,
        you have to choose from the available methods:
        - "gaussian", add gaussian noise
        If callable, it should be a function that takes in input
        the gate name and returns the gate matrix with the error.
    cross_talk : str | callable
        Crosstalk model.
        - If "gaussian", use gaussian noise on the four-qubits gate
        If callable, it should be a function that takes in input
        the gate name (with the xtalk configuration) and returns
        the gate matrix with the error.
        Default to None.
    """

    def __init__(
        self,
        id_infidelity,
        weights_dict,
        infidelity_method="gaussian",
        cross_talk="gaussian",
    ):

        if qmop is None:
            raise ImportError("Please install qmatchatea.")

        self.id_infidelity = id_infidelity
        self.weights_dict = weights_dict

        if isinstance(infidelity_method, str):
            self._infidelity_method = getattr(
                self, f"_{infidelity_method.lower()}_infidelity"
            )
        elif callable(infidelity_method):
            self._infidelity_method = infidelity_method
        else:
            raise ValueError(
                f"Only str or callable can be crosstalk, not {type(infidelity_method)}"
            )

        if isinstance(cross_talk, str):
            self._cross_talk = getattr(self, f"_{cross_talk.lower()}_crosstalk")
        elif callable(cross_talk):
            self._cross_talk = cross_talk
        else:
            raise ValueError(
                f"Only str or callable can be crosstalk, not {type(cross_talk)}"
            )

        # Dictionary of the available operations
        self._ops = {
            "idle": QCId,
            "I": QCId,
            "T": qmop.QCTgate,
            "TDG": qmop.QCTadggate,
            "S": qmop.QCSgate,
            "SDG": qmop.QCSadggate,
            "Z": qmop.QCZpauli,
            "H": qmop.QCHadamard,
            "CZ": qmop.QCCz,
            "CZ_r": qmop.QCCz,
            "SWAP": qmop.QCSwap,
            "SWAP_r": qmop.QCSwap,
        }

    @property
    def operations(self):
        """Property giving a list of the available operations"""
        return list(self._ops.keys())

    def __getitem__(self, key):
        """
        Get the operation with name `key`

        **Arguments**

        key : Tuple[ str, Tuple[float] ]
            Name of the operation you are interested in
            and its parameters

        **Returns**

        `QCOperation`
            Operation with the correct infidelity
        """
        if isinstance(key, str):
            name = key
            params = []
        else:
            name, params = key
        name = name.upper()
        # This is the default case
        if name in self._ops:
            # Apply the noise to the operation
            operation_mat = self._infidelity_method(name, params)
        # The only case that is not here is for crosstalk
        elif name == "XTALK":
            # First, we create the 4-qubit gate without crosstalk
            operation_mat = self._cross_talk(params)
            key = str(key)
        else:
            raise KeyError(
                f"{name} is not available, use only XTALK, {self._ops.keys()}"
            )

        # Create a new operation with the given matrix
        operation = qmop.QCOperation(name=name, operator=lambda: operation_mat)
        return operation

    def _gaussian_infidelity(self, operation_name, params):
        """
        Apply a gaussian noise to the operation

        **Arguments**

        operation_name : str
            The name of the operation to be applied
        params : Tuple[float]
            Tuple of the operation parameres

        **Returns**

        np.ndarray
            The matrix of the operation taking into account the infidelity
        """

        infidelity = self.id_infidelity * self.weights_dict[operation_name]
        op_mat = self._ops[operation_name](*params).operator

        op_mat = op_mat + np.random.normal(0, infidelity, size=op_mat.shape)
        return op_mat

    def _gaussian_crosstalk(self, params):
        """
         Apply a gaussian noise to the operation

        **Arguments**

         params : float
             The weight of this specific type of crosstalk
             If None, no parameters are used. Default to None.

         **Returns**

         np.ndarray
             The matrix of the operation taking into account the infidelity
        """

        infidelity = self.id_infidelity * params[0]
        op_mat = np.identity(16, dtype=np.float64)
        op_mat += np.random.normal(0, infidelity, size=op_mat.shape)

        return op_mat

    def _cccp_crosstalk(self, params):
        """
        Apply the crosstalk as a triple-controlled phase with a
        normally distributed phase

        **Arguments**

        params : float
            The weight of this specific type of crosstalk
            If None, no parameters are used. Default to None.

        **Returns**

        np.ndarray
            The matrix of the operation taking into account the infidelity
        """

        infidelity = self.id_infidelity * params[0] * 0.0010420522033015207
        op_mat = np.identity(16, dtype=np.complex128)
        op_mat[-1, -1] = np.exp(1j * np.random.normal(0, infidelity))

        return op_mat


class ContinuosOperations(DiscreteOperations):
    """
    Class to handle the discrete oprations of a given simulation

    **Arguments**

    id_infidelity: float
        What should be the infidelity of an identity, i.e.
        of an idle qubit. It is used as scale for the infidelity
        of all the other operations, which are defined
        as `id_infidelity*weights_dict["operation"]`.
    weights_dict: Dictionary[(str, float)]
        Dictionary with the infidelity weight of each operation.
    infidelity_method : str | callable, optional
        Way to implement the infidelity of the gate. If str,
        you have to choose from the available methods:
        - "gaussian", add gaussian noise to the matrix
        - "gaussian_on_params", add gaussian noise to the gate parameters
        If callable, it should be a function that takes in input
        the gate name and gate parameters and returns the gate matrix with the error.
    cross_talk : str | callable
        Crosstalk model.
        - If "gaussian", use gaussian noise on the four-qubits gate
        If callable, it should be a function that takes in input
        the gate name (with the xtalk configuration) and returns
        the gate matrix with the error.
        Default to None.
    """

    def __init__(
        self,
        id_infidelity,
        weights_dict,
        infidelity_method="gaussian",
        cross_talk="gaussian",
    ):
        super().__init__(
            id_infidelity,
            weights_dict,
            infidelity_method=infidelity_method,
            cross_talk=cross_talk,
        )

        # Dictionary of the available operations
        self._ops.update(
            {
                "I": QCId,
                "RZ": qmop.QCPgate,
                "RX": QCRX,
                "RY": QCRY,
                "CP": qmop.QCCp,
                "CP_r": qmop.QCCp,
                "SWAP": qmop.QCSwap,
                "SWAP_r": qmop.QCSwap,
            }
        )

    def _gaussian_on_params_infidelity(self, operation_name, operation_params):
        """
        Apply a gaussian noise to the operation

        **Arguments**

        operation_name : str
            The name of the operation to be applied
        operation_params : Tuple[float]
            Tuple of the operation parameres

        Returns
        -------
        np.ndarray
            The matrix of the operation taking into account the infidelity
        """
        old_operation_name = None
        # Map for constant gates to parametric form
        if operation_name == "H":
            # Decomposition in X + Ry(pi/2)
            operation_params = (np.pi / 2,)
            operation_name = "RY"
            old_operation_name = "H"
        elif operation_name == "T":
            # Decomposition in Rz(pi/4)
            operation_params = (np.pi / 4,)
            operation_name = "RZ"
        elif operation_name == "TDG":
            # Decomposition in Rz(pi/4)
            operation_params = (-np.pi / 4,)
            operation_name = "RZ"
        elif operation_name == "CZ":
            # Decomposition in Cp
            operation_params = (np.pi,)
            operation_name = "CP"
        elif operation_name == "SWAP":
            return self._gaussian_on_params_infidelity_swap()

        if operation_params is None:
            return self._gaussian_infidelity(operation_name, operation_params)

        infidelity = self.id_infidelity * self.weights_dict[operation_name]
        noise = np.random.normal(0, infidelity, size=len(operation_params))
        params = (pp + noise[ii] for ii, pp in enumerate(operation_params))
        op_mat = self._ops[operation_name](*params).operator

        if old_operation_name == "H":
            op_mat = np.array([[0, 1], [1, 0]], dtype=complex) @ op_mat

        return op_mat

    def _gaussian_on_params_infidelity_swap(self):
        """
        Generate a SWAP gate with a given infidelity supposing that
        the swap can be decomposed in the following form, where
        the CZ has the gaussian error on the parameters

        ---0-H-0-H-0---
           |   |   |
        -H-0-0-0-H-0-H-
        """
        infidelity = self.id_infidelity * self.weights_dict["SWAP"]
        had = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
        hhhh = np.kron(had, had)
        idhh = np.kron(np.identity(2), had)
        czs = [
            np.array(
                [
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, np.exp(1j * (np.pi + np.random.normal(0, infidelity)))],
                ]
            )
            for _ in range(3)
        ]
        swap = idhh @ czs[0] @ hhhh @ czs[1] @ hhhh @ czs[2] @ idhh

        return swap


# Definition of operations not avaliable in qmatchatea


class QCId(qmop.QCOperation):
    """
    Identity gate

    **Arguments**

    conditioned : :py:class:`ClassicalCondition`, optional
        Classical condition to be checked for applying the operation on the
        simulation.
    """

    def __init__(self, conditioned=qmop.ClassicalCondition()):
        super().__init__("id", None, conditioned=conditioned)

    @property
    def operator(self):
        """
        Overwriting operator with identity
        """
        return np.identity(2)


class QCRX(qmop.QCOperation):
    """
    Rotatio on X axis gate

    **Arguments**

    theta: float
        Rotation angle along X
    conditioned : :py:class:`ClassicalCondition`, optional
        Classical condition to be checked for applying the operation on the
        simulation.
    """

    def __init__(self, theta, conditioned=qmop.ClassicalCondition()):
        super().__init__("rx", self.matrix, theta, conditioned=conditioned)

    @staticmethod
    def matrix(theta):
        """
        Overwriting operator with RX gate
        """
        theta = theta / 2
        return np.array(
            [[np.cos(theta), -1j * np.sin(theta)], [-1j * np.sin(theta), np.cos(theta)]]
        )


class QCRY(qmop.QCOperation):
    """
    Rotatio on Y axis gate

    **Arguments**

    theta: float
        Rotation angle along Y
    conditioned : :py:class:`ClassicalCondition`, optional
        Classical condition to be checked for applying the operation on the
        simulation.
    """

    def __init__(self, theta, conditioned=qmop.ClassicalCondition()):
        super().__init__("ry", self.matrix, theta, conditioned=conditioned)

    @staticmethod
    def matrix(theta):
        """
        Overwriting operator with RX gate
        """
        theta = theta / 2
        return np.array(
            [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]],
            dtype=complex,
        )
