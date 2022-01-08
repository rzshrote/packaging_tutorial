"""
expkg root module
"""
# # import individual files as modules
# from . import example_functions
# from . import ExampleClass
#
# # add objects in modules' __all__ to __init__.__all__
# __all__ = ['submodule']
# __all__ += example_functions.__all__
# __all__ += ExampleClass.__all__
#
# # delete modules loaded from individual files
# del example_functions
# del ExampleClass

# from each file import __all__
# from .example_functions import *
# from .ExampleClass import *
from . import example_functions
from . import ExampleClass
from . import submodule
