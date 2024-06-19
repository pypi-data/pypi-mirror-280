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
Module for reading the qasm file creating a noisy circuit
"""

from ast import literal_eval
import numpy as np


try:
    from qmatchatea.circuit import Qcircuit
except ImportError:
    Qcircuit = None

__all__ = ["read_qasm_function"]


def read_qasm_function(filename, operations):
    """
    Read a qasm file and build a Qcircuit object for the qmatchatea simulation.
    Works only when a single register is there.

    **Arguments**

    filename: str
        Filename of the qasm file to read
    operations: DiscreteOperations
        Operations class to handle the noise

    **Returns**

    Qcircuit
        A Quantum circuit class to run with qmatchatea representing a single
        trajectory
    """

    if Qcircuit is None:
        raise ImportError("Please install qmatchatea.")

    with open(filename, "r") as qfh:
        # Read header
        header = qfh.readline()[:-1].split()
        version = float(header[-1][:-1])
        if not np.isclose(version, 2.0):
            raise ValueError(f"The only QASM version supported is 2.0, not {version}")

        # Read all the includes
        line = qfh.readline()[:-1].split()
        while line[0] == "include":
            line = qfh.readline()[:-1].split()

        # Read the quantum register
        qreg = line[1][:-1].replace("q", "").replace("[", "").replace("]", "")
        num_qubits = int(qreg)

        # Read the classical register
        creg = qfh.readline().replace(";", "").split()
        if creg[0] == "creg":
            _ = int(creg[1][:-1][2])  # Number of bits
            # The circuit starts now
            line = qfh.readline().replace(";", "").split()
        else:
            line = creg

        # Initialization of the circuit
        qcirc = Qcircuit(num_qubits)

        # Cycle over all the lines
        while len(line) > 0:
            # We need this to later add identities where nothing is applied
            filled_idxs = []
            # A comment means a new layer
            while line[0] != "#":
                gate = _read_gate(line)
                qubits = _read_qubits(line)
                filled_idxs += qubits

                # Crosstalk is treated as a gate
                # with its weight as parameter
                # Add the operation to the circuit
                qcirc.add(operations[gate], qubits)

                # Read the new line
                line = qfh.readline().replace(";", "").split()
                if len(line) == 0:
                    break

            # Fill with identities all the empty spaces in the current layer
            if operations.weights_dict["I"] != 0:
                empty_idxs = np.setdiff1d(np.arange(num_qubits), np.array(filled_idxs))
                for qubit in empty_idxs:
                    qcirc.add(operations["i"], [qubit])

            # Read next line in the circuit
            line = qfh.readline().replace(";", "").split()

    return qcirc


def _read_gate(line):
    """
    Read a gate, understanding if it is parametric,
    from a qasm line

    **Arguments**

    line: List[str]
        List of strings. The line where the split() method was called

    **Returns**

    str | Tuple[str, List[float]]
        The gate identifiear and its parameters (if any)
    """
    gate = line[0]

    # The gate is parametric
    if "(" in line[0]:
        gate = gate.split("(")
        # Up to ")", which is the last character
        params = gate[1][:-1].split(",")
        params = [literal_eval(pp) for pp in params]
        gate = (gate[0], params)
    else:
        gate = (gate, [])

    return gate


def _read_qubits(line):
    """
    Read the qubits to which a gate is applied from a qasm line

    **Arguments**

    line: List[str]
        List of strings. The line where the split() method was called

    **Returns**

    List[int]
        The list of qubit indexes
    """
    qubits = "".join(line[1:]).replace("q", "").replace("[", "").replace("]", "")
    qubits = qubits.split(",")
    qubits = [int(qq) for qq in qubits if len(qq) > 0]

    return qubits
