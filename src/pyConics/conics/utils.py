#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

# #------------------------------------------------------------------
# # Everything that can be visible to the world.
 
# __all__ = [ 'skew_symmetric', 'cross', 'dot', 'are_perpendicular', \
#             'are_parallel', 'distance' ]

# #------------------------------------------------------------------
# # Import from...
# #
# from typing import Any
# from numpy import linalg as LA

# #------------------------------------------------------------------
# # Import from...
# # We use here TYPE_CHECKING constant to avoid circular import  
# # exceptions.
# #
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     ... # Do nothing here, because there are no pyConics modules
#         # here to be imported.
        
# from pyConics.errors import CTypeError, CArgumentsError
# from pyConics.tolerance import tol
# from pyConics.constants import const
# from pyConics.point import CPoint
# from pyConics.line import CLine

# #------------------------------------------------------------------
# # Import as...
# #
# import numpy as np
