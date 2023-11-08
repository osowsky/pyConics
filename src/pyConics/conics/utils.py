#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

# #------------------------------------------------------------------
# # Everything that can be visible to the world.
 
__all__ = [ 'create_conic_from_lines', 'create_conic' ]

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
from pyConics.tolerance import tol
from pyConics.constants import const
from pyConics.point import CPoint
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

def create_conic( a: float, c: float, center: CPoint, angle: float ) -> np.ndarray:
    # Get the minor axis.
    a2 = a * a
    c2 = c * c
    if ( a >= c ): # it is an ellipse.
        b2 = a2 - c2
    else: # it is a hyperbole.
        b2 = c2 - a2

    # Build a quadratic form for the conic with centered on ( 0, 0 )
    # and without rotation.
    if ( a >= c ): # it is an ellipse.
        C = np.array( [ [ 1.0 / a2, 0.0 ], [ 0.0, 1.0 / b2 ] ] )
    else:
        C = np.array( [ [ 1.0 / a2, 0.0 ], [ 0.0, 1.0 / -b2 ] ] )

    # Build the rotating matrix.
    R = np.array( [ [ np.cos( angle ), np.sin( angle ) ], [ -np.sin( angle ), np.cos( angle ) ] ] )

    # Get the center vector.
    xy_o = center.gform[ 0 : 2 ][np.newaxis].T

    # Create the matrices ABC, DE, and F.
    ABC = tol.adjust2relzeros( R.T @ C @ R )
    DE = ( -1 * ABC ) @ xy_o
    F = ( xy_o.T @ ABC @ xy_o ) - 1

    # Build the matrix representation of a conic.
    return tol.adjust2relzeros( np.block( [ [ ABC, DE ], [ DE.T, F ] ] ) )

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

    # Default nondegenerate conic.
    C4 = CConic( name = 'C4' )
    print( C4 )
    print( f'Is {C4.name} degenerate? {C4.is_degenerate}.\n' )

    # Nondegenerate conic with a, c, center, and angle.
    C5 = CConic( 2.0, 0.5, CPoint( ( 2, 1 ) ), 30.0 / 180 * const.pi, 'C5' )
    print( C5 )
    print( f'Is {C5.name} degenerate? {C5.is_degenerate}.\n' )

    # Nondegenerate conic with a, and foci.
    C6 = CConic( 2.0, name = 'C6', foci = ( CPoint( ( 0, 1 ) ), CPoint( ( 0, -1 ) ) ) )
    print( C6 )
    print( f'Is {C6.name} degenerate? {C6.is_degenerate}.\n' )
