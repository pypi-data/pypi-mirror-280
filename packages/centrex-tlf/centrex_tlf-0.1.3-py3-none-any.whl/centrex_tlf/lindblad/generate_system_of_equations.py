from typing import Literal, Tuple, Union, overload

import numpy as np
import numpy.typing as npt
import sympy as smp

from .utils import generate_density_matrix_symbolic

__all__ = ["generate_system_of_equations_symbolic"]


@overload
def generate_system_of_equations_symbolic(
    hamiltonian: smp.matrices.dense.MutableDenseMatrix,
    C_array: npt.NDArray[np.float_],
    fast: bool,
    split_output: Literal[False],
) -> smp.matrices.dense.MutableDenseMatrix:
    ...


@overload
def generate_system_of_equations_symbolic(
    hamiltonian: smp.matrices.dense.MutableDenseMatrix,
    C_array: npt.NDArray[np.float_],
    fast: bool,
) -> smp.matrices.dense.MutableDenseMatrix:
    ...


@overload
def generate_system_of_equations_symbolic(
    hamiltonian: smp.matrices.dense.MutableDenseMatrix,
    C_array: npt.NDArray[np.float_],
    fast: bool,
    split_output: Literal[True],
) -> Tuple[
    smp.matrices.dense.MutableDenseMatrix, smp.matrices.dense.MutableDenseMatrix
]:
    ...


def generate_system_of_equations_symbolic(
    hamiltonian: smp.matrices.dense.MutableDenseMatrix,
    C_array: npt.NDArray[np.float_],
    fast: bool = False,
    split_output: bool = False,
) -> Union[
    smp.matrices.dense.MutableDenseMatrix,
    Tuple[smp.matrices.dense.MutableDenseMatrix, smp.matrices.dense.MutableDenseMatrix],
]:
    n_states = hamiltonian.shape[0]
    ρ = generate_density_matrix_symbolic(n_states)
    C_conj_array = np.einsum("ijk->ikj", C_array.conj())

    matrix_mult_sum = smp.zeros(n_states, n_states)
    if fast:
        # C_array is an array of 2D arrays, where each 2D array only has one
        # entry, i.e. don't have to do the full matrix multiplication each
        # time for C@ρ@Cᶜ, i.e. using manual spare matrix multiplication
        for C, Cᶜ in zip(C_array, C_conj_array):
            idC = np.nonzero(C)
            idCᶜ = np.nonzero(Cᶜ)
            val = C[idC][0] * Cᶜ[idCᶜ][0] * ρ[idC[-1], idCᶜ[0]][0]
            matrix_mult_sum[idC[0][0], idCᶜ[-1][0]] += val

    else:
        for idx in range(C_array.shape[0]):
            matrix_mult_sum[:, :] += C_array[idx] @ ρ @ C_conj_array[idx]

    Cprecalc = np.einsum("ijk,ikl", C_conj_array, C_array)

    a = -0.5 * (Cprecalc @ ρ + ρ @ Cprecalc)
    b = -1j * (hamiltonian @ ρ - ρ @ hamiltonian)

    if split_output:
        return b, matrix_mult_sum + a
    else:
        system = smp.zeros(n_states, n_states)
        system += matrix_mult_sum + a + b
        return system
