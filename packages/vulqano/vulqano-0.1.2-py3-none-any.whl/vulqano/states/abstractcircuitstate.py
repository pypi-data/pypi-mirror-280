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
Define a class for abstract many-body representation of quantum circuits.

A ciruits is represented by a n-dimensional array of strings, where the first
index labels the time-step, and the other indices label the position of the qubit
in the lattice. Each string denote the name of the corresponding gate
(see vulqano.gates.discretegates and vulqano.gates.discretegates).
"""

import math
from math import pi as PI
from itertools import product
from inspect import getsource
import numpy as np
from numpy import ma
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import colors
from qtealeaves.tooling.hilbert_curvature import hilbert_curve_2d
from vulqano.gates.discretegates import (
    GATES_DICTIONARY as DISCRETE_GATES_DICTIONARY,
)
from vulqano.gates.continuousgates import (
    GATES_DICTIONARY as CONTINUOUS_GATES_DICTIONARY,
)


__all__ = [
    "AbstractCircuitState",
]

plt.ioff()


def hilbert_displacements_2d(n_x, n_y):
    """
    Hilber corve mapping functions for embedding circuits on 2d qubits lattices.
    Returns displacements generating the Hilbert curve for a 2d grid with both
    sides being a power of two.

    **Arguments**

    n_x : int
        Number of sites in x-direction

    n_y : int
        Number of sites in y-direction
    """
    hilbert_map = hilbert_curve_2d(n_x, n_y)
    inverse_hilbert_map = np.zeros((n_x * n_y, 2), dtype=int)
    for idx, linear_index in np.ndenumerate(hilbert_map):
        inverse_hilbert_map[linear_index] = idx
    displacements = inverse_hilbert_map - np.roll(inverse_hilbert_map, 1, axis=0)
    displacements[0] = [0, 0]
    return displacements


def compact_hamiltonian(hamiltonian):
    """
    Transform the Hamiltonian representation.

    **Arguments**

    hamiltonian : list of (np.array of strings, float, mask)
        Abstract description of the Hamiltonian. The energy is obtained by
        counting how many times each subcircuit hamiltonian_operator[i][0]
        appears on a region A of the circuit suck that that
        hamiltonian_operator[i][2] is True for all (t,q) in A.
        The counted number is multiplied by the weight hamiltonian_operator[i][1].

    **Returns**

    hamiltonian_operator_compact :  : list of (np.array of ints, np.array of floats)
        Abstract description of the Hamiltonian. The energy is obtained as
        E = sum_i sum_{t,q} IS(hamiltonian_operator[i][0](t,q))*
                            hamiltonian_operator[i][1](t,q)
        Where IS(hamiltonian_operator[i][0](t,q)) checks if the subcircuit
        hamiltonian_operator[i][0] is appears on the site (t,q) of the circuit
        state.

    """
    hamiltonian_operator_compact = []
    for operator, coupling, mask in hamiltonian:
        first_appearance = True
        for op, couplings_array in hamiltonian_operator_compact:
            if np.array_equal(op, operator):
                couplings_array += coupling * mask
                first_appearance = False
        if first_appearance:
            operator_new = np.empty_like(operator, dtype=object)
            operator_new[:] = operator
            hamiltonian_operator_compact.append((operator_new, coupling * mask))
    return hamiltonian_operator_compact


class AbstractCircuitState:
    """
    Abstract representation of the state of the quantum circuit.

    **Arguments**

    vector : numpy.array of strings
        Array of gates applied at each time and on each qubit. The first index
        correspond to the time step, the other indices label the qubit in the
        lattice.
    name : str
        Circuit name.
    rot_amplitudes_array : np array of float or None.
        A numpy array of float with the same shape of the circuit, where at each
        entry a parameter is specified for the corresponding continuous gate.
        If none the state is a discrete state that can only contain discrete gates.
        Default is None.

    **Attributes**

    vector : numpy.array of strings
        Array of gates applied at each time and on each qubit. The first index
        correspond to the time step, the other indices label the qubit in the
        lattice.
    name : str
        Circuit name.
    times : int
        Number of time steps of the circuit.
    qubits : touple of ints
        Number of qubits in each direction of the lattice.
    is_continuous : bool
        If True the circuit contains continouous gates, False if it contains
        only discrete gates.
    dim : int
        Number of dimension of the circuit state, i.e. 1 + number of dimensions
        of the qubits lattice.
    rot_amplitudes : np array of float.
        A numpy array of float with the same shape of the circuit, where at each
        entry a parameter is specified for the corresponding continuous gate.
        All entries are set to 0 for discrete gates set.
    gates_dictionary : dictionary
        vulqano.gates.discretegates.GATES_DICTIONARY or
        vulqano.gates.continuousgates.GATES_DICTIONARY
    """

    def __init__(self, vector, name, rot_amplitudes_array=None):
        self.vector = vector
        self.name = name
        self.times = vector.shape[0]
        self.qubits = vector.shape[1:]
        self.dim = len(vector.shape)

        if self.dim not in [2, 3]:
            raise ValueError("Only (1+1)d and (1+2)d circuit states are implemented.")

        self.is_continuous = rot_amplitudes_array is not None
        if self.is_continuous:
            if rot_amplitudes_array.shape != vector.shape:
                raise ValueError(
                    "vector and rot_amplitudes_array must have the same array shape."
                )
            self.rot_amplitudes = rot_amplitudes_array % (2 * PI)
            self.gates_dictionary = CONTINUOUS_GATES_DICTIONARY
        else:
            self.rot_amplitudes = np.full(self.vector.shape, 0.0)
            self.gates_dictionary = DISCRETE_GATES_DICTIONARY

    def __str__(self):
        """
        Generates a pictorial representation of the circuit.

        **Returns**

         : str
            A pictorial representation of the circuit.
        """

        if self.is_continuous:
            return (
                "\n"
                + self.name
                + ":\n\n"
                + str(self.vector)
                + ":\n\nRotation amplitudes:\n"
                + str(self.rot_amplitudes)
            )

        return "\n" + self.name + ":\n\n" + str(self.vector)

    def add_swap_area(self, swap_l, swap_r):
        """
        Adds layers of idle gates at the first and last time-steps of the circuit.

        **Arguments**

        swap_l : int
            Number of idle time steps at the beginning of the circuit.
        swap_r : int
            Number of idle time steps at the end of the circuit.

        **Returns**

        self : AbstractCircuitState
            Modified circuit.
        """
        if swap_l <= 0 or swap_r <= 0:
            raise ValueError("swap_l and swap_r must be positive integers.")

        idle_region_l = np.full(np.append(swap_l, self.qubits), "idle")
        idle_region_r = np.full(np.append(swap_r, self.qubits), "idle")
        self.vector = np.concatenate((idle_region_l, self.vector, idle_region_r))

        idle_region_l = np.full(np.append(swap_l, self.qubits), 0)
        idle_region_r = np.full(np.append(swap_r, self.qubits), 0)
        self.rot_amplitudes = np.concatenate(
            (idle_region_l, self.rot_amplitudes, idle_region_r)
        )

        self.times = self.vector.shape[0]
        return self

    def expand(self, distance, idle_block_length):
        """
        Expand the circuit by adding unifomly distrubited blocks of idle time-steps
        at a fixed distance.

        **Arguments**

        distance : int
            Distance between blocks of idle time-steps.
        idle_block_length : int
            Number of time steps in the idle blocks.

        **Returns**

        self : AbstractCircuitState
            Modified circuit.
        """
        if distance <= 0:
            raise ValueError("distance must be a positive.")
        if idle_block_length < 0:
            raise ValueError("idle_block_length must be 0 or a positive.")

        subcirc_list = []
        t_ii = 0
        while t_ii < self.times:
            subcirc_list.append(self.vector[t_ii : t_ii + distance])
            if t_ii + distance < self.times:
                subcirc_list.append(
                    np.full(np.append(idle_block_length, self.qubits), "idle")
                )
            t_ii += distance
        self.vector = np.concatenate(subcirc_list)

        subcirc_list = []
        t_ii = 0
        while t_ii < self.times:
            subcirc_list.append(self.rot_amplitudes[t_ii : t_ii + distance])
            if t_ii + distance < self.times:
                subcirc_list.append(
                    np.full(np.append(idle_block_length, self.qubits), 0)
                )
            t_ii += distance
        self.rot_amplitudes = np.concatenate(subcirc_list)

        self.times += self.vector.shape[0]
        return self

    def get_energy(self, hamiltonian_operator):
        """
        Returns the energy associated to the circuit state by an Hamiltonian
        operator.

        **Arguments**

        hamiltonian_operator : list of (np.array of strings, float, mask)
            Abstract description of the Hamiltonian. The energy is obtained by
            counting how many times each subcircuit hamiltonian_operator[i][0]
            is applied on a site of the circuit state such that
            hamiltonian_operator[i][2](t,q) is True. The counted number is multiplied
            by the weight hamiltonian_operator[i][1].

        **Returns**

        energy : float
            Energy associated to the circuit state by the Hamiltonian operator.
        """
        hamiltonian_operator = compact_hamiltonian(hamiltonian_operator)
        tmp_ham = []
        for operator, coupling in hamiltonian_operator:
            tmp_ham.append((ma.masked_equal(operator, "any"), coupling))
        hamiltonian_operator = tmp_ham
        energy = 0
        vector_shape = np.array(self.vector.shape)
        for operator, coupling in hamiltonian_operator:
            op_shape = np.array(operator.shape)
            for site in product(*[range(s) for s in vector_shape - op_shape + 1]):
                slices = tuple(
                    slice(site[i], (site + op_shape)[i]) for i in range(self.dim)
                )
                if np.ma.allequal(
                    operator,
                    self.vector[slices],
                ):
                    energy += coupling[site]
        return energy

    def make_3d(self):
        """
        Extends the qubit lattice dimension a (1+1)d circuit via Hilbert mapping
        and returns an equivalent (1+2)d circuit.

        **Returns**

        AbstractCircuitState
            (1+2)d circuit
        """
        if self.dim != 2:
            raise ValueError("Only (1+1)d circuits can be extended to (1+2)d circuits.")
        q_base = int(np.log2(self.qubits[0]))

        if abs(np.log2(self.qubits[0]) - q_base) > 1e-14:
            raise ValueError(
                "Number of qubits must be a power of 2 for Hilbert mapping."
            )

        displacements = hilbert_displacements_2d(
            2 ** round(q_base / 2), 2 ** (q_base - round(q_base / 2))
        )

        gates_array_out = np.full(
            (self.times, 2 ** round(q_base / 2), 2 ** (q_base - round(q_base / 2))),
            "idle",
            dtype=object,
        )
        parameters_array_out = np.zeros(
            (self.times, 2 ** round(q_base / 2), 2 ** (q_base - round(q_base / 2)))
        )
        for time in range(self.times):
            site = np.array([0, 0])
            for ii, (d_x, d_y) in enumerate(displacements):
                site += (d_x, d_y)
                gates_array_out[time][site[0], site[1]] = self.vector[time][ii]
                parameters_array_out[time][site[0], site[1]] = self.rot_amplitudes[
                    time
                ][ii]
                if self.vector[time][ii] == "busy":
                    if (d_x, d_y) == (1, 0):
                        gates_array_out[time][site[0] - d_x, site[1] - d_y] += "_r"
                    if (d_x, d_y) == (0, -1):
                        (
                            gates_array_out[time][site[0] - d_x, site[1] - d_y],
                            gates_array_out[time][site[0], site[1]],
                        ) = (
                            gates_array_out[time][site[0], site[1]],
                            gates_array_out[time][site[0] - d_x, site[1] - d_y],
                        )

                        (
                            parameters_array_out[time][site[0] - d_x, site[1] - d_y],
                            parameters_array_out[time][site[0], site[1]],
                        ) = (
                            parameters_array_out[time][site[0], site[1]],
                            parameters_array_out[time][site[0] - d_x, site[1] - d_y],
                        )
                    if (d_x, d_y) == (-1, 0):
                        gates_array_out[time][site[0] - d_x, site[1] - d_y] += "_r"
                        (
                            gates_array_out[time][site[0] - d_x, site[1] - d_y],
                            gates_array_out[time][site[0], site[1]],
                        ) = (
                            gates_array_out[time][site[0], site[1]],
                            gates_array_out[time][site[0] - d_x, site[1] - d_y],
                        )
                        (
                            parameters_array_out[time][site[0] - d_x, site[1] - d_y],
                            parameters_array_out[time][site[0], site[1]],
                        ) = (
                            parameters_array_out[time][site[0], site[1]],
                            parameters_array_out[time][site[0] - d_x, site[1] - d_y],
                        )

        if not self.is_continuous:
            parameters_array_out = None

        return AbstractCircuitState(
            gates_array_out,
            self.name + "_to_3d",
            rot_amplitudes_array=parameters_array_out,
        )

    def to_qasm(self):
        """
        Returns the OPENQASM code for the circuit.

        **Returns**

        openqasm_string : str
            OPENQASM code for the circuit.
        """

        openqasm_string = (
            'OPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q['
            + str(np.prod(self.qubits))
            + "];\n"
        )
        nd_to_1d_map = np.arange(np.prod(self.qubits)).reshape(self.qubits)

        for time in range(self.times):
            if "\n\n" != openqasm_string[-2:]:
                openqasm_string += "\n"
            for qubit_position in product(*[range(size) for size in self.qubits]):
                gate = self.vector[time][qubit_position]
                if gate in self.gates_dictionary:
                    if self.gates_dictionary[gate]["Qasm"] is not None:
                        control_qubit = nd_to_1d_map[qubit_position]
                        connectivity = self.gates_dictionary[gate]["Connectivity"]
                        connectivity = [
                            0 for ii in range(self.dim - len(connectivity) - 1)
                        ] + connectivity
                        target_qubit = nd_to_1d_map[
                            tuple(
                                qubit_position[ii] + connectivity[ii]
                                for ii in range(self.dim - 1)
                            )
                        ]
                        openqasm_string += self.gates_dictionary[gate]["Qasm"](
                            self.rot_amplitudes[time][qubit_position],
                            control_qubit,
                            target_qubit,
                        )
                else:
                    raise ValueError(
                        "Gate " + str(gate) + " not defined in gates dictionary"
                    )
        return openqasm_string

    def draw(
        self,
        filename,
        ncols=1,
    ):
        """
        Draw a figure representing the circuit as the state of a lattice.

        **Arguments**

        filename : str
            Name of the file, path and extension included.
        ncols : int, optional
            Number of columns in kegend. If 0, no legend is plotted.

        **Returns**

        None.
        """

        circuit_state_vector = np.copy(self.vector)
        rot_amplitudes_vector = np.copy(self.rot_amplitudes)

        # Add empty time steps to fit subplots into a rectangle
        if self.dim == 3:
            rows = int(circuit_state_vector.shape[0] ** (0.5))
            cols = math.ceil(circuit_state_vector.shape[0] / rows)
            new_steps = rows * cols - circuit_state_vector.shape[0]
            circuit_state_vector = np.concatenate(
                (
                    circuit_state_vector,
                    np.full(np.append(new_steps, self.qubits), "idle"),
                )
            )
            rot_amplitudes_vector = np.concatenate(
                (rot_amplitudes_vector, np.full(np.append(new_steps, self.qubits), 0))
            )

        rgb_array = np.zeros(np.append(circuit_state_vector.shape, 3))
        for site in product(*[range(s) for s in circuit_state_vector.shape]):
            rgb_array[site] = self.gates_dictionary[circuit_state_vector[site]][
                "Color"
            ](rot_amplitudes_vector[site])
        plt.rcParams["figure.dpi"] = 500

        if self.dim == 2:
            fig, ax_1 = plt.subplots()
            ax_1.imshow(np.transpose(rgb_array, (1, 0, 2)))
            ax_1.set_xlabel("$t$")
            ax_1.set_ylabel("$q$")
            ax_1.set_xticks(range(0, rgb_array.shape[0], 5))
            ax_1.set_xticklabels(range(0, rgb_array.shape[0], 5), fontsize=6)
            ax_1.set_yticks(range(0, rgb_array.shape[1]))
            ax_1.set_yticklabels(range(0, rgb_array.shape[1]), fontsize=6)

        elif self.dim == 3:
            rows = int(circuit_state_vector.shape[0] ** (0.5))
            cols = math.ceil(circuit_state_vector.shape[0] / rows)
            fig, axs = plt.subplots(rows, cols)
            for ii, jj in product(range(rows), range(cols)):
                nn = ii + rows * jj
                axs[ii, jj].imshow(np.transpose(rgb_array[nn], (1, 0, 2)))
                axs[ii, jj].set_title("t=" + str(nn), fontsize=6)
                axs[ii, jj].xaxis.set_tick_params(labelbottom=False)
                axs[ii, jj].yaxis.set_tick_params(labelleft=False)
                axs[ii, jj].set_xticks([])
                axs[ii, jj].set_yticks([])

        else:
            raise ValueError(
                "Circuit drawing implemented only for (1+1)d and (2+1)d circuits."
            )

        if ncols > 0:
            involved_gates = set()
            for gate in self.gates_dictionary:
                if np.count_nonzero(self.vector == gate) > 0:
                    involved_gates.add(gate)

            gate_colors = []
            gate_labels = []
            for gate in involved_gates:
                if (
                    not self.is_continuous
                    or not self.gates_dictionary[gate]["is_parametric"]
                ):
                    gate_colors.append(self.gates_dictionary[gate]["Color"](0))
                    gate_labels.append(("$" + gate + "$").replace("dg", r"^\dag"))
            sorter = np.array(gate_labels).argsort()
            gate_colors = np.array(gate_colors)[sorter]
            gate_labels = np.array(gate_labels)[sorter]
            plt.figlegend(
                handles=[
                    mpatches.Patch(label=label, edgecolor="black", facecolor=color)
                    for color, label in zip(gate_colors, gate_labels)
                ],
                handlelength=1,
                handleheight=1,
                bbox_to_anchor=[0.9, 0.5],
                loc="center left",
                ncol=ncols,
            )

            if self.is_continuous:
                parametric_legend_instructions = []
                for gate in involved_gates:
                    if self.gates_dictionary[gate]["is_parametric"]:
                        # Extract colormap name from lambda function
                        lambda_source = getsource(self.gates_dictionary[gate]["Color"])
                        sub1 = 'get_cmap("'
                        sub2 = '")'
                        cmap_name = lambda_source[
                            lambda_source.index(sub1)
                            + len(sub1) : lambda_source.index(sub2)
                        ]

                        parametric_legend_instructions.append(
                            ("$" + gate + "$", cmap_name)
                        )

                fig.subplots_adjust(bottom=0.1)
                delta = 0.9 / (6 * len(parametric_legend_instructions))
                n_ticks = 3
                norm = mpl.colors.Normalize(vmin=0, vmax=2 * PI)

                for ii, (gate_name, cmap_name) in enumerate(
                    parametric_legend_instructions
                ):
                    cbar_ax_1 = fig.add_axes(
                        [0.05 + delta + ii * 6 * delta, 0, 5 * delta, 0.05]
                    )
                    cmap = plt.get_cmap(cmap_name, 100 * n_ticks)
                    cmap = colors.LinearSegmentedColormap.from_list(
                        cmap.name,
                        cmap(
                            np.concatenate(
                                (np.linspace(0.25, 1, 100), np.linspace(1, 0.25, 100))
                            )
                        ),
                    )
                    scalar_mappable = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
                    scalar_mappable.set_array([])
                    cbar = fig.colorbar(
                        scalar_mappable,
                        ticks=np.round(np.linspace(0, 2 * PI, n_ticks), 2),
                        boundaries=np.linspace(0, 2 * PI, 100 * n_ticks),
                        orientation="horizontal",
                        cax=cbar_ax_1,
                    )
                    cbar.ax.set_title(gate_name, fontsize=10)
                    cbar.ax.tick_params(labelsize=6)
                    cbar.ax.set_xticklabels(["$0$", r"$\pi$", r"$2\pi$"])

        fig.suptitle(self.name)
        plt.savefig(filename + ".pdf", bbox_inches="tight")
        plt.close(fig)


def test_discrete():
    """
    Test state creation, energy calculation, qasm generation, and drawing of a
    non-paramateric circuit.


    Returns
    -------
    None.
    """
    input_circuit = AbstractCircuitState(
        np.array(
            [
                ["SWAP", "busy", "CZ", "busy"],
                ["Z", "Z", "Z", "idle"],
                ["CZ", "busy", "CZ", "busy"],
                ["idle", "idle", "Z", "idle"],
            ]
        ),
        "input_circuit",
    )

    print(input_circuit)

    swap_left, swap_right = (3, 2)
    input_circuit.expand(2, 1)
    input_circuit.add_swap_area(swap_left, swap_right)
    print(input_circuit)

    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, input_circuit.qubits), False),
            np.full(
                np.append(
                    input_circuit.times - swap_right - swap_left, input_circuit.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, input_circuit.qubits), False),
        )
    )
    machine = {
        "gates": {"Z", "H", "CZ", "SWAP"},
        "hamiltonian": (
            (np.array([["Z"]]), 0.001, circuit_area_mask),
            (np.array([["H"]]), 0.001, circuit_area_mask),
            (np.array([["idle"]]), 0.001, circuit_area_mask),
            (np.array([["CZ"]]), 0.005, circuit_area_mask),
            (np.array([["SWAP"]]), 1, circuit_area_mask),
            (np.array([["CZ", "any", "CZ"]]), 0.5, circuit_area_mask),
            (
                np.array([["CZ", "any", "any", "CZ"]]),
                0.05,
                circuit_area_mask,
            ),
            (
                np.full(np.append(1, input_circuit.qubits), "idle"),
                -np.prod(input_circuit.qubits) * 0.001,
                circuit_area_mask,
            ),
        ),
    }
    print("\nEnergy -> ", input_circuit.get_energy(machine["hamiltonian"]), "\n")

    print(input_circuit.to_qasm())

    input_circuit.draw("discerete_circuit_draw_test")


def test_discrete_2d():
    """
    Test state creation, energy calculation, qasm generation, and drawing of a
    non-paramateric circuit.


    Returns
    -------
    None.
    """
    input_circuit = AbstractCircuitState(
        np.array(
            [
                [["SWAP", "busy"], ["idle", "idle"], ["CZ", "busy"], ["idle", "H"]],
                [["Z", "idle"], ["Z", "idle"], ["CZ_r", "idle"], ["busy", "Z"]],
                [["CZ", "busy"], ["Z", "idle"], ["CZ", "busy"], ["Z", "idle"]],
                [["idle", "idle"], ["idle", "Z"], ["Z", "idle"], ["idle", "idle"]],
            ]
        ),
        "input_circuit",
    )

    print(input_circuit)

    swap_left, swap_right = (3, 2)
    input_circuit.expand(2, 1)
    input_circuit.add_swap_area(swap_left, swap_right)
    print(input_circuit)

    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, input_circuit.qubits), False),
            np.full(
                np.append(
                    input_circuit.times - swap_right - swap_left, input_circuit.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, input_circuit.qubits), False),
        )
    )
    machine = {
        "gates": {"Z", "H", "CZ", "SWAP"},
        "hamiltonian": (
            (np.array([[["Z"]]]), 0.001, circuit_area_mask),
            (np.array([[["H"]]]), 0.001, circuit_area_mask),
            (np.array([[["idle"]]]), 0.001, circuit_area_mask),
            (np.array([[["CZ"]]]), 0.005, circuit_area_mask),
            (np.array([[["SWAP"]]]), 1, circuit_area_mask),
            (np.array([[["CZ", "any", "CZ"]]]), 0.5, circuit_area_mask),
            (np.array([[["CZ"], ["any"], ["CZ"]]]), 0.5, circuit_area_mask),
            (
                np.array([[["CZ", "any", "any", "CZ"]]]),
                0.05,
                circuit_area_mask,
            ),
            (
                np.array([[["CZ"], ["any"], ["any"], ["CZ"]]]),
                0.05,
                circuit_area_mask,
            ),
            (
                np.full(np.append(1, input_circuit.qubits), "idle"),
                -np.prod(input_circuit.qubits) * 0.001,
                circuit_area_mask,
            ),
        ),
    }
    print("\nEnergy -> ", input_circuit.get_energy(machine["hamiltonian"]), "\n")

    print(input_circuit.to_qasm())

    input_circuit.draw("discerete_2d_circuit_draw_test")


def test_continuous():
    """
    Test state creation, energy calculation, qasm generation, and drawing of a
    paramateric circuit.


    Returns
    -------
    None.
    """

    input_circuit = AbstractCircuitState(
        np.array(
            [
                ["SWAP", "busy", "CP", "busy"],
                ["RX", "RZ", "RX", "idle"],
                ["CP", "busy", "CP", "busy"],
                ["idle", "idle", "RZ", "idle"],
            ]
        ),
        "input_circuit",
        rot_amplitudes_array=np.array(
            [
                [0, 0, 2, 0],
                [0.5, 1, 7, 0],
                [5, 0, 2, 0],
                [0, 0, 1, 0],
            ]
        ),
    )

    print(input_circuit)

    swap_left, swap_right = (3, 2)
    input_circuit.expand(2, 1)
    input_circuit.add_swap_area(swap_left, swap_right)
    print(input_circuit)

    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, input_circuit.qubits), False),
            np.full(
                np.append(
                    input_circuit.times - swap_right - swap_left, input_circuit.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, input_circuit.qubits), False),
        )
    )
    machine = {
        "gates": {"RX", "RZ", "CP", "SWAP"},
        "hamiltonian": (
            (np.array([["RX"]]), 0.001, circuit_area_mask),
            (np.array([["RZ"]]), 0.001, circuit_area_mask),
            (np.array([["idle"]]), 0.001, circuit_area_mask),
            (np.array([["CP"]]), 0.005, circuit_area_mask),
            (np.array([["CP"]]), 0.005, circuit_area_mask),
            (np.array([["SWAP"]]), 1, circuit_area_mask),
            (np.array([["CP", "any", "CP"]]), 0.5, circuit_area_mask),
            (np.array([["CP", "any", "any", "CP"]]), 0.05, circuit_area_mask),
            (
                np.full(np.append(1, input_circuit.qubits), "idle"),
                -np.prod(input_circuit.qubits) * 0.001,
                circuit_area_mask,
            ),
        ),
    }
    print("\nEnergy -> ", input_circuit.get_energy(machine["hamiltonian"]), "\n")

    print(input_circuit.to_qasm())

    input_circuit.draw("continuous_circuit_draw_test")


def test_continuous_2d():
    """
    Test state creation, energy calculation, qasm generation, and drawing of a
    paramateric circuit.


    Returns
    -------
    None.
    """

    input_circuit = AbstractCircuitState(
        np.array(
            [
                [["SWAP", "busy"], ["idle", "idle"], ["CP", "busy"], ["idle", "idle"]],
                [["RX", "idle"], ["RZ", "idle"], ["RX", "idle"], ["idle", "idle"]],
                [["CP", "busy"], ["idle", "idle"], ["CP_r", "idle"], ["busy", "idle"]],
                [["idle", "idle"], ["idle", "idle"], ["RZ", "idle"], ["idle", "idle"]],
            ]
        ),
        "input_circuit",
        rot_amplitudes_array=np.array(
            [
                [[0, 0], [0, 0], [2, 0], [0, 0]],
                [[2, 0], [1, 0], [7, 0], [0, 0]],
                [[5, 0], [0, 0], [2, 0], [0, 0]],
                [[0, 0], [0, 0], [1, 0], [0, 0]],
            ]
        ),
    )

    print(input_circuit)

    swap_left, swap_right = (3, 2)
    input_circuit.expand(2, 1)
    input_circuit.add_swap_area(swap_left, swap_right)
    print(input_circuit)

    circuit_area_mask = np.concatenate(
        (
            np.full(np.append(swap_left, input_circuit.qubits), False),
            np.full(
                np.append(
                    input_circuit.times - swap_right - swap_left, input_circuit.qubits
                ),
                True,
            ),
            np.full(np.append(swap_right, input_circuit.qubits), False),
        )
    )
    machine = {
        "gates": {"RX", "RZ", "CP", "SWAP"},
        "hamiltonian": (
            (np.array([[["RX"]]]), 0.001, circuit_area_mask),
            (np.array([[["RZ"]]]), 0.001, circuit_area_mask),
            (np.array([[["idle"]]]), 0.001, circuit_area_mask),
            (np.array([[["CP"]]]), 0.005, circuit_area_mask),
            (np.array([[["CP"]]]), 0.005, circuit_area_mask),
            (np.array([[["SWAP"]]]), 1, circuit_area_mask),
            (np.array([[["CP", "any", "CP"]]]), 0.5, circuit_area_mask),
            (np.array([[["CP", "any", "any", "CP"]]]), 0.05, circuit_area_mask),
            (
                np.full(np.append(1, input_circuit.qubits), "idle"),
                -np.prod(input_circuit.qubits) * 0.001,
                circuit_area_mask,
            ),
        ),
    }
    print("\nEnergy -> ", input_circuit.get_energy(machine["hamiltonian"]), "\n")

    print(input_circuit.to_qasm())

    input_circuit.draw("continuous_circuit_2d_draw_test")


def test_hilbert_mapping():
    """
    Test the dimensional extension via Hilbert mapping.


    Returns
    -------
    None.
    """

    input_circuit = AbstractCircuitState(
        np.array(
            [
                ["SWAP", "busy", "CP", "busy", "SWAP", "busy", "CP", "busy"],
                ["RX", "RZ", "RX", "idle", "RX", "RZ", "RX", "idle"],
                ["idle", "CP", "busy", "CP", "busy", "CP", "busy", "idle"],
                ["idle", "SWAP", "busy", "CP", "busy", "SWAP", "busy", "RZ"],
            ]
        ),
        "input_circuit",
        rot_amplitudes_array=np.array(
            [
                [0, 0, 2, 0, 0, 0, 2, 0],
                [0.2, 0.1, 7, 0, 0.2, 0.1, 7, 0],
                [0, 5, 0, 2, 0, 5, 0, 0],
                [0, 0, 0, 2, 0, 0, 0, 1],
            ]
        ),
    )

    input_circuit.draw("input_2d")

    output_circuit = input_circuit.make_3d()
    for idx, gate in np.ndenumerate(output_circuit.vector):
        if not CONTINUOUS_GATES_DICTIONARY[gate]["is_parametric"]:
            if output_circuit.rot_amplitudes[idx] != 0:
                print(output_circuit)
                raise ValueError(
                    "Non zero parameter associated to a non-parametric gate at size "
                    + str(idx)
                    + " of the circuit state:"
                    + str(output_circuit)
                )

    print(output_circuit.to_qasm())
    output_circuit.draw("output_3d")


if __name__ == "__main__":
    test_discrete()
    test_continuous()
    test_discrete_2d()
    test_continuous_2d()
    test_hilbert_mapping()
