#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'Line' ]

#------------------------------------------------------------------
# Import from...
#  
from varname import varname
from agobj import AGObj
from errors import LineTypeError
from origin import origin

#------------------------------------------------------------------
# Import as...
#
import numpy as np
np.set_printoptions( formatter = { 'float': lambda x: "{0:0.4e}".format( x ) } )

#------------------------------------------------------------------
# Class Line.
#  
class Line( AGObj ):
    def __init__( self,
                  line: tuple[ float, float, float ] = ( 1.0, -1.0, 0.0 ),
                  name: str = '' ) -> None:
        super().__init__( name )

        # Redim the geometric form.
        self._gform = _validate_point( line )

        # Store this value to be possible restore it to the origin.
        self._from_origin = self._gform

        # Translate the origin from ( 0, 0 ) to another origin in '(origin.x, origin.y )'.
        self.update_origin()

    def __repr__( self ) -> str:
        # return an info messsage for this class.
        info = f'{self.name}: ( x, y ) | {self.gform} * [ x y 1 ]\' = 0'
        if ( self.gform[ 0 ] == 0.0 ) and ( self.gform[ 1 ] == 0.0 ):
            info += f' -> line at the infinity.'
        return info

    def update_origin( self ) -> None:
        # Translate the origin from ( 0, 0 ) to another origin in '(origin.x, origin.y )'.
        self._gform = origin.change_line( self._from_origin )

    def cross( self, other: Point | Line ) -> Point | Line:
        from functions import cross

        # Get the cross product.
        res = cross( self, other )
        res.name = str( varname() )
        return res

    def __mul__( self, other: Point | Line ) -> Point | Line:
        # Get the cross product.
        res = self.cross( other )
        res.name = str( varname() )
        return res

#------------------------------------------------------------------
# Internal functions.
#  
def _validate_point( line: tuple[ float, float, float ] ) -> np.ndarray:
    if ( len( line ) == 3 ):
        return np.array( line )
    else:
        raise LineTypeError( Line.__name__, Line.gform.fset.__name__ )

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Keep this imports even there is no test code.
    from line import Line
    from point import Point

    import os
    os.system( 'cls' )

    # Create the line y = x + 1
    print( origin )
    l1 = Line( ( 1, -1, 1 ) )
    print( l1, '\n' )

    # Change the origin to ( 0, 1 ), update the origin and back it to the origin.
    origin.x = 0
    origin.y = 1
    print( origin )
    l1.update_origin()
    print( l1, '\n' )
    origin.reset()
    print( origin )
    l1.update_origin()
    print( l1, '\n' )

    # Change the origin to ( 1, 0 ), update the origin and back it to the origin.
    origin.x = 1
    origin.y = 0
    print( origin )
    l1.update_origin()
    print( l1, '\n' )
    origin.reset()
    print( origin )
    l1.update_origin()
    print( l1, '\n' )
 
    # How to use cross product.
    p1 = Point( ( 1, 1 ) )      # p1 = ( 1, 1 )
    p2 = Point( ( -1, -1 ) )    # p2 = ( -1, -1 ) 
    l1 = p1.cross( p2 )         # l1: y = x
    print( l1, '\n' )
    l1 = p1 * p2                # l1: y = x
    print( l1, '\n' )
    
    l1 = Line( ( 1, -1, 1 ) )
    l2 = Line( ( 1, -1, -1 ) )
    l3 = Line( ( -1, -1, 1 ) )
    p3 = l1.cross( l2 )       # p3 is a point at the infinity.
    print( p3, '\n' )
    p3 = l1 * l2       # p3 is a point at the infinity.
    print( p3, '\n' )
    p4 = l1.cross( l3 )       # p4 = ( 0, 1 )
    print( p4, '\n' )
    p4 = l1 * l3       # p4 = ( 0, 1 )
    print( p4, '\n' )
    p5 = l2.cross( l3 )       # p5 = ( 1, 0 )
    print( p5, '\n' )
    p5 = l2 * l3       # p5 = ( 1, 0 )
    print( p5, '\n' )

    p6 = Point( ( 1, 0 ) )
    l4 = l1.cross( p6 )        # l4 = ( 1, 1, -1 ) that pass through p6
    print( l4, '\n' )
    l4 = l1 * p6        # l4 = ( 1, 1, -1 ) that pass through p6
    print( l4, '\n' )
    l5 = p6.cross( l1 )        # l5 = ( 1, 1, -1 ) that pass through p6
    print( l5, '\n' )
    l5 = p6 * l1        # l5 = ( 1, 1, -1 ) that pass through p6
    print( l5, '\n' )
