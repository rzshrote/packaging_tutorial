"""
Module containing example functions
"""
from rpy2.robjects.vectors import IntMatrix

# __all__ = ['fn1', 'fn2', 'fn3']

def fn1(arg1, arg2):
    """
    Test function 1

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
