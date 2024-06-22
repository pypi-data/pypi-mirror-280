# Copyright 2011-2017 Kwant authors.
#
# This file is part of Kwant.  It is subject to the license terms in the file
# LICENSE.rst found in the top-level directory of this distribution and at
# https://kwant-project.org/license.  A list of Kwant authors can be found in
# the file AUTHORS.rst at the top-level directory of this distribution and at
# https://kwant-project.org/authors.

"""Low-level access to LAPACK functions. """

__all__ = ['trsen',
           'trevc',
           'tgsen',
           'tgevc',
           'prepare_for_lapack']

from itertools import compress

import numpy as np
cimport numpy as np

cimport scipy.linalg.cython_lapack as lapack

ctypedef int l_int
ctypedef bint l_logical

int_dtype = np.int32
logical_dtype = np.int32

ctypedef float complex float_complex
ctypedef double complex double_complex

ctypedef fused scalar:
    float
    double
    float complex
    double complex

ctypedef fused single_precision:
    float
    float complex

ctypedef fused double_precision:
    double
    double complex

ctypedef fused cmplx:
    float complex
    double complex

ctypedef fused floating:
    float
    double

# exceptions

class LinAlgError(RuntimeError):
    pass


# some helper functions
def assert_fortran_mat(*mats):
    # This is a workaround for a bug in NumPy version < 2.0,
    # where 1x1 matrices do not have the F_Contiguous flag set correctly.
    for mat in mats:
        if (mat is not None and (mat.shape[0] > 1 or mat.shape[1] > 1) and
            not mat.flags["F_CONTIGUOUS"]):
            raise ValueError("Input matrix must be Fortran contiguous")


cdef np.ndarray maybe_complex(scalar selector,
                              np.ndarray real, np.ndarray imag):
    cdef np.ndarray r
    r = real
    if scalar in floating:
        if imag.nonzero()[0].size:
            r = real + 1j * imag
    return r


cdef l_int lwork_from_qwork(scalar qwork):
    if scalar in floating:
        return <l_int>qwork
    else:
        return <l_int>qwork.real


def trsen(np.ndarray[l_logical] select,
          np.ndarray[scalar, ndim=2] T,
          np.ndarray[scalar, ndim=2] Q,
          calc_ev=True):
    cdef l_int N, M, lwork, liwork, qiwork, info

    assert_fortran_mat(T, Q)

    # Allocate workspaces

    N = T.shape[0]

    cdef np.ndarray[scalar] wr, wi
    if scalar in cmplx:
        wr = np.empty(N, dtype=T.dtype)
        wi = None
    else:
        wr = np.empty(N, dtype=T.dtype)
        wi = np.empty(N, dtype=T.dtype)

    cdef char *compq
    cdef scalar *q_ptr
    if Q is not None:
        compq = "V"
        q_ptr = <scalar *>Q.data
    else:
        compq = "N"
        q_ptr = NULL

    # Workspace query
    # Xtrsen expects &qwork as a <scalar *> (even though it's an integer)
    cdef scalar qwork
    lwork = liwork = -1

    if scalar is float:
        lapack.strsen("N", compq, <l_logical *>select.data,
                      &N, <float *>T.data, &N, q_ptr, &N,
                      <float *>wr.data, <float *>wi.data, &M, NULL, NULL,
                      &qwork, &lwork, &qiwork, &liwork, &info)
    elif scalar is double:
        lapack.dtrsen("N", compq, <l_logical *>select.data,
                      &N, <double *>T.data, &N, q_ptr, &N,
                      <double *>wr.data, <double *>wi.data, &M, NULL, NULL,
                      &qwork, &lwork, &qiwork, &liwork, &info)
    elif scalar is float_complex:
        lapack.ctrsen("N", compq, <l_logical *>select.data,
                      &N, <float complex *>T.data, &N, q_ptr, &N,
                      <float complex *>wr.data, &M, NULL, NULL,
                      &qwork, &lwork, &info)
    elif scalar is double_complex:
        lapack.ztrsen("N", compq, <l_logical *>select.data,
                      &N, <double complex *>T.data, &N, q_ptr, &N,
                      <double complex *>wr.data, &M, NULL, NULL,
                      &qwork, &lwork, &info)

    assert info == 0, "Argument error in trsen"

    lwork = lwork_from_qwork(qwork)
    cdef np.ndarray[scalar] work = np.empty(lwork, dtype=T.dtype)

    cdef np.ndarray[l_int] iwork = None
    if scalar in floating:
        liwork = qiwork
        iwork = np.empty(liwork, dtype=int_dtype)

    # Tha actual calculation

    if scalar is float:
        lapack.strsen("N", compq, <l_logical *>select.data,
                      &N, <float *>T.data, &N, q_ptr, &N,
                      <float *>wr.data, <float *>wi.data, &M, NULL, NULL,
                      <float *>work.data, &lwork,
                      <l_int *>iwork.data, &liwork, &info)
    elif scalar is double:
        lapack.dtrsen("N", compq, <l_logical *>select.data,
                      &N, <double *>T.data, &N, q_ptr, &N,
                      <double *>wr.data, <double *>wi.data, &M, NULL, NULL,
                      <double *>work.data, &lwork,
                      <l_int *>iwork.data, &liwork, &info)
    elif scalar is float_complex:
        lapack.ctrsen("N", compq, <l_logical *>select.data,
                      &N, <float complex *>T.data, &N, q_ptr, &N,
                      <float complex *>wr.data, &M, NULL, NULL,
                      <float complex *>work.data, &lwork, &info)
    elif scalar is double_complex:
        lapack.ztrsen("N", compq, <l_logical *>select.data,
                      &N, <double complex *>T.data, &N, q_ptr, &N,
                      <double complex *>wr.data, &M, NULL, NULL,
                      <double complex *>work.data, &lwork, &info)

    if info > 0:
        raise LinAlgError("Reordering failed; problem is very ill-conditioned")

    assert info == 0, "Argument error in trsen"

    # Real inputs possibly produce complex output
    cdef np.ndarray w = maybe_complex[scalar](0, wr, wi)

    return tuple(compress((T, Q, w), (True, Q is not None, calc_ev)))


# Helper function for xTREVC and xTGEVC
def txevc_postprocess(dtype, T, vreal, np.ndarray[l_logical] select):
    cdef int N, M, i, m, indx

    N = T.shape[0]
    if select is None:
        select = np.ones(N, dtype = logical_dtype)
    selindx = select.nonzero()[0]
    M = selindx.size

    v = np.empty((N, M), dtype = dtype, order='F')

    indx = 0
    for m in range(M):
        k = selindx[m]

        if k < N-1 and T[k+1,k]:
            # we have the situation of a 2x2 block, and
            # the eigenvalue with the positive imaginary part desired
            v[:, m] = vreal[:, indx] + 1j * vreal[:, indx + 1]

            # Check if the eigenvalue with negative real part is also
            # selected, if it is, we need the same entries in vr
            if not select[k+1]:
                indx += 2
        elif k > 0 and T[k,k-1]:
            # we have the situation of a 2x2 block, and
            # the eigenvalue with the negative imaginary part desired
            v[:, m] = vreal[:, indx] - 1j * vreal[:, indx + 1]

            indx += 2
        else:
            # real eigenvalue
            v[:, m] = vreal[:, indx]

            indx += 1
    return v


def trevc(np.ndarray[scalar, ndim=2] T,
          np.ndarray[scalar, ndim=2] Q,
          np.ndarray[l_logical] select,
          left=False, right=True):
    cdef l_int N, info, M, MM
    cdef char *side
    cdef char *howmny

    # Parameter checks

    if (T.shape[0] != T.shape[1] or Q.shape[0] != Q.shape[1]
        or T.shape[0] != Q.shape[0]):
        raise ValueError("Invalid Schur decomposition as input")

    assert_fortran_mat(T, Q)

    # Workspace allocation

    N = T.shape[0]

    cdef np.ndarray[scalar] work
    if scalar in floating:
        work = np.empty(4 * N, dtype=T.dtype)
    else:
        work = np.empty(2 * N, dtype=T.dtype)

    cdef np.ndarray rwork = None
    if scalar is float_complex:
        rwork = np.empty(N, dtype=np.float32)
    elif scalar is double_complex:
        rwork = np.empty(N, dtype=np.float64)

    if left and right:
        side = "B"
    elif left:
        side = "L"
    elif right:
        side = "R"
    else:
        return

    cdef np.ndarray[l_logical] select_cpy
    cdef l_logical *select_ptr
    if select is not None:
        howmny = "S"
        MM = select.nonzero()[0].size
        # Correct for possible additional storage if a single complex
        # eigenvalue is selected.
        # For that: Figure out the positions of the 2x2 blocks.
        cmplxindx = np.diagonal(T, -1).nonzero()[0]
        for i in cmplxindx:
            if bool(select[i]) != bool(select[i+1]):
                MM += 1

        # Select is overwritten in strevc.
        select_cpy = np.array(select, dtype = logical_dtype,
                              order = 'F')
        select_ptr = <l_logical *>select_cpy.data
    else:
        MM = N
        select_ptr = NULL
        if Q is not None:
            howmny = "B"
        else:
            howmny = "A"

    cdef np.ndarray[scalar, ndim=2] vl_r = None
    cdef scalar *vl_r_ptr
    if left:
        if Q is not None and select is None:
            vl_r = np.asfortranarray(Q.copy())
        else:
            vl_r = np.empty((N, MM), dtype=T.dtype, order='F')
        vl_r_ptr = <scalar *>vl_r.data
    else:
        vl_r_ptr = NULL

    cdef np.ndarray[scalar, ndim=2]  vr_r = None
    cdef scalar *vr_r_ptr
    if right:
        if Q is not None and select is None:
            vr_r = np.asfortranarray(Q.copy())
        else:
            vr_r = np.empty((N, MM), dtype=T.dtype, order='F')
        vr_r_ptr = <scalar *>vr_r.data
    else:
        vr_r_ptr = NULL

    # The actual calculation

    if scalar is float:
        lapack.strevc(side, howmny, select_ptr,
                      &N, <float *>T.data, &N,
                      vl_r_ptr, &N, vr_r_ptr, &N, &MM, &M,
                      <float *>work.data, &info)
    elif scalar is double:
        lapack.dtrevc(side, howmny, select_ptr,
                      &N, <double *>T.data, &N,
                      vl_r_ptr, &N, vr_r_ptr, &N, &MM, &M,
                      <double *>work.data, &info)
    elif scalar is float_complex:
        lapack.ctrevc(side, howmny, select_ptr,
                      &N, <float complex *>T.data, &N,
                      vl_r_ptr, &N, vr_r_ptr, &N, &MM, &M,
                      <float complex *>work.data, <float *>rwork.data, &info)
    elif scalar is double_complex:
        lapack.ztrevc(side, howmny, select_ptr,
                      &N, <double complex *>T.data, &N,
                      vl_r_ptr, &N, vr_r_ptr, &N, &MM, &M,
                      <double complex *>work.data, <double *>rwork.data, &info)

    assert info == 0, "Argument error in trevc"
    assert MM == M, "Unexpected number of eigenvectors returned in strevc"

    if select is not None and Q is not None:
        if left:
            vl_r = np.asfortranarray(np.dot(Q, vl_r))
        if right:
            vr_r = np.asfortranarray(np.dot(Q, vr_r))

    cdef np.ndarray vl, vr
    if left:
        vl = vl_r
    if right:
        vr = vr_r
    if scalar in floating:
        # If there are complex eigenvalues, we need to postprocess the
        # eigenvectors.
        if scalar is float:
            dtype = np.complex64
        else:
            dtype = np.complex128
        if np.diagonal(T, -1).nonzero()[0].size:
            if left:
                vl = txevc_postprocess(dtype, T, vl_r, select)
            if right:
                vr = txevc_postprocess(dtype, T, vr_r, select)

    if left and right:
        return (vl, vr)
    elif left:
        return vl
    else:
        return vr


def tgsen(np.ndarray[l_logical] select,
           np.ndarray[scalar, ndim=2] S,
           np.ndarray[scalar, ndim=2] T,
           np.ndarray[scalar, ndim=2] Q,
           np.ndarray[scalar, ndim=2] Z,
           calc_ev=True):
    cdef l_int ijob = 0
    cdef l_int N, M, lwork, liwork, info

    # Check parameters

    if ((S.shape[0] != S.shape[1] or T.shape[0] != T.shape[1] or
         S.shape[0] != T.shape[0]) or
        (Q is not None and (Q.shape[0] != Q.shape[1] or
                            S.shape[0] != Q.shape[0])) or
        (Z is not None and (Z.shape[0] != Z.shape[1] or
                            S.shape[0] != Z.shape[0]))):
        raise ValueError("Invalid Schur decomposition as input")

    assert_fortran_mat(S, T, Q, Z)

    # Allocate workspaces

    N = S.shape[0]

    cdef np.ndarray[scalar] alphar, alphai
    if scalar in cmplx:
        alphar = np.empty(N, dtype=S.dtype)
        alphai = None
    else:
        alphar = np.empty(N, dtype=S.dtype)
        alphai = np.empty(N, dtype=S.dtype)

    cdef np.ndarray[scalar] beta
    beta = np.empty(N, dtype=S.dtype)

    cdef l_logical wantq
    cdef scalar *q_ptr
    if Q is not None:
        wantq = 1
        q_ptr = <scalar *>Q.data
    else:
        wantq = 0
        q_ptr = NULL

    cdef l_logical wantz
    cdef scalar *z_ptr
    if Z is not None:
        wantz = 1
        z_ptr = <scalar *>Z.data
    else:
        wantz = 0
        z_ptr = NULL

    # Workspace query
    # Xtgsen expects &qwork as a <scalar *> (even though it's an integer)
    lwork = -1
    liwork = -1
    cdef scalar qwork
    cdef l_int qiwork

    if scalar is float:
        lapack.stgsen(&ijob, &wantq, &wantz, <l_logical *>select.data,
                      &N, <float *>S.data, &N,
                      <float *>T.data, &N,
                      <float *>alphar.data, <float *>alphai.data,
                      <float *>beta.data,
                      q_ptr, &N, z_ptr, &N, &M, NULL, NULL, NULL,
                      &qwork, &lwork, &qiwork, &liwork, &info)
    elif scalar is double:
        lapack.dtgsen(&ijob, &wantq, &wantz, <l_logical *>select.data,
                      &N, <double *>S.data, &N,
                      <double *>T.data, &N,
                      <double *>alphar.data, <double *>alphai.data,
                      <double *>beta.data,
                      q_ptr, &N, z_ptr, &N, &M, NULL, NULL, NULL,
                      &qwork, &lwork, &qiwork, &liwork, &info)
    elif scalar is float_complex:
        lapack.ctgsen(&ijob, &wantq, &wantz, <l_logical *>select.data,
                      &N, <float complex *>S.data, &N,
                      <float complex *>T.data, &N,
                      <float complex *>alphar.data, <float complex *>beta.data,
                      q_ptr, &N, z_ptr, &N, &M, NULL, NULL, NULL,
                      &qwork, &lwork, &qiwork, &liwork, &info)
    elif scalar is double_complex:
        lapack.ztgsen(&ijob, &wantq, &wantz, <l_logical *>select.data,
                      &N, <double complex *>S.data, &N,
                      <double complex *>T.data, &N,
                      <double complex *>alphar.data, <double complex *>beta.data,
                      q_ptr, &N, z_ptr, &N, &M, NULL, NULL, NULL,
                      &qwork, &lwork, &qiwork, &liwork, &info)

    assert info == 0, "Argument error in tgsen"

    lwork = lwork_from_qwork(qwork)
    cdef np.ndarray[scalar] work = np.empty(lwork, dtype=S.dtype)

    liwork = qiwork
    cdef np.ndarray[l_int] iwork = np.empty(liwork, dtype=int_dtype)

    # The actual calculation

    if scalar is float:
        lapack.stgsen(&ijob, &wantq, &wantz, <l_logical *>select.data,
                      &N, <float *>S.data, &N,
                      <float *>T.data, &N,
                      <float *>alphar.data, <float *>alphai.data,
                      <float *>beta.data,
                      q_ptr, &N, z_ptr, &N, &M, NULL, NULL, NULL,
                      <float *>work.data, &lwork,
                      <l_int *>iwork.data, &liwork, &info)
    elif scalar is double:
        lapack.dtgsen(&ijob, &wantq, &wantz, <l_logical *>select.data,
                      &N, <double *>S.data, &N,
                      <double *>T.data, &N,
                      <double *>alphar.data, <double *>alphai.data,
                      <double *>beta.data,
                      q_ptr, &N, z_ptr, &N, &M, NULL, NULL, NULL,
                      <double *>work.data, &lwork,
                      <l_int *>iwork.data, &liwork, &info)
    elif scalar is float_complex:
        lapack.ctgsen(&ijob, &wantq, &wantz, <l_logical *>select.data,
                      &N, <float complex *>S.data, &N,
                      <float complex *>T.data, &N,
                      <float complex *>alphar.data, <float complex *>beta.data,
                      q_ptr, &N, z_ptr, &N, &M, NULL, NULL, NULL,
                      <float complex *>work.data, &lwork,
                      <l_int *>iwork.data, &liwork, &info)
    elif scalar is double_complex:
        lapack.ztgsen(&ijob, &wantq, &wantz, <l_logical *>select.data,
                      &N, <double complex *>S.data, &N,
                      <double complex *>T.data, &N,
                      <double complex *>alphar.data, <double complex *>beta.data,
                      q_ptr, &N, z_ptr, &N, &M, NULL, NULL, NULL,
                      <double complex *>work.data, &lwork,
                      <l_int *>iwork.data, &liwork, &info)

    if info > 0:
        raise LinAlgError("Reordering failed; problem is very ill-conditioned")

    assert info == 0, "Argument error in tgsen"

    # Real inputs possibly produce complex output
    cdef np.ndarray alpha = maybe_complex[scalar](0, alphar, alphai)

    return tuple(compress((S, T, Q, Z, alpha, beta),
                          (True, True, Q is not None, Z is not None,
                           calc_ev, calc_ev)))


def tgevc(np.ndarray[scalar, ndim=2] S,
          np.ndarray[scalar, ndim=2] T,
          np.ndarray[scalar, ndim=2] Q,
          np.ndarray[scalar, ndim=2] Z,
          np.ndarray[l_logical] select,
          left=False, right=True):
    cdef l_int N, info, M, MM

    # Check parameters

    if ((S.shape[0] != S.shape[1] or T.shape[0] != T.shape[1] or
         S.shape[0] != T.shape[0]) or
        (Q is not None and (Q.shape[0] != Q.shape[1] or
                            S.shape[0] != Q.shape[0])) or
        (Z is not None and (Z.shape[0] != Z.shape[1] or
                            S.shape[0] != Z.shape[0]))):
        raise ValueError("Invalid Schur decomposition as input")

    assert_fortran_mat(S, T, Q, Z)

    # Allocate workspaces

    N = S.shape[0]

    cdef np.ndarray[scalar] work
    if scalar in floating:
        work = np.empty(6 * N, dtype=S.dtype)
    else:
        work = np.empty(2 * N, dtype=S.dtype)

    cdef np.ndarray rwork = None
    if scalar is float_complex:
        rwork = np.empty(2 * N, dtype=np.float32)
    elif scalar is double_complex:
        rwork = np.empty(2 * N, dtype=np.float64)

    cdef char *side
    if left and right:
        side = "B"
    elif left:
        side = "L"
    elif right:
        side = "R"
    else:
        return

    cdef l_logical backtr = False

    cdef char *howmny
    cdef np.ndarray[l_logical] select_cpy = None
    cdef l_logical *select_ptr
    if select is not None:
        howmny = "S"
        MM = select.nonzero()[0].size
        # Correct for possible additional storage if a single complex
        # eigenvalue is selected.
        # For that: Figure out the positions of the 2x2 blocks.
        cmplxindx = np.diagonal(S, -1).nonzero()[0]
        for i in cmplxindx:
            if bool(select[i]) != bool(select[i+1]):
                MM += 1

        # select is overwritten in tgevc
        select_cpy = np.array(select, dtype=logical_dtype,
                              order = 'F')
        select_ptr = <l_logical *>select_cpy.data
    else:
        MM = N
        select_ptr = NULL
        if ((left and right and Q is not None and Z is not None) or
            (left and not right and Q is not None) or
            (right and not left and Z is not None)):
            howmny = "B"
            backtr = True
        else:
            howmny = "A"

    cdef np.ndarray[scalar, ndim=2] vl_r
    cdef scalar *vl_r_ptr
    if left:
        if backtr:
            vl_r = Q
        else:
            vl_r = np.empty((N, MM), dtype=S.dtype, order='F')
        vl_r_ptr = <scalar *>vl_r.data
    else:
        vl_r_ptr = NULL

    cdef np.ndarray[scalar, ndim=2] vr_r
    cdef scalar *vr_r_ptr
    if right:
        if backtr:
            vr_r = Z
        else:
            vr_r = np.empty((N, MM), dtype=S.dtype, order='F')
        vr_r_ptr = <scalar *>vr_r.data
    else:
        vr_r_ptr = NULL

    if scalar is float:
        lapack.stgevc(side, howmny, select_ptr,
                      &N, <float *>S.data, &N,
                      <float *>T.data, &N,
                      vl_r_ptr, &N, vr_r_ptr, &N, &MM, &M,
                      <float *>work.data, &info)
    elif scalar is double:
        lapack.dtgevc(side, howmny, select_ptr,
                      &N, <double *>S.data, &N,
                      <double *>T.data, &N,
                      vl_r_ptr, &N, vr_r_ptr, &N, &MM, &M,
                      <double *>work.data, &info)
    elif scalar is float_complex:
        lapack.ctgevc(side, howmny, select_ptr,
                      &N, <float complex *>S.data, &N,
                      <float complex *>T.data, &N,
                      vl_r_ptr, &N, vr_r_ptr, &N, &MM, &M,
                      <float complex *>work.data, <float *>rwork.data, &info)
    elif scalar is double_complex:
        lapack.ztgevc(side, howmny, select_ptr,
                      &N, <double complex *>S.data, &N,
                      <double complex *>T.data, &N,
                      vl_r_ptr, &N, vr_r_ptr, &N, &MM, &M,
                      <double complex *>work.data, <double *>rwork.data, &info)

    assert info == 0, "Argument error in tgevc"
    assert MM == M, "Unexpected number of eigenvectors returned in tgevc"

    if not backtr:
        if left:
            vl_r = np.asfortranarray(np.dot(Q, vl_r))
        if right:
            vr_r = np.asfortranarray(np.dot(Z, vr_r))

    # If there are complex eigenvalues, we need to postprocess the eigenvectors
    cdef np.ndarray vl, vr
    if left:
        vl = vl_r
    if right:
        vr = vr_r
    if scalar in floating:
        if scalar is float:
            dtype = np.complex64
        else:
            dtype = np.complex128
        if np.diagonal(S, -1).nonzero()[0].size:
            if left:
                vl = txevc_postprocess(dtype, S, vl_r, select)
            if right:
                vr = txevc_postprocess(dtype, S, vr_r, select)

    if left and right:
        return (vl, vr)
    elif left:
        return vl
    else:
        return vr


def prepare_for_lapack(overwrite, *args):
    """Convert arrays to Fortran format.

    This function takes a number of array objects in `args` and converts them
    to a format that can be directly passed to a Fortran function (Fortran
    contiguous NumPy array). If the arrays have different data type, they
    converted arrays are cast to a common compatible data type (one of NumPy's
    `float32`, `float64`, `complex64`, `complex128` data types).

    If `overwrite` is ``False``, an NumPy array that would already be in the
    correct format (Fortran contiguous, right data type) is neverthelessed
    copied. (Hence, overwrite = True does not imply that acting on the
    converted array in the return values will overwrite the original array in
    all cases -- it does only so if the original array was already in the
    correct format. The conversions require copying. In fact, that's the same
    behavior as in SciPy, it's just not explicitly stated there)

    If an argument is ``None``, it is just passed through and not used to
    determine the proper LAPACK type.

    Returns a list of properly converted arrays.
    """

    # Make sure we have NumPy arrays
    mats = [None]*len(args)
    for i in range(len(args)):
        if args[i] is not None:
            arr = np.asanyarray(args[i])
            if not np.issubdtype(arr.dtype, np.number):
                raise ValueError("Argument cannot be interpreted "
                                 "as a numeric array")

            mats[i] = (arr, arr is not args[i] or overwrite)
        else:
            mats[i] = (None, True)

    # First figure out common dtype
    # Note: The return type of common_type is guaranteed to be a floating point
    #       kind.
    dtype = np.common_type(*[arr for arr, ovwrt in mats if arr is not None])

    if dtype not in (np.float32, np.float64, np.complex64, np.complex128):
        raise AssertionError("Unexpected data type from common_type")

    ret = []
    for npmat, ovwrt in mats:
        # Now make sure that the array is contiguous, and copy if necessary.
        if npmat is not None:
            if npmat.ndim == 2:
                if not npmat.flags["F_CONTIGUOUS"]:
                    npmat = np.asfortranarray(npmat, dtype = dtype)
                elif npmat.dtype != dtype:
                    npmat = npmat.astype(dtype)
                elif not ovwrt:
                    # ugly here: copy makes always C-array, no way to tell it
                    # to make a Fortran array.
                    npmat = np.asfortranarray(npmat.copy())
            elif npmat.ndim == 1:
                if not npmat.flags["C_CONTIGUOUS"]:
                    npmat = np.ascontiguousarray(npmat, dtype = dtype)
                elif npmat.dtype != dtype:
                    npmat = npmat.astype(dtype)
                elif not ovwrt:
                    npmat = np.asfortranarray(npmat.copy())
            else:
                raise ValueError("Dimensionality of array is not 1 or 2")

        ret.append(npmat)

    if len(ret) == 1:
        return ret[0]
    else:
        return tuple(ret)
