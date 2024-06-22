#######################################################################
# Copyright (c) 2019-present, Blosc Development Team <blosc@blosc.org>
# All rights reserved.
#
# This source code is licensed under a BSD-style license (found in the
# LICENSE file in the root directory of this source tree)
#######################################################################

import numexpr as ne
import numpy as np
import pytest

import blosc2

NITEMS_SMALL = 1000
NITEMS = 10_000


@pytest.fixture(params=[np.float32, np.float64])
def dtype_fixture(request):
    return request.param


@pytest.fixture(params=[(NITEMS_SMALL,), (NITEMS,), (NITEMS // 100, 100)])
def shape_fixture(request):
    return request.param


@pytest.fixture
def array_fixture(dtype_fixture, shape_fixture):
    nelems = np.prod(shape_fixture)
    na1 = np.linspace(0, 10, nelems, dtype=dtype_fixture).reshape(shape_fixture)
    # For full generality, use different chunks and blocks
    # chunks = [c // 17 for c in na1.shape]
    # blocks = [c // 19 for c in na1.shape]
    # chunks1 = [c // 23 for c in na1.shape]
    # blocks1 = [c // 29 for c in na1.shape]
    chunks = [c // 4 for c in na1.shape]
    blocks = [c // 8 for c in na1.shape]
    chunks1 = [c // 10 for c in na1.shape]
    blocks1 = [c // 30 for c in na1.shape]
    a1 = blosc2.asarray(na1, chunks=chunks, blocks=blocks)
    na2 = np.copy(na1)
    a2 = blosc2.asarray(na2, chunks=chunks, blocks=blocks)
    na3 = np.copy(na1)
    # Let other operands have chunks1 and blocks1
    a3 = blosc2.asarray(na3, chunks=chunks1, blocks=blocks1)
    na4 = np.copy(na1)
    a4 = blosc2.asarray(na4, chunks=chunks1, blocks=blocks1)
    return a1, a2, a3, a4, na1, na2, na3, na4


@pytest.mark.parametrize("reduce_op", ["sum", "prod", "min", "max", "any", "all"])
def test_reduce_bool(array_fixture, reduce_op):
    a1, a2, a3, a4, na1, na2, na3, na4 = array_fixture
    expr = a1 + a2 > a3 * a4
    nres = ne.evaluate("na1 + na2 > na3 * na4")
    res = getattr(expr, reduce_op)()
    nres = getattr(nres, reduce_op)()
    tol = 1e-15 if a1.dtype == "float64" else 1e-6
    np.testing.assert_allclose(res, nres, atol=tol, rtol=tol)


@pytest.mark.parametrize("reduce_op", ["sum", "prod", "mean", "std", "var", "min", "max", "any", "all"])
@pytest.mark.parametrize("axis", [0, 1, (0, 1), None])
@pytest.mark.parametrize("keepdims", [True, False])
@pytest.mark.parametrize("dtype_out", [np.int16, np.float64])
@pytest.mark.parametrize("kwargs", [{}, {"cparams": dict(clevel=1, shuffle=blosc2.Filter.BITSHUFFLE)}])
def test_reduce_params(array_fixture, axis, keepdims, dtype_out, reduce_op, kwargs):
    a1, a2, a3, a4, na1, na2, na3, na4 = array_fixture
    if axis is not None and np.isscalar(axis) and len(a1.shape) >= axis:
        return
    if type(axis) == tuple and len(a1.shape) < len(axis):
        return
    if reduce_op == "prod":
        # To avoid overflow, create a1 and a2 with small values
        na1 = np.linspace(0, 0.1, np.prod(a1.shape), dtype=np.float32).reshape(a1.shape)
        a1 = blosc2.asarray(na1)
        na2 = np.linspace(0, 0.5, np.prod(a1.shape), dtype=np.float32).reshape(a1.shape)
        a2 = blosc2.asarray(na2)
        expr = a1 + a2 - 0.2
        nres = eval("na1 + na2 - .2")
    else:
        expr = a1 + a2 - a3 * a4
        nres = eval("na1 + na2 - na3 * na4")
    if reduce_op in ("sum", "prod", "mean", "std"):
        if reduce_op in ("mean", "std") and dtype_out == np.int16:
            # mean and std need float dtype as output
            dtype_out = np.float64
        res = getattr(expr, reduce_op)(axis=axis, keepdims=keepdims, dtype=dtype_out, **kwargs)
        nres = getattr(nres, reduce_op)(axis=axis, keepdims=keepdims, dtype=dtype_out)
    else:
        res = getattr(expr, reduce_op)(axis=axis, keepdims=keepdims, **kwargs)
        nres = getattr(nres, reduce_op)(axis=axis, keepdims=keepdims)
    tol = 1e-15 if a1.dtype == "float64" else 1e-6
    if kwargs != {}:
        if not np.isscalar(res):
            assert isinstance(res, blosc2.NDArray)
        np.testing.assert_allclose(res[()], nres, atol=tol, rtol=tol)
    else:
        np.testing.assert_allclose(res, nres, atol=tol, rtol=tol)


# TODO: "prod" is not supported here because it overflows with current values
@pytest.mark.parametrize("reduce_op", ["sum", "min", "max", "mean", "std", "var", "any", "all"])
@pytest.mark.parametrize("axis", [0, 1, None])
def test_reduce_expr_arr(array_fixture, axis, reduce_op):
    a1, a2, a3, a4, na1, na2, na3, na4 = array_fixture
    if axis is not None and len(a1.shape) >= axis:
        return
    expr = a1 + a2 - a3 * a4
    nres = eval("na1 + na2 - na3 * na4")
    res = getattr(expr, reduce_op)(axis=axis) + getattr(a1, reduce_op)(axis=axis)
    nres = getattr(nres, reduce_op)(axis=axis) + getattr(na1, reduce_op)(axis=axis)
    tol = 1e-15 if a1.dtype == "float64" else 1e-6
    np.testing.assert_allclose(res, nres, atol=tol, rtol=tol)


# Test broadcasting
@pytest.mark.parametrize("reduce_op", ["sum", "mean", "std", "var", "min", "max", "any", "all"])
@pytest.mark.parametrize("axis", [0, 1, (0, 1), None])
@pytest.mark.parametrize("keepdims", [True, False])
@pytest.mark.parametrize(
    "shapes",
    [
        ((5, 5, 5), (5, 5), (5,)),
        ((10, 10, 10), (10, 10), (10,)),
        ((100, 100, 100), (100, 100), (100,)),
    ],
)
def test_broadcast_params(axis, keepdims, reduce_op, shapes):
    na1 = np.linspace(0, 1, np.prod(shapes[0])).reshape(shapes[0])
    na2 = np.linspace(1, 2, np.prod(shapes[1])).reshape(shapes[1])
    na3 = np.linspace(2, 3, np.prod(shapes[2])).reshape(shapes[2])
    a1 = blosc2.asarray(na1)
    a2 = blosc2.asarray(na2)
    a3 = blosc2.asarray(na3)

    expr1 = a1 + a2 - a3
    assert expr1.shape == shapes[0]
    expr2 = a1 * a2 + 1
    assert expr2.shape == shapes[0]
    res = expr1 - getattr(expr2, reduce_op)(axis=axis, keepdims=keepdims)
    assert res.shape == shapes[0]
    # print(f"res: {res.shape} expr1: {expr1.shape} expr2: {expr2.shape}")
    nres = eval(f"na1 + na2 - na3 - (na1 * na2 + 1).{reduce_op}(axis={axis}, keepdims={keepdims})")

    tol = 1e-14 if a1.dtype == "float64" else 1e-5
    np.testing.assert_allclose(res[:], nres, atol=tol, rtol=tol)
