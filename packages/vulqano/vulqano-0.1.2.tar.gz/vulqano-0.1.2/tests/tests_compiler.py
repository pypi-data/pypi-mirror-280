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
Specific unit tests for the compiler.
"""

import unittest
from vulqano.rules.abstractdiscreterules import (
    unit_test_2d as discerete_rules_test_2d,
    unit_test_3d as discerete_rules_test_3d,
)
from vulqano.rules.abstractcontinuousrules import (
    unit_test_2d as continuous_rules_test_2d,
    unit_test_3d as continuous_rules_test_3d,
)
from vulqano.hamiltonians.mchamiltonians import (
    unit_test_discrete as mchamiltonian_test_discrete,
)
from vulqano.hamiltonians.mchamiltonians import (
    unit_test_continuous as mchamiltonian_test_continuous,
)
from vulqano.markoviandynamics import unit_test_discrete as discrete_markov_test
from vulqano.markoviandynamics import (
    unit_test_discrete_3d as discrete_markov_test_3d,
)
from vulqano.markoviandynamics import (
    unit_test_continuous as continuous_markov_test,
    unit_test_continuous_3d as continuous_markov_test_3d,
)
from vulqano.quantumdynamics import (
    unit_test as quantum_test,
    unit_test_collapsed as collapsed_quantum_test,
)


class TestRules(unittest.TestCase):
    """
    Execute unit test for the rules generators.
    """

    def test_discrete_rules_2d(self):
        success = discerete_rules_test_2d()
        print("Discrete (1+1)d rules generator test -> ", success)
        self.assertTrue(
            success, "Discrete (1+1)d rules generator did not pass unit tests."
        )

    def test_discrete_rules_3d(self):
        success = discerete_rules_test_3d()
        print("Discrete (1+2)d rules generator test -> ", success)
        self.assertTrue(
            success, "Discrete (1+2)d rules generator did not pass unit tests."
        )

    def test_continuous_rules_2d(self):
        success = continuous_rules_test_2d()
        print("Continuous (1+1)d rules generator test -> ", success)
        self.assertTrue(
            success,
            "Continuous (1+1)d rules generator did not pass unit tests.",
        )

    def test_continuous_rules_3d(self):
        success = continuous_rules_test_3d()
        print("Continuous (1+2)d rules generator test -> ", success)
        self.assertTrue(
            success,
            "Continuous (1+2)d rules generator did not pass unit tests.",
        )


class TestMCHamiltonian(unittest.TestCase):
    """
    Execute unit test for the Marcov Chain Hamiltonians.
    """

    def test_discrete_mc_hamiltonian(self):
        success = mchamiltonian_test_discrete()
        print("Discrete (1+1)d MC Hamiltonian test -> ", success)
        self.assertTrue(
            success, "Discrete (1+1)d MC Hamiltonian did not pass unit tests."
        )

    def test_continuous_mc_hamiltonian(self):
        success = mchamiltonian_test_continuous()
        print("Continuous (1+1)d MC Hamiltonian test -> ", success)
        self.assertTrue(
            success, "Continuous (1+1)d MC Hamiltonian did not pass unit tests."
        )


class TestMarkovianDynamics(unittest.TestCase):
    """
    Execute unit test for the Markovian Dynamics of circuits.
    """

    def test_markovian_dynamics_discrete(self):
        success = discrete_markov_test()
        print("Markovian dynamics of discrete (1+1)d circuit test -> ", success)
        self.assertTrue(
            success,
            "Markovian dynamics of discrete (1+1)d circuit did not pass unit tests.",
        )

    def test_markovian_dynamics_continuous(self):
        success = continuous_markov_test()
        print("Markovian dynamics of continuous (1+1)d circuit test -> ", success)
        self.assertTrue(
            success,
            "Markovian dynamics of continuous (1+1)d circuit did not pass unit tests.",
        )

    def test_markovian_dynamics_discrete_3d(self):
        success = discrete_markov_test_3d()
        print("Markovian dynamics of discrete (1+2)d circuit test -> ", success)
        self.assertTrue(
            success,
            "Markovian dynamics of discrete (1+2)d circuit did not pass unit tests.",
        )

    def test_markovian_dynamics_continuous_3d(self):
        success = continuous_markov_test_3d()
        print("Markovian dynamics of continuous (1+2)d circuit test -> ", success)
        self.assertTrue(
            success,
            "Markovian dynamics of continuous (1+2)d circuit did not pass unit tests.",
        )


class TestQuantumDynamics(unittest.TestCase):
    """
    Execute unit test for the Quantum Dynamics.
    """

    def test_quantum_dynamics(self):
        success = quantum_test()
        print("Quantum dynamics of discrete (1+1)d circuit test -> ", success)
        self.assertTrue(
            success,
            "Quantum dynamics of discrete (1+1)d circuit did not pass unit tests: "
            + "the probability of getting an equivalent circuit is lower than 0.999",
        )

    def test_quantum_dynamics_collapsed(self):
        success = collapsed_quantum_test()
        print("Quantum dynamics of collapsed discrete (1+1)d circuit test -> ", success)
        self.assertTrue(
            success,
            "Quantum dynamics of collapsed discrete (1+1)d circuit did not pass unit tests: "
            + "the probability of getting an equivalent circuit is lower than 0.999",
        )
