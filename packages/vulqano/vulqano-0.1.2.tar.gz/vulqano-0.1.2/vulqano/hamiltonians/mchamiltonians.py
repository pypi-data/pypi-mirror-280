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
Define a class for Markov chain infidelity Hamiltonians.
"""

import itertools
import numpy as np
from numpy import ma
from vulqano.gates.discretegates import (
    gate_labels_to_ints as discrete_gate_labels_to_ints,
)
from vulqano.gates.continuousgates import (
    gate_labels_to_ints as continuous_gate_labels_to_ints,
)
from vulqano.states.abstractcircuitstate import (
    AbstractCircuitState,
    compact_hamiltonian,
)
from vulqano.states.mcstates import DiscreteMCState, ContinuousMCState


__all__ = [
    "MCHamiltonian",
]


class MCHamiltonian:
    """
    Class for continuous and discrete MC Hamiltonians encoding infidelity.

    The dictionary in input define the Hamiltonian. While in the input Hamiltonian
    the gates are encoded as strings, in Markov chain Hamiltonian the gates are
    labeled by integers. This different encoding allows to more quickly count
    a subciruit with a given cost appears in the circuit state.


    **Arguments**

    hamiltonian_operator : list of (np.array of strings, float, mask)
        Abstract description of the Hamiltonian. The energy is obtained by
        counting how many times each subcircuit hamiltonian_operator[i][0]
        appears on a region A of the circuit suck that that
        hamiltonian_operator[i][2] is True for all (t,q) in A.
        The counted number is multiplied by the weight hamiltonian_operator[i][1].
    dim : int
        Number of dimension of the circuit state on which the Hamiltonian acts,
        i.e. 1 + number of dimensions of the qubits lattice.
    is_continuous : bool
        If true the Hamiltonian acts on continuous states. If false it acts on
        discrete states.

    **Attributes**

    hamiltonian_operator : list of (np.array of ints, np.array of floats)
        Abstract description of the Hamiltonian. The energy is obtained as
        E = sum_i sum_{t,q} IS(hamiltonian_operator[i][0](t,q))*
                            hamiltonian_operator[i][1](t,q)
        Where IS(hamiltonian_operator[i][0](t,q)) checks if the subcircuit
        hamiltonian_operator[i][0] is appears on the site (t,q) of the circuit
        state.
    dim : int
        Number of dimension of the circuit state on which the Hamiltonian acts,
        i.e. 1 + number of dimensions of the qubits lattice.
    interactions_range : (int,int)
        A tuple with two ints, respectively corresponding to the interaction
        range (the maximum distance between interacting gates of the time-qubits
        lattice) in the time and qubits directions.
    is_continuous : bool
        If true the Hamiltonian acts on continuous states. If false it acts on
        discrete states.

    """

    def __init__(self, hamiltonian_operator, dim, is_continuous):
        self.hamiltonian_operator = compact_hamiltonian(hamiltonian_operator)
        self.dim = dim
        self.is_continuous = is_continuous

        if is_continuous:
            gate_labels_to_ints = continuous_gate_labels_to_ints
        else:
            gate_labels_to_ints = discrete_gate_labels_to_ints
        tmp_ham = []
        for operator, coupling in self.hamiltonian_operator:
            if len(operator.shape) != dim:
                raise ValueError(
                    "The Hamiltonian operators and state must have the same number of dimensions."
                )
            tmp_ham.append(
                (
                    ma.masked_equal(
                        gate_labels_to_ints(operator),
                        gate_labels_to_ints("any"),
                    ),
                    coupling,
                )
            )
        self.hamiltonian_operator = tmp_ham
        self.interactions_range = [
            max(elem[0].shape[ii] for elem in self.hamiltonian_operator) - 1
            for ii in range(self.dim)
        ]

    def get_energy(self, state_vector, position=None):
        """
        Returns the energy associated by the Hamiltonian to a (sub)circuit state.

        **Arguments**

        state_vector : numpy.array of ints
            A vector representing the circuit (or subcircuit) state.
        position : tuple ints or None, optional
            Position  of the first gate of the subcircuit in the
            global circuit state. If None the position is (0,...,0).
            Default is None.

        **Returns**

        energy : float
            The expectation value of the Hamiltonian (infidelity cost).
        """
        if position is None:
            position = [0 for ii in range(self.dim)]
        energy = 0
        vector_shape = np.array(state_vector.shape)
        for operator, coupling in self.hamiltonian_operator:
            op_shape = np.array(operator.shape)
            for site in itertools.product(
                *[range(s) for s in vector_shape - op_shape + 1]
            ):
                if np.ma.allequal(
                    operator,
                    state_vector[
                        tuple(
                            slice(site[i], (site + op_shape)[i])
                            for i in range(self.dim)
                        )
                    ],
                ):
                    energy += coupling[
                        tuple(position[ii] + site[ii] for ii in range(self.dim))
                    ]
        return energy

    def get_energy_diff(self, state_vector, transition):
        """
        Returns the energy difference generated in the circuit by appliyng a rule
        that repleces a subcircuit in a given region.

        **Arguments**

        state_vector : np.array of strings
            A vector representing the circuit state.
        transition : (window, (rule, direction))
            Description of the transition to be applied->
            window : touple of ints
                Region of the circuit where the transition rule applies:
                (t_min,q1_min,q2_min,...,t_max,q1_max,q2_max,... )
            rule : DiscreteMCRule
                Transformation rule to apply.
            direction : bool
                Direction of the transformation rule: True for state_a->state_b,
                False for state_b->state_a.

        **Returns**

        energy_diff : float
            Energy after the transition - energy before the transition.
        transition_instructions : (np array of ints, mask)
            Matrix representing the new subcircuit.
            Where the mask is true, the gate is not raplaced.
        """

        if self.is_continuous:
            mask = np.logical_not(transition[1][0].any_mask)
        else:
            mask = np.logical_not(transition[1][0].masks[0] | transition[1][0].masks[1])

        if transition[1][1]:  # From A to B
            new_local = transition[1][0].state_b
        else:  # From B to A
            new_local = transition[1][0].state_a

        outer_window = [
            max(transition[0][ii] - self.interactions_range[ii], 0)
            for ii in range(self.dim)
        ] + [
            min(
                transition[0][ii]
                + transition[0][ii + self.dim]
                + self.interactions_range[ii],
                state_vector.shape[ii],
            )
            for ii in range(self.dim)
        ]
        local_state_old = state_vector[
            tuple(
                slice(outer_window[ii], outer_window[ii + self.dim] + 1)
                for ii in range(self.dim)
            )
        ]
        local_state_new = np.copy(local_state_old)
        np.putmask(
            local_state_new[
                tuple(
                    slice(
                        transition[0][ii] - outer_window[ii],
                        transition[0][ii]
                        + transition[0][ii + self.dim]
                        - outer_window[ii]
                        + 1,
                    )
                    for ii in range(self.dim)
                )
            ],
            mask,
            new_local,
        )

        energy_diff = self.get_energy(
            local_state_new, position=outer_window[: self.dim]
        ) - self.get_energy(local_state_old, position=outer_window[: self.dim])

        transition_instructions = (new_local, mask)

        return energy_diff, transition_instructions


def unit_test_discrete():
    """
    Compares the energy calculated with a MCHamiltonian on an MCState with the
    energy calculated with an abstract Hamiltonian on a AbstractCircuitState.

    Returns
    -------
    bool
        True if the difference is zero.
    """

    vector = np.array(
        [
            [
                "idle",
                "Z",
                "idle",
                "Z",
                "idle",
                "Z",
                "idle",
                "Z",
                "idle",
                "Z",
                "idle",
                "Z",
                "idle",
                "Z",
                "idle",
                "Z",
            ],
            [
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
            ],
            [
                "CZ",
                "busy",
                "CZ",
                "busy",
                "CZ",
                "busy",
                "CZ",
                "busy",
                "CZ",
                "busy",
                "CZ",
                "busy",
                "CZ",
                "busy",
                "CZ",
                "busy",
            ],
            [
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
                "idle",
                "H",
            ],
            [
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
            ],
        ]
    )

    circuit_state = AbstractCircuitState(vector, "")
    swap_left = 1
    swap_right = 2
    circuit_state.add_swap_area(swap_left, swap_right)
    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, circuit_state.qubits), False),
            np.full(
                np.append(
                    circuit_state.times - swap_right - swap_left, circuit_state.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, circuit_state.qubits), False),
        )
    )

    swap_area_mask = np.logical_not(circuit_area_mask)
    hamiltonian = (
        (np.array([["Z"]]), 0.001, circuit_area_mask),
        (np.array([["H"]]), 0.001, circuit_area_mask),
        (np.array([["idle"]]), 0.001, circuit_area_mask),
        (np.array([["CZ"]]), 0.005, circuit_area_mask),
        (np.array([["SWAP"]]), 0.5, circuit_area_mask),
        (np.array([["CZ", "any", "CZ"]]), 0.05, circuit_area_mask),
        (
            np.array([["CZ", "any", "any", "CZ"]]),
            0.005,
            circuit_area_mask,
        ),
        (
            np.array([["CZ", "any", "any", "any", "CZ"]]),
            0.0005,
            circuit_area_mask,
        ),
        (
            np.full(np.append(1, circuit_state.qubits), "idle"),
            -np.prod(circuit_state.qubits) * 0.001,
            circuit_area_mask,
        ),
        (np.array([["SWAP"]]), 0, swap_area_mask),
        (np.array([["Z"]]), 1, swap_area_mask),
        (np.array([["H"]]), 1, swap_area_mask),
        (np.array([["CZ"]]), 1, swap_area_mask),
    )

    energy_diff = np.abs(
        circuit_state.get_energy(hamiltonian)
        - MCHamiltonian(hamiltonian, circuit_state.dim, False).get_energy(
            DiscreteMCState(circuit_state).vector
        )
    )
    return energy_diff < 10 ** (-15)


def unit_test_continuous():
    """
    Compares the energy calculated with a MCHamiltonian on an MCState with the
    energy calculated with an abstract Hamiltonian on a AbstractCircuitState.

    Returns
    -------
    bool
        True if the difference is zero.
    """

    vector = np.array(
        [
            [
                "idle",
                "RZ",
                "idle",
                "RZ",
                "idle",
                "RZ",
                "idle",
                "RZ",
                "idle",
                "RZ",
                "idle",
                "RZ",
                "idle",
                "RZ",
                "idle",
                "RZ",
            ],
            [
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
            ],
            [
                "CP",
                "busy",
                "CP",
                "busy",
                "CP",
                "busy",
                "CP",
                "busy",
                "CP",
                "busy",
                "CP",
                "busy",
                "CP",
                "busy",
                "CP",
                "busy",
            ],
            [
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
                "idle",
                "RX",
            ],
            [
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
                "SWAP",
                "busy",
            ],
        ]
    )

    rot_amplitudes_array = np.array(
        [
            [
                0,
                1,
                0,
                1,
                0,
                1,
                0,
                1,
                0,
                1,
                0,
                1,
                0,
                1,
                0,
                1,
            ],
            [
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
            ],
            [
                4,
                0,
                4,
                0,
                4,
                0,
                4,
                0,
                4,
                0,
                4,
                0,
                4,
                0,
                4,
                0,
            ],
            [
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
                0,
                2,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ]
    )

    circuit_state = AbstractCircuitState(
        vector, "", rot_amplitudes_array=rot_amplitudes_array
    )

    swap_left = 1
    swap_right = 2
    circuit_state.add_swap_area(swap_left, swap_right)
    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, circuit_state.qubits), False),
            np.full(
                np.append(
                    circuit_state.times - swap_right - swap_left, circuit_state.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, circuit_state.qubits), False),
        )
    )

    swap_area_mask = np.logical_not(circuit_area_mask)
    hamiltonian = (
        (np.array([["RZ"]]), 0.001, circuit_area_mask),
        (np.array([["RX"]]), 0.001, circuit_area_mask),
        (np.array([["idle"]]), 0.001, circuit_area_mask),
        (np.array([["CP"]]), 0.005, circuit_area_mask),
        (np.array([["SWAP"]]), 0.5, circuit_area_mask),
        (np.array([["CP", "any", "CP"]]), 0.05, circuit_area_mask),
        (
            np.array([["CP", "any", "any", "CP"]]),
            0.005,
            circuit_area_mask,
        ),
        (
            np.array([["CP", "any", "any", "any", "CP"]]),
            0.0005,
            circuit_area_mask,
        ),
        (
            np.full(np.append(1, circuit_state.qubits), "idle"),
            -np.prod(circuit_state.qubits) * 0.001,
            circuit_area_mask,
        ),
        (np.array([["SWAP"]]), 0, swap_area_mask),
        (np.array([["RZ"]]), 1, swap_area_mask),
        (np.array([["RX"]]), 1, swap_area_mask),
        (np.array([["CP"]]), 1, swap_area_mask),
    )

    energy_diff = np.abs(
        circuit_state.get_energy(hamiltonian)
        - MCHamiltonian(hamiltonian, circuit_state.dim, True).get_energy(
            ContinuousMCState(circuit_state).vector
        )
    )
    return energy_diff < 10 ** (-15)


if __name__ == "__main__":
    print(unit_test_discrete())
    print(unit_test_continuous())
