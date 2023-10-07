#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'skew_symmetric', 'cross', 'dot', 'are_orthogonal', \
            'are_parallel', 'distance' ]

#------------------------------------------------------------------
# Import from...
#
from os.path import basename, splitext
from typing import Any
from numpy import linalg as LA

if ( __name__ == '__main__' ) or \
    ( __name__ == splitext( basename( __file__ ) )[ 0 ] ):
    from errors import TypeError, ArgumentsError
    from point import Point
    from line import Line
    from tolerance import tol
else:
    from .errors import TypeError, ArgumentsError
    from .point import Point
    from .line import Line
    from .tolerance import tol

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

def cross( gf1: Point | Line, gf2: Point | Line ) -> Any[ Point | Line ]:
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
        return Line( tuple[float, float, float]( res ), shift_origin = False )
    elif ( ( isinstance( gf1, ( Point ) ) ) and ( isinstance( gf2, ( Point ) ) ) ):
        # Condition 1.
        # Get the skew-symmetric matrix from gf1.
        ss_gf1 = skew_symmetric( gf1 )

        # Cross product betwwen them.
        return Line( tuple[float, float, float]( ss_gf1 @ gf2.gform ), shift_origin = False )
    else:    
        # Condition 2.
        # Are they parallel lines? Test for epsilon number condition.
        if ( are_parallel( gf1, gf2 ) == True ): # type: ignore
            gf1.gform[ 0 ] = gf2.gform[ 0 ]
            gf1.gform[ 1 ] = gf2.gform[ 1 ]

        # Get the skew-symmetric matrix from gf1.
        ss_gf1 = skew_symmetric( gf1 )

        return Point( tuple[ float, float, float ]( ss_gf1 @ gf2.gform ), shift_origin = False )

def dot( gf1: Point | Line, gf2: Point | Line ) -> float:
    if ( not isinstance( gf1, ( Point, Line ) ) ):
        raise TypeError( gf1.__class__.__name__ )
    if ( not isinstance( gf2, ( Point, Line ) ) ):
        raise TypeError( gf2.__class__.__name__ )
    
    # There are 2 conditions:
    # 1) Point x Line returns their inner product.
    # 2) Line x Point returns their inner product.
    if ( ( isinstance( gf1, ( Point ) ) ) and ( isinstance( gf2, ( Line ) ) ) ):
        # Condition 1.
        return np.inner( gf1.gform, gf2.gform )
    elif ( ( isinstance( gf1, ( Line ) ) ) and ( isinstance( gf2, ( Point ) ) ) ):
        # Condition 2.
        return np.inner( gf1.gform, gf2.gform )
    else:
        raise ArgumentsError( dot.__name__, gf1.__class__.__name__, gf2.__class__.__name__ )

def are_parallel( gf1: Line, gf2: Line ) -> bool:
    if ( not isinstance( gf1, Line ) ):
        raise TypeError( gf1.__class__.__name__ )
    if ( not isinstance( gf2, Line ) ):
        raise TypeError( gf2.__class__.__name__ )
    
    # To be parallel lines, x1 == x2 and y1 == y2 must be equals
    # or ( x1 * y2 ) - ( x2 * y1 ) must be zero.
    op1  = gf1.gform[ 0 ] * gf2.gform[ 1 ]
    op2 = gf1.gform[ 1 ] * gf2.gform[ 0 ]

    if ( tol.iszero( op1 - op2  ) == True ):
        return True
    return False

def are_orthogonal( gf1: Line, gf2: Line ) -> bool:
    if ( not isinstance( gf1, Line ) ):
        raise TypeError( gf1.__class__.__name__ )
    if ( not isinstance( gf2, Line ) ):
        raise TypeError( gf2.__class__.__name__ )
    
    # To be orthogonal lines, ( x1 * x2 ) + ( y1 * y2 ) must be zero.
    op1  = gf1.gform[ 0 ] * gf2.gform[ 0 ]
    op2 = gf1.gform[ 1 ] * gf2.gform[ 1 ]

    if ( tol.iszero( op1 + op2  ) == True ):
        return True
    return False

def distance( gf1: Point | Line, gf2: Point | Line ) -> float:
    if ( not isinstance( gf1, ( Point, Line ) ) ):
        raise TypeError( gf1.__class__.__name__ )
    if ( not isinstance( gf2, ( Point, Line ) ) ):
        raise TypeError( gf2.__class__.__name__ )
    
    # There are 4 conditions:
    # 1) Point x Point returns the distance between them.
    # 2) Line x Point returns the distance between them.
    # 3) Point x Line returns the distance between them.
    # 4) Line x Line returns  the distance between them if they are parallel lines.
    if ( ( isinstance( gf1, ( Point ) ) ) and ( isinstance( gf2, ( Point ) ) ) ):
        # Condition 1.
        return LA.norm( gf1.gform - gf2.gform )
    elif ( ( isinstance( gf1, ( Line ) ) ) and ( isinstance( gf2, ( Point ) ) ) ):
        # Condition 2.
        l: Line = gf1 * gf2 # line passes through gf2 and it is orthogonal to gf1.
        p: Point = l * gf1  # point is the intersection point beween l and gf1.
        return LA.norm( p.gform - gf2.gform )
    elif ( ( isinstance( gf1, ( Point ) ) ) and ( isinstance( gf2, ( Line ) ) ) ):
        # Condition 3.
        l: Line = gf1 * gf2 # line passes through gf1 and it is orthogonal to gf2.
        p: Point = l * gf2  # point is the intersection point beween l and gf2.
        return LA.norm( p.gform - gf1.gform )
    else:
        # Condition 4.
        if ( are_parallel( gf1, gf2 ) == False ): # type: ignore
            return 0.0
        n = LA.norm( gf1.gform - gf2.gform )
        d = np.sqrt( ( gf1.gform[ 0 ] ** 2 ) + ( gf1.gform[ 1 ] ** 2 ) )
        return n / d

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
    l1: Line = cross( p1, p2 )  # l1: y = x
    print( l1, '\n' )
    
    l1 = Line( ( 1, -1, 1 ) )
    l2 = Line( ( 1, -1, -1 ) )
    l3 = Line( ( -1, -1, 1 ) )
    p3: Point = cross( l1, l2 )  # p3 is a point at the infinity.
    print( p3, '\n' )
    p4: Point = cross( l1, l3 )  # p4 = ( 0, 1 )
    print( p4, '\n' )
    p5: Point = cross( l2, l3 )  # p5 = ( 1, 0 )
    print( p5, '\n' )
    
    p6 = Point( ( 1, 0 ) )
    l4: Line = cross( l1, p6 )   # l4 = ( 1, 1, -1 ) that pass through p6
    print( l4, '\n' )
    l5: Line = cross( p6, l1 )   # l5 = ( 1, 1, -1 ) that pass through p6
    print( l5, '\n' )

    # Test invalid argument for dot function.
    try:
        print( dot( l1, l2 ) )
    except ArgumentsError as e:
        print( e )
    print()

    # Get the inner product from a Line and a Point.
    # l1: y = x + 1 and p4 = ( 0, 1 ) => <p4, l1> = 0.0 
    print( f'Inner product: < p4, l1 > = {dot( p4, l1 )}' )
    print( f'Inner product: < l1, p4 > = {dot( l1, p4 )}\n' )

    
    # Are Lines parallel or orthogonal?
    l1 = Line( ( 1, -1, 0 ), 'l1' )  # x = y
    l2 = Line( ( 1, -1, 1 ), 'l2' )  # y = x + 1
    l3 = Line( ( 1, 1, -2 ), 'l3' )  # y = -x + 2
    
    # Are the lines parallel?
    print( l1, l2, l3, sep = '\n' )
    print( f'Are l1 and l2 parallel? {are_parallel( l1, l2 )}' )
    print( f'Are l1 and l3 parallel? {are_parallel( l1, l3 )}' )
    print( f'Are l2 and l3 parallel? {are_parallel( l2, l3 )}' )

    # Are the lines orthogonal?
    print( f'Are l1 and l2 orthogonal? {are_orthogonal( l1, l2 )}' )
    print( f'Are l1 and l3 orthogonal? {are_orthogonal( l1, l3 )}' )
    print( f'Are l2 and l3 orthogonal? {are_orthogonal( l2, l3 )}\n' )

    # Distance between 2 points.
    p1 = Point( ( 0, 1 ), 'p1' )
    p2 = Point( ( 1, 0 ), 'p2' )
    d12 = distance( p1, p2 )
    d21 = distance( p2, p1 )
    print( f'The distance from {p1}\nto {p2}\nis {d12:.4f}.\n' )
    print( f'The distance from {p2}\nto {p1}\nis {d21:.4f}.\n' )

    # Distance between a point and a line.
    p1 = Point( ( 1, 0 ), 'p1' )
    l1 = Line( ( 1, -1, 1 ), 'l1' )
    dlp = distance( l1, p1 )
    dpl = distance( p1, l1 )
    print( f'The distance from {l1}\nto {p1}\nis {dlp:.4f}.\n' )
    print( f'The distance from {p1}\nto {l1}\nis {dpl:.4f}.\n' )

    # Distance between two lines.
    l1 = Line( ( 1, -1, 1 ), 'l1' )
    l2 = Line( ( 1, -1, -1 ), 'l2' )
    d12 = distance( l1, l2 )
    d21 = distance( l2, l1 )
    print( f'The distance from {l1}\nto {l2}\nis {d12:.4f}.\n' )
    print( f'The distance from {l2}\nto {l1}\nis {d21:.4f}.\n' )
