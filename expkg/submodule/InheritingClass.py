"""
Module containing the InheritingClass class.
"""
from .ExampleClassInSubmodule import ExampleClassInSubmodule

class InheritingClass(ExampleClassInSubmodule):
    """docstring for InheritingClass."""

    def __init__(self, arg):
        """docstring for InheritingClass constructor."""
        super(InheritingClass, self).__init__()
        self.arg = arg

    def minherit(self, arg):
        """
        Test function for inheritance.

        Parameters
        ----------
        arg : object
            Any Python object.
        """
        print("Inherited:", arg)
