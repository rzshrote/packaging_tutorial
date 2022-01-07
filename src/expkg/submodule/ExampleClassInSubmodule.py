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
