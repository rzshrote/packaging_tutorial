"""
Module containing the ExampleClassInSubmodule class.
"""
from rpy2.robjects.vectors import IntMatrix
from expkg.example_functions import fn1, fn2
# __all__ = ['ExampleClassInSubmodule']

class ExampleClassInSubmodule:
    """docstring for ExampleClassInSubmodule."""

    def __init__(self, arg):
        """docstring for ExampleClassInSubmodule constructor."""
        super(ExampleClassInSubmodule, self).__init__()
        self.arg = arg

    def m2(self, arg):
        """
        Test method 2

        Parameters
        ----------
        arg : object
            Any Python object.
        """
        print(arg)

def fn4():
    """
    Create an array of numbers.
    """
    return IntMatrix([1,2,3])

def fn5(arg1, arg2, arg3):
    """
    Call multiple functions
    """
    fn1(arg1, arg2)
    fn2(arg1, arg2, arg3)
