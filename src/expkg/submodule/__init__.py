# from . import ExampleClassInSubmodule
#
# __all__ = []
# __all__ += ExampleClassInSubmodule.__all__
#
# del ExampleClassInSubmodule

# from .ExampleClassInSubmodule import *

# order dependent imports
from . import ExampleClassInSubmodule
from . import InheritingClass
