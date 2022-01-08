"""
Module containing the ExampleClass class.
"""
# __all__ = ['ExampleClass']

class ExampleClass:
    """docstring for ExampleClass."""

    def __init__(self, arg):
        """docstring for ExampleClass constructor."""
        super(ExampleClass, self).__init__()
        self.arg = arg

    def m1(self, arg):
        """
        Test method 1

        Parameters
        ----------
        arg : object
            Any Python object.
        """
        print(arg)
