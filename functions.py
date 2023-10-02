#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'skew_symmetric', 'cross' ]

#------------------------------------------------------------------
# Import from...
#
from varname import varname
from errors import TypeError
from point import Point
from line import Line

#------------------------------------------------------------------
# Import as...
#
import numpy as np

def skew_symmetric( gf: Point | Line ) -> np.ndarray:
    if ( not isinstance( gf, ( Point, Line ) ) ):
        raise TypeError( gf.__class__.__name__ )

    # Build a skew-symmetric matrix from a point or a Line.
    l1 = [ 0.0, -gf.gform[ 2 ], gf.gform[ 1 ] ]
    l2 = [ gf.gform[ 2 ], 0.0, -gf.gform[ 0 ] ]
    l3 = [ -gf.gform[ 1 ], gf.gform[ 0 ], 0.0 ]
    return np.array( [ l1, l2, l3 ] )

def cross( gf1: Point | Line, gf2: Point | Line ) -> Point | Line:
    if ( not isinstance( gf1, ( Point, Line ) ) ):
        raise TypeError( gf1.__class__.__name__ )
    if ( not isinstance( gf2, ( Point, Line ) ) ):
        raise TypeError( gf2.__class__.__name__ )
    
    # There are 3 conditions:
    # 1) Point x Point returns a Line that passes
    #    through both Points.
    # 2) Line x Line returns a Point that intercepts
    #    both Lines.
    # 3) Line x Point or Point x Line returns a Line
    #    that pass through the Point.
    if ( ( isinstance( gf1, ( Point ) ) ) and ( isinstance( gf2, ( Line ) ) ) ) or \
        ( ( isinstance( gf1, ( Line ) ) ) and ( isinstance( gf2, ( Point ) ) ) ):
        # Condition 3.
        to_origin = np.array( [ [ 1.0, 0.0, 0.0 ], [ 0.0, 1.0, 0.0 ], [ 0.0, 0.0, 0.0 ] ] )

        # Get the skew-symmetric matrix from gf{1,2}.
        if ( isinstance( gf1, ( Point ) ) ):
            ss_gf = skew_symmetric( gf1 )
            res = ss_gf @ to_origin @ gf2.gform
        else:
            ss_gf = skew_symmetric( gf2 )
            res = ss_gf @ to_origin @ gf1.gform
        res = Line( tuple[float, float, float]( res ) )
        res.name = str( varname() )
        return res
    else:
        # Get the skew-symmetric matrix from gf1.
        ss_gf1 = skew_symmetric( gf1 )

        # Anything else.
        res = ss_gf1 @ gf2.gform

        # Condition 1.
        if ( ( isinstance( gf1, ( Point ) ) ) and ( isinstance( gf2, ( Point ) ) ) ):
            res = Line( tuple[float, float, float]( res ) )
            res.name = str( varname() )
            return res
        
        # Condition 2.
        if ( res[ -1 ] != 0.0 ):
            res = Point( tuple[float, float, float]( res / res[ -1 ] ) )
        else:
            res = Point( tuple[ float, float, float ]( res ) )
        res.name = str( varname() )
        return res


#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    import os
    os.system( 'cls' )

    # Plot the skew-symmetric matrix of a point.
    p1 = Point( ( 3.0, 2.0 ) )
    print( p1, '\n' )
    ssp1 = skew_symmetric( p1 )
    print( ssp1, '\n' ) 

    # Test invalid argument for the skew_symmetric function.
    try:
        p2 = ( ( 'a', 'b' )  )
        ssp2 = skew_symmetric( p2 ) # type: ignore
    except TypeError as e:
        print( e )
    print()

    # How to use cross product.
    p1 = Point( ( 1, 1 ) )      # p1 = ( 1, 1 )
    p2 = Point( ( -1, -1 ) )    # p2 = ( -1, -1 ) 
    l1 = cross( p1, p2 )        # l1: y = x
    print( l1, '\n' )
    
    l1 = Line( ( 1, -1, 1 ) )
    l2 = Line( ( 1, -1, -1 ) )
    l3 = Line( ( -1, -1, 1 ) )
    p3 = cross( l1, l2 )       # p3 is a point at the infinity.
    print( p3, '\n' )
    p4 = cross( l1, l3 )       # p4 = ( 0, 1 )
    print( p4, '\n' )
    p5 = cross( l2, l3 )       # p5 = ( 1, 0 )
    print( p5, '\n' )
    
    p6 = Point( ( 1, 0 ) )
    l4 = cross( l1, p6 )        # l4 = ( 1, 1, -1 ) that pass through p6
    print( l4, '\n' )
    l5 = cross( p6, l1 )        # l5 = ( 1, 1, -1 ) that pass through p6
    print( l5, '\n' )
