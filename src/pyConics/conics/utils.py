#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

# #------------------------------------------------------------------
# # Everything that can be visible to the world.
 
__all__ = [ 'create_conic_from_lines' ]

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
from pyConics.line import CLine

# #------------------------------------------------------------------
# # Import as...
# #
import numpy as np

def create_conic_from_lines( lines: tuple[ CLine, CLine ] ) -> np.ndarray:
    l1 = lines[ 0 ].gform[np.newaxis]
    l2 = lines[ 1 ].gform[np.newaxis].T
    M = ( l2 @ l1 )
    return M + M.T

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Keep this imports even there is no test code.
    from pyConics.point import CPoint
    from pyConics.line import CLine
    from pyConics.conics.conic import CConic

    # Degenerate conic.
    f = CLine( ( 1, 0, 1 ) )    
    g = CLine( ( 1, 0, -1 ) )
    C0 = CConic( degenerate = ( f, g ), name = 'C0' )
    print( C0 )
    print( f'Is {C0.name} degenerate? {C0.is_degenerate}.\n' )

    # Degenerate conic.
    f = CLine( ( 1, 0, -1 ) )    
    g = CLine( ( 1, 0, -3 ) )
    C1 = CConic( degenerate = ( f, g ), name = 'C1' )
    print( C1 )
    print( f'Is {C1.name} degenerate? {C1.is_degenerate}.\n' )

    # Degenerate conic.
    f = CLine( ( 1, -1, -2 ) )    
    g = CLine( ( -1, -1, 2 ) )
    C2 = CConic( degenerate = ( f, g ), name = 'C2' )
    print( C2 )
    print( f'Is {C2.name} degenerate? {C2.is_degenerate}.\n' )

    # Degenerate conic.
    f = CLine( ( 1, 0, -2 ) )    
    C3 = CConic( degenerate = ( f, f ), name = 'C3' )
    print( C3 )
    print( f'Is {C3.name} degenerate? {C3.is_degenerate}.\n' )

