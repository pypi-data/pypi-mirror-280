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
Abstract class for a MarkovChainMonteCarlo.
"""

import random
from itertools import product
import numpy as np
from vulqano.rules.mcrules import (
    generate_discrete_mcrules,
    generate_continuous_mcrules,
)
from vulqano.states.mcstates import DiscreteMCState, ContinuousMCState
from vulqano.hamiltonians.mchamiltonians import (
    MCHamiltonian,
)


__all__ = [
    "MarkovChainMonteCarlo",
]


class ListsGrid(np.ndarray):
    """
    This is a class for the transitions map. Each transition acts with a rule on
    a region [t_min,t_max]*[q1_min,q1_max]*...*[qn_min,qn_max] of the (1+n)-dimensional
    time-qubits lattice. Each region corresponds to a site
    [t_min,q1_min,q2_min,...,t_max,q1_max,q2_max,... ] of a multidimensional numpy
    array. The value fo the site is a list of the transitions acting on the region.
    """

    def __new__(cls, shape):
        obj = super().__new__(
            cls, shape, dtype=object, buffer=None, offset=0, strides=None, order=None
        )
        for region in product(*[range(size) for size in shape]):
            obj[region] = []
        return obj

    def __delitem__(self, key):
        self[key] = []

    def add_element(self, key, element):
        """
        Add a transition to the list at position key.

        **Arguments**

        key : tuple
            Position in the array, corresponding to a window.
        element : list
            Transition rule acting on the window, direction of the rule (True is a->b)

        **Returns**

        None.

        """
        self[key].append(element)

    def random(self):
        """
        Picks an element from the uniform distribution of all the action windows,
        then a random transition actiong on the selected action window.
        The complexity is o(times*qubits/#_allowed_transitions)=
        o(1/average_grid_density)

        **Returns**

        key : tuple
            Random window of the circuit
        value : list
            Random transition acting on the window

        """
        local_transitions = []
        while not local_transitions:
            key = tuple(random.randint(0, size - 1) for size in self.shape)
            local_transitions = self[key]
        value = random.choice(local_transitions)
        return (key, value)


class MarkovChainMonteCarlo:
    """
    Abstract model for a MCMC.

    **Arguments**

    state : AbstractCircuitState
        Initial state of the MC.
    gates : set  of strings
        Set of gates that can be created and destroyed in the transitions.
    hamiltonian : list of (np.array of strings, float, mask)
        Abstract description of the Hamiltonian. The energy is obtained by
        counting how many times each subcircuit hamiltonian_operator[i][0]
        appears on a region A of the circuit suck that that
        hamiltonian_operator[i][2] is True for all (t,q) in A.
        The counted number is multiplied by the weight hamiltonian_operator[i][1].
    rules_classes : str or list of ints, optional
        A list of the ints identifying the rule classes that we want to generate.
        Default is "all" and generates all the rule classes.
    generators : "std" or list of generators, optional
        The list of generators producing the rules to be used. Default is "std",
        in this case a standard list of rules is used.

    **Attributes**

    state : DiscreteMCState or ContinuousMCState
        Current state of of the Marcov chain.
    rules : list of DiscreteMCRule(s) or ContinuousMCRule(s)
        List of all the allowed transition rules.
    transitions_classes_probs : dictionary
        A dictionary associating to each class of rules a probabiilty factor.
        This factor changes the probability by multipling the temperature in the
        Boltzmann distribution.
    max_rule_shape : tuple of ints
        Max number of time steps in rules and qubits in rules for each direction
        of the time-qubit lattice.
    map : dictionary
        A map of all the possible transformations that can be applied to the actual
        circuit state. Each key represents the time steps and qubits window
        identifing the subcircuit to be replaced: (t0, q0, ... t1-t0, q1-q0, ...).
        Each item represents the rule to be applied, the direction of the rule
        (true if ->), and the rule type.
    hamiltonian : MCHamiltonian
        System Hamiltonian for defining the Boltzamann distribution.
    temperature : float
        Temperature of the Boltzamann distribution for the transition probablity.
    """

    def __init__(
        self,
        state,
        gates,
        hamiltonian,
        rules_classes="all",
        generators="std",
    ):
        self.rules = []
        self.transitions_classes_probs = {}

        if state.is_continuous:
            self.state = ContinuousMCState(state)
            rules_generator = generate_continuous_mcrules

        else:
            self.state = DiscreteMCState(state)
            rules_generator = generate_discrete_mcrules

        self.hamiltonian = MCHamiltonian(hamiltonian, state.dim, state.is_continuous)

        for rule in rules_generator(
            gates,
            self.state.vector.ndim,
            rules_classes=rules_classes,
            generators=generators,
        ):
            self.rules.append(rule)
            self.transitions_classes_probs[rule.class_index] = 1

        self.max_rule_shape = tuple(
            max(rule.state_a.shape[ii] for rule in self.rules)
            for ii in range(self.state.dim)
        )
        self.map = ListsGrid(shape=self.state.vector.shape + self.max_rule_shape)
        self.temperature = 1000000
        self.update_map(
            tuple(0 for ii in range(self.state.dim))
            + tuple(size - 1 for size in self.state.vector.shape)
        )

    def apply_boltzmann_transition(self):
        """
        Selects a random transition and applies the transition with probability
        min(1,e^(E_f-E_i)/(T*alpha)), where alpha is a factor depending on the
        transition class (1 by default, time dependent tuning optional) then
        calls the method update() to update the transitions map. The energy
        difference is calculate locally, looking at a subcircuit which includes
        the region of the transition with an additional boundary depending on the
        range of the Hamiltonian.

        **Returns**

        energy_diff: float
            Energy variation generated by the transition.
        last_transition: MCRule
            Last transition applied.
        """

        # Select random element from transitions map
        transition = self.map.random()

        # Accept the transition with boltzmann probability
        energy_diff, transition_instructions = self.hamiltonian.get_energy_diff(
            self.state.vector, transition
        )

        if random.uniform(0, 1) > min(
            np.exp(
                -energy_diff
                / (
                    self.transitions_classes_probs[transition[1][0].class_index]
                    * self.temperature
                )
            ),
            1,
        ):
            return 0, None

        # Increment the transition counter
        if transition[1][1]:  # From A to B
            transition[1][0].counters[0] += 1
        else:  # From B to A
            transition[1][0].counters[1] += 1

        # Update the state
        self.state.transition(
            transition[0][: self.state.dim],
            transition[1][0],
            transition_instructions,
        )

        # Update the map
        self.update_map(transition[0])

        # Return Energy difference and last transition window
        return energy_diff, transition

    def update_map(self, window):
        """
        Updates the transitions map looking at the region where the circuit has
        been updated in the last transition and its boundary.

        **Parameters**

        window : tuple
            Region of the last transition.

        **Returns**

        None.
        """

        # Remove old rules acting on the area of the last transition
        for rule_size in product(*[range(size) for size in self.max_rule_shape]):
            for position in product(
                *[
                    range(
                        max(0, window[ii] - rule_size[ii] - 1),
                        window[ii] + window[self.state.dim + ii] + 1,
                    )
                    for ii in range(self.state.dim)
                ]
            ):
                key = position + rule_size
                del self.map[key]

        # Add new rules acting on the area of the last transition
        for rule in self.rules:
            for position in product(
                *[
                    range(
                        max(0, window[ii] - rule.shape[ii]),
                        window[ii] + window[self.state.dim + ii] + 1,
                    )
                    for ii in range(self.state.dim)
                ]
            ):
                valid_rule, direction = self.state.check_rule(rule, position)
                if valid_rule:
                    self.map.add_element(
                        position + tuple(ii - 1 for ii in rule.shape),
                        (rule, direction),
                    )
