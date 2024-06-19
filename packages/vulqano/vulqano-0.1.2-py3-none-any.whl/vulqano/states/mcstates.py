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
Define a class for Markov chain circuit states.

Note:
While in abstract states the gates are encoded as strings, in Markov chain states
the gates are labeled by integers. This different encoding allows to more quickly
check whether a rule applies to the circuit state.
"""

import numpy as np
from vulqano.states.abstractcircuitstate import AbstractCircuitState
from vulqano.gates.discretegates import ROT_NUMBERS
from vulqano.gates.discretegates import (
    gate_labels_to_ints as discrete_array_strings_to_ints,
)
from vulqano.gates.discretegates import (
    gate_ints_to_labels as discrete_array_ints_to_strings,
)
from vulqano.gates.continuousgates import (
    gate_labels_to_ints as continuous_array_strings_to_ints,
)
from vulqano.gates.continuousgates import (
    gate_ints_to_labels as continuous_array_ints_to_strings,
)


__all__ = [
    "_MCState",
    "DiscreteMCState",
    "ContinuousMCState",
]


class _MCState:
    """
    Base class for Markov chain circuit states.
    """

    def transition(self, position, rule, transition_instructions):
        """
        Locally transforms the circuit by replacing a subcircuit.

        **Arguments**

        position : tuple of ints
            Position in the time-qubit lattice where the new subcircuit is placed.
        rule : DiscereteMCRule
            Transtition rule.
        transition_instructions : object
            Other instructions.

        **Returns**

        None.
        """
        raise NotImplementedError("Not yet implemented")

    def check_rule(self, rule, position):
        """
        Check if a rule can be applied to a region of the state.

        **Arguments**

        rule : DiscreteMCRule
            Discrete MC rule to be applied to a region of the state.
        position : tuple of ints
            Position in the time-qubit lattice where the rule is tested.

        **Returns**

           : (bool, bool)
           The first bool indicates if the rule can be applied. The second bool
           indicates the direction of the rule, True for state_a->state_b, and
           false for state_b->state_a.

        """
        raise NotImplementedError("Not yet implemented")

    def to_abstract(self, name):
        """
        Returns the circuit as an abstract circuit.

        **Arguments**

        name : str
            Name of the circuit.

        **Returns**

        AbstractCircuitState
            Abstract representation of the circuit.
        """
        raise NotImplementedError("Not yet implemented")


class DiscreteMCState(_MCState):
    """
    Class for discrete Markov chain circuit states.

    **Arguments**

    abstractstate : AbstractCircuitState
        AbstractCircuitState to be converted to a DiscreteMCState.

    **Attributes**

    vector : numpy.array
        Array of gates applied at each time and on each qubit. The first index
        correspond to the time step, the other indices label the qubit in the
        lattice.
    times : int
        Circuit depth.
    qubits : touple of ints
        Number of qubits in each direction of the lattice.
    dim : int
        Number of dimension of the circuit state, i.e. 1 + number of dimensions
        of the qubits lattice.
    rot_mask : mask
        True where the qubit is a rotation.
    """

    def __init__(self, abstractstate):
        if abstractstate.is_continuous:
            raise ValueError(
                "Only discrete abstract states can be converted to DiscreteMCState"
            )
        self.vector = discrete_array_strings_to_ints(abstractstate.vector)
        self.times = abstractstate.times
        self.qubits = abstractstate.qubits
        self.dim = abstractstate.dim
        if self.dim not in [2, 3]:
            raise ValueError(
                "Only (1+1)d and (1+2)d MC circuit states are implemented."
            )
        self.rot_mask = np.isin(abstractstate.vector, ROT_NUMBERS)

    def transition(self, position, rule, transition_instructions):
        """
        Locally transforms the circuit by replacing a subcircuit.

        **Arguments**

        position : tuple of ints
            Position in the time-qubit lattice where the new subcircuit is placed.
        rule : DiscereteMCRule
            Transtition rule.
        transition_instructions : (np.array, mask)
            Matrix representing the new subcircuit.
            Where the mask is true, the gate is not raplaced.

        **Returns**

        None.
        """
        slices = tuple(
            slice(position[i], position[i] + transition_instructions[0].shape[i])
            for i in range(self.dim)
        )
        np.putmask(
            self.vector[slices],
            transition_instructions[1],
            transition_instructions[0],
        )
        self.rot_mask[slices] = np.isin(self.vector[slices], ROT_NUMBERS)

    def check_rule(self, rule, position):
        """
        Check if a rule can be applied to a region of the state.

        **Arguments**

        rule : DiscreteMCRule
            Discrete MC rule to be applied to a region of the state.
        position : tuple of ints
            Position in the time-qubit lattice where the rule is tested.

        **Returns**

           : (bool, bool)
           The first bool indicates if the rule can be applied. The second bool
           indicates the direction of the rule, True for state_a->state_b, and
           false for state_b->state_a.

        """
        slices = tuple(
            slice(position[i], position[i] + rule.shape[i]) for i in range(self.dim)
        )
        sub_circ = self.vector[slices]
        if rule.shape == sub_circ.shape:
            sub_rot_mask = self.rot_mask[slices]
            mask = sub_rot_mask & rule.masks[1]
            if np.all(np.equal(sub_circ, rule.state_a) | rule.masks[0] | mask):
                return (True, True)
            if np.all(np.equal(sub_circ, rule.state_b) | rule.masks[0] | mask):
                return (True, False)
        return (False, False)

    def to_abstract(self, name):
        """
        Returns the circuit as an abstract circuit.

        **Arguments**

        name : str
            Name of the circuit.

        **Returns**

        AbstractCircuitState
            Abstract representation of the circuit.
        """
        return AbstractCircuitState(discrete_array_ints_to_strings(self.vector), name)


class ContinuousMCState(_MCState):
    """
    Class for continuous Markov chain circuit states.

    **Arguments**

    abstractstate : AbstractCircuitState
        AbstractCircuitState to be converted to a ContinuousMCState.

    **Attributes**

    vector : numpy.array
        Array of gates applied at each time and on each qubit. The first index
        correspond to the time step, the other indices label the qubit in the
        lattice.
    times : int
        Circuit depth.
    qubits : touple of ints
    dim : int
        Number of dimension of the circuit state, i.e. 1 + number of dimensions
        of the qubits lattice.
        Number of qubits in each direction of the lattice.
    rot_amplitudes : np array of float.
        A numpy array of float with the same shape of the circuit, where at each
        entry a parameter is specified for the corresponding continuous gate.
    """

    def __init__(self, abstractstate):
        if not abstractstate.is_continuous:
            raise ValueError(
                "Only continuous abstract states can be converted to ContinuousMCState"
            )
        self.vector = continuous_array_strings_to_ints(abstractstate.vector)
        self.times = abstractstate.times
        self.qubits = abstractstate.qubits
        self.dim = abstractstate.dim
        if self.dim not in [2, 3]:
            raise ValueError(
                "Only (1+1)d and (1+2)d MC circuit states are implemented."
            )
        self.rot_amplitudes = np.copy(abstractstate.rot_amplitudes)

    def transition(self, position, rule, transition_instructions):
        """
        Locally transforms the circuit by replacing a subcircuit.

        **Arguments**

        position : tuple of ints
            Position in the time-qubit lattice where the new subcircuit is placed.
        rule : DiscereteMCRule
            Transtition rule.
        transition_instructions : (np.array, mask)
            Matrix representing the new subcircuit.
            Where the mask is true, the gate is not raplaced.

        **Returns**

        None.
        """
        slices = tuple(
            slice(position[i], position[i] + transition_instructions[0].shape[i])
            for i in range(self.dim)
        )
        np.putmask(
            self.vector[slices],
            transition_instructions[1],
            transition_instructions[0],
        )
        np.putmask(
            self.rot_amplitudes[slices],
            transition_instructions[1],
            rule.rot_transformation_func(self.rot_amplitudes[slices]),
        )

    def check_rule(self, rule, position):
        """
        Check if a rule can be applied to a region of the state.

        **Arguments**

        rule : ContinuousMCRule
            Continuous MC rule to be applied to a region of the state.
        position : tuple of ints
            Position in the time-qubit lattice where the rule is tested.

        **Returns**

           : (bool, bool)
           The first bool indicates if the rule can be applied. The second bool
           indicates the direction of the rule, always True for continuous rules.
        """
        slices = tuple(
            slice(position[i], position[i] + rule.shape[i]) for i in range(self.dim)
        )
        sub_circ = self.vector[slices]
        sub_circ_amplitudes = self.rot_amplitudes[slices]
        if rule.shape == sub_circ.shape:
            if np.all(
                np.equal(sub_circ, rule.state_a) | rule.any_mask
            ) and rule.amplitudes_condition(sub_circ_amplitudes):
                return (True, True)
        return (False, False)

    def to_abstract(self, name):
        """
        Returns the circuit as an abstract circuit.

        **Arguments**

        name : str
            Name of the circuit.

        **Returns**

        AbstractCircuitState
            Abstract representation of the circuit.
        """
        return AbstractCircuitState(
            continuous_array_ints_to_strings(self.vector),
            name,
            rot_amplitudes_array=self.rot_amplitudes,
        )
