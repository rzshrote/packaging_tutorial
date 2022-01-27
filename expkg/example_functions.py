"""
Module containing example functions
"""
from rpy2.robjects.vectors import IntMatrix

# __all__ = ['fn1', 'fn2', 'fn3']

def fn1(arg1, arg2):
    """
    Test function 1

    .. math::
        \\mathbf{Z} = \\begin{bmatrix} \\mathbf{Z_{misc}} & \\mathbf{Z_{a}} \\end{bmatrix}

    .. math::
        \\mathbf{Y} = \\mathbf{XB} + \\mathbf{ZU} + \\mathbf{E}

    Section:

    - :math:`\\mathbf{Z}` is a matrix.
    - :math:`\\mathbf{Z_{misc}}` is a matrix of miscellaneous random effect predictors of shape ``(n,p_misc)``
    - :math:`\\mathbf{Z_{a}}` is a matrix of additive genomic marker effect predictors of shape ``(n,p_a)``
    - ``p_misc`` + ``p_a`` = ``p``.

    Parameters
    ----------
    arg1 : object
        Any Python object.
    arg2 : object
        Any Python object.
    """
    print(arg1, ":", arg2)

def fn2(arg1, arg2, arg3):
    """
    Test function 2

    Parameters
    ----------
    arg1 : object
        Any Python object.
    arg2 : object
        Any Python object.
    arg3 : object
        Any Python object.
    """
    print(arg1, "?", arg2, ":", arg3)

def fn3():
    """
    Create an array of numbers.
    """
    return IntMatrix([1,2,3])
