.. _NDArray:

NDArray
=======

The multidimensional data array class. This class consists of a set of useful parameters and methods that allow not only to create an array correctly, but also to being able to extract multidimensional slices from it (and much more).

.. currentmodule:: blosc2.NDArray

Methods
-------

.. autosummary::
    :toctree: autofiles/ndarray
    :nosignatures:

    __getitem__
    __setitem__
    copy
    iterchunks_info
    slice
    squeeze
    resize
    tobytes
    to_cframe

Attributes
----------

.. autosummary::
    :toctree: autofiles/ndarray

    ndim
    shape
    ext_shape
    chunks
    ext_chunks
    blocks
    blocksize
    chunksize
    dtype
    fields
    info
    schunk
    size


.. currentmodule:: blosc2

Constructors
------------

.. autosummary::
    :toctree: autofiles/ndarray
    :nosignatures:

    asarray
    copy
    empty
    frombuffer
    full
    ndarray_from_cframe
    uninit
    zeros
