#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'CConic' ]

#------------------------------------------------------------------
# Import from...
#
from typing import Any
from matplotlib import pyplot as plt
from matplotlib.path import Path
from numpy import linalg as LA

#------------------------------------------------------------------
# Import from...
# We use here TYPE_CHECKING constant to avoid circular import  
# exceptions.
#
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    ... # Do nothing here, because there are no pyConics modules
        # here to be imported.

from pyConics.constants import cconst
from pyConics.agobj import CAGObj
from pyConics.errors import CTypeError, CConicTypeError, CValueError
from pyConics.origin import corigin
from pyConics.tolerance import ctol
from pyConics.conics.utils import create_conic_from_lines, create_conic
from pyConics.conics.utils import get_lines_from_degenerate_conic
from pyConics.point import CPoint
from pyConics.line import CLine
from pyConics.linearAlgebra import rank, is_symmetric

#------------------------------------------------------------------
# Import as...
#
import numpy as np
np.set_printoptions( formatter = { 'float': lambda x: "{0:0.4e}".format( x ) } )

#------------------------------------------------------------------
# Class CConic.
#  
class CConic( CAGObj ):
    # from pyConics.point import CPoint
    # from pyConics.line import CLine

    def __init__( self,
                  a: float = 1.0, # by default, it is created a circle with
                  c: float = 0.0, # radius equal to 1 and its center at ( 0, 0 ).
                  angle: float = 0.0, # angle in radians.
                  /,
                  center: CPoint = CPoint( ( 0, 0 ), 'o' ),
                  name: str = '',
                  *,
                  foci: tuple[ CPoint, CPoint ] | None = None,
                  degenerate: tuple[ CLine, CLine ] | None = None ) -> None:
        # from pyConics.point import CPoint

        # Precedence for creating the conic:
        # 1) First: the parameter degenerate was defined.
        # 2) Second: the parameter foci, and a were defined.
        # 3) Third: the parameters a, c, center and angle were defined.
        # 4) Fourth: if no parameter was defined, then a circle is created.
        super().__init__( name )

        # Validate the CPoint and CLine objects.
        if ( not isinstance( center, CPoint ) ):
            raise CTypeError( center.__class__.__name__ )
        if ( foci is not None ):
            if ( not isinstance( foci[ 0 ], CPoint ) ):
                raise CTypeError( foci[ 0 ].__class__.__name__ )
            if ( not isinstance( foci[ 1 ], CPoint ) ):
                raise CTypeError( foci[ 1 ].__class__.__name__ )
    
        if ( degenerate is not None ):
            if ( not isinstance( degenerate[ 0 ], CLine ) ):
                raise CTypeError( degenerate[ 0 ].__class__.__name__ )
            if ( not isinstance( degenerate[ 1 ], CLine ) ):
                raise CTypeError( degenerate[ 1 ].__class__.__name__ )
            
        # We need to keep the main parameters saved, so that it is possible
        # to recover them.
        # Each precedence will be analyzed.
        # 1) the parameter degenerate was defined.
        #    the parameters a, c, center, angle and foci are not used.
        self._lines4deg: tuple[ CLine, CLine ] | None = None
        if ( degenerate is not None ):
            if ( degenerate[ 0 ].at_infinity() ) or ( degenerate[ 1 ].at_infinity() ):
                raise CConicTypeError( CConic.__name__, 'degenerate' )
            else:
                self._lines4deg = ( degenerate[ 0 ].copy(), degenerate[ 1 ].copy() )
                self._gform = create_conic_from_lines( self._lines4deg )
                self._from_origin = self._gform.copy()
        # 2) the parameter foci, and a were defined.
        #    the parameters c, center, and angle will be find out through foci.
        #    the parameter degenerate is not used.
        elif ( foci is not None ):
            if ( foci[ 0 ].at_infinity() ) or ( foci[ 1 ].at_infinity() ):
                raise CConicTypeError( CConic.__name__, 'foci' )
            if ( a <= 0.0 ):
                raise CConicTypeError( CConic.__name__, 'a or c' )
            else:
                # Get center, c, and angle.
                f1: CPoint = foci[ 0 ].copy()
                f2: CPoint = foci[ 1 ].copy()
                xm = ( f1.x + f2.x ) / 2
                ym = ( f1.y + f2.y ) / 2
                center = CPoint( ( xm, ym ) )

                # Get the distance between the foci.
                c = f1.distance( f2 ) / 2

                # Focal Line.
                l: CLine = f1 * f2

                # Get the angle.
                angle = l.coef_angular( True )
        # 3) and 4) the parameters a, c, center, and angle were defined.
        #           the parameters foci, and degenerate are not used.
        else:
            if ( center.at_infinity() ):
                raise CConicTypeError( CConic.__name__, 'center' )
            if ( ( a <= 0.0 ) or ( c < 0.0 ) ):
                raise CConicTypeError( CConic.__name__, 'a or c' )
        
        # Create the nondegenerate conic.
        if ( self._lines4deg is None ):
            self._gform = create_conic( a, c, center, angle )
            self._from_origin = self._gform.copy()

        # Get the matrix rank.
        self._rank = rank( self._gform )

    def __repr__( self ) -> str:
        # # return an info messsage for this class.
        info = f'{self.name}: ( x, y ) | [ x y 1 ] *\n{self.gform} * [ x y 1 ].T = 0'
        return info

    def __contains__( self, other: CPoint ) -> bool:
        # from pyConics import CPoint
        if ( not isinstance( other, CPoint ) ):
            raise CTypeError( other.__class__.__name__ )
    
        # Get the line that is tangent to other.
        l: CLine = self * other

        # The point lies in the line.
        return other in l

    def __eq__( self, other: CConic ) -> bool:
        if ( not isinstance( other, CConic ) ):
            raise CTypeError( other.__class__.__name__ )

        # Copy the matrices in the input arguments.
        A = self._gform.copy()
        B = other._gform.copy()

        # Get the elements that are different of zero.
        rows, cols = np.where( A != 0.0 )
    
        # At least one element of self must be different of zero.
        if ( ( rows.size == 0 ) or ( cols.size == 0 ) ):
            return False
    
        # Get the constant that multiplies A.
        i = rows[ 0 ]
        j = cols[ 0 ]
        alf = B[ i, j ] / A[ i, j ]

        # alp can not be zero.
        if ( alf == 0.0 ):
            return False
    
        # Scaling B.
        B = B / alf

        # Test all elements.    
        n, *_ = A.shape
        for i in range( n ):
            for j in range( n ):
                if ( not ctol.iszero( A[ i, j ] - B[ i, j ] ) ):
                    return False
        return True
    
    def __add__( self, other: CConic ) -> CConic:
        if ( not isinstance( other, CConic ) ):
            raise CTypeError( other.__class__.__name__ )
        
        M = self._gform + other._gform
        return CConic.create_from_array( M )

    def __mul__( self, other: CPoint | CLine ) -> Any[ CPoint | CLine ]:
        # from pyConics import CPoint, CLine
        if ( not isinstance( other, ( CPoint, CLine ) ) ):
            raise CTypeError( other.__class__.__name__ )
    
        # Multiply the Conic by the point. A line is returned.
        if ( isinstance( other, CPoint ) ):
            v = self._gform @ other._gform
            l = CLine( ( v[ 0 ], v[ 1 ], v[ 2 ] ), shift_origin = False )
            return l

        # Multiply the Conic by the line. A point is returned.
        if ( self.is_fullrank == False ):
            return CPoint(( 0.0, 0.0, 0.0 ), shift_origin = False )

        v = LA.inv( self._gform ) @ other._gform
        p = CPoint( ( v[ 0 ], v[ 1 ], v[ 2 ] ), shift_origin = False )
        return p
    
    def __rmul__( self, other: int | float ) -> CConic:
        if ( not isinstance( other, ( float, int ) ) ):
            raise CTypeError( other.__class__.__name__ )
        
        C = self.copy()
        if ( self._lines4deg is not None ):
            l1 = self._lines4deg[ 0 ].copy()
            l1._gform = other * l1._gform
            l1._from_origin = l1._gform.copy()
            l2 = self._lines4deg[ 1 ].copy()

            C._lines4deg = ( l1, l2 )
            C._gform = create_conic_from_lines( C._lines4deg )
            C._from_origin = self._gform.copy()
        else:
            C._gform = other * self._gform
            C._from_origin = C._gform.copy()
        return C

    @property
    def is_degenerate( self ) -> bool:
        return False if ( self._lines4deg is None ) else True
    
    @property
    def rank( self ) -> int:
        return self._rank
    
    @property
    def is_fullrank( self ) -> bool:
        nrow, *_ = self._gform.shape
        return True if ( nrow == self._rank ) else False

    @classmethod
    def create_from_array( cls, M: np.ndarray ) -> CConic:
        if ( not isinstance( M, np.ndarray ) ):
            raise CTypeError( M.__class__.__name__ )
        
        # The matrix must be a square matrix.
        nrows, ncols = M.shape
        if ( nrows != ncols ):
            raise CValueError( M.__class__.__name__,
                               f'You can not create a conic from a ({nrows}x{ncols}) matrix.')

        # The matrix must be a 3x3 matrix.
        if ( nrows != 3 ):
            raise CValueError(M.__class__.__name__,
                              f'You can not create a conic from a ({nrows}x{ncols}) matrix. It must be a (3x3) matrix.')

        # Check tolerance.
        M1 = ctol.adjust2relzeros( M )

        # The matrix can not be full of zeros.
        if ( ctol.iszero( float( LA.norm( M1 ) ) ) ):
            raise CValueError(M.__class__.__name__,
                              f'The matrix cannot be filled with zero.')

        # Check to see if the matrix is symmetric.
        if ( is_symmetric( M1 ) == False ):
            raise CValueError(M.__class__.__name__,
                              f'The matrix must be a symmetric matrix.')

        # It is all ok.
        # Get its rank.
        rk = rank( M1 )

        # Is it full rank?
        if ( rk == nrows ):
            C = cls()
            C._gform = M1.copy()
            C._from_origin = M1.copy()
            return C
        
        # It is a degenerate conic.
        l1, l2 = get_lines_from_degenerate_conic( M1 )

        # Create a degenerate conic and return it.
        C = cls( degenerate = ( l1, l2 ) )
        return C
    
    def update_origin( self ) -> None:
        # Translate the origin from ( 0, 0 ) to another origin in '(origin.x, origin.y )'.
        if ( self._lines4deg is not None ):
            self._lines4deg[ 0 ].update_origin()
            self._lines4deg[ 1 ].update_origin()
            self._gform = create_conic_from_lines( self._lines4deg )
        else:
            self._gform = corigin.change_conic( self._gform )

    def copy( self ) -> CConic:
        C = CConic()
        C._rank = self._rank
        C.name = self.name

        if ( self._lines4deg is not None ):
            C._lines4deg = ( self._lines4deg[ 0 ].copy(), self._lines4deg[ 1 ].copy() )
            C._gform = create_conic_from_lines( C._lines4deg )
        else:
            C._gform = self._gform.copy()
        C._from_origin = C._gform.copy()        
        return C

    def sequence( self, x: list[ float ], /,
                  y: list[ float ] | None = None
                ) -> tuple[ tuple[ CPoint, ... ], ... ]:
        # from pyConics.point import CPoint
        
        # Degenerate conic.
        if ( self._lines4deg is not None ):
            lop1 = self._lines4deg[ 0 ].sequence( x )
            lop2 = self._lines4deg[ 1 ].sequence( x )
            return ( lop1, lop2 )

        # Nondegenerate conic.
        if ( y is None ):
            y = x

        nrows = len( y )
        ncols = len( x )
        Vx = np.empty( shape = ( nrows, ncols ) )
        for i in range( 0, nrows):
            for j in range( 0, ncols ):
                _x = np.array( [ x[ j ], y[ i ], 1.0 ] )[np.newaxis].T
                Vx[ i ][ j ] = np.squeeze( _x.T @ self._gform @ _x )

        X, Y = np.meshgrid( x, y )

        _fig = plt.figure( figsize = ( 0, 0 ) )
        _ax = _fig.add_subplot( 111 )
        cs = _ax.contour( X, Y, Vx, levels = [ 0.0 ] )
        plt.close( _fig )

        # Get vertices and codes of the path.
        p = cs.get_paths()[ 0 ]
        v = np.array( p.vertices )
        c = np.array( p.codes )

        # Get the codes equal to Path.MOVETO.
        idx = np.where( c == Path.MOVETO )
        idx = idx[ 0 ]
        if ( idx.size == 0 ):
            return tuple( [] ),

        # Build the lists.
        res = []
        xy = []
        p = CPoint( ( v[ 0 ][ 0 ], v[ 0 ][ 1 ] ), shift_origin = False )
        xy.append( p )
        for i in range( 1, c.size ):
            p = CPoint( ( v[ i ][ 0 ], v[ i ][ 1 ] ), shift_origin = False )

            if ( c[ i ] == Path.MOVETO ):
                res.append( tuple( xy ) )
                xy = []            

            xy.append( p )
        res.append( tuple( xy ) )

        return tuple( res )
    
    def pole( self, l: CLine ) -> CPoint:
        if ( not isinstance( l, CLine ) ):
            raise CTypeError( l.__class__.__name__ )
        p: CPoint = self * l
        return p
    
    def polar( self, p: CPoint ) -> CLine:
        if ( not isinstance( p, CPoint ) ):
            raise CTypeError( p.__class__.__name__ )
        l: CLine = self * p
        return l

    def area( self ) -> float:
        if ( self._rank == 1 ):
            return 0.0
        
        if ( self._rank == 2 ):
            return cconst.inf
        
        A = LA.det( self._gform )
        if ( A < 0.0 ):
            return cconst.pi / np.sqrt( -A )
        return cconst.inf
    
#------------------------------------------------------------------
# Internal functions.
#  

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Keep this imports even there is no test code.
    from pyConics.point import CPoint
    from pyConics.line import CLine
    
    import os
    os.system( 'cls' )

    # Create some conics.
    # WARN: angles must be in radians.
    C0 = CConic( name = 'C0' )
    print( C0, '\n' )

    C1 = CConic( 0.3, 0.5, 30.0 / 180 * cconst.pi, CPoint( ( 0, 0 ) ), 'C1' )
    print( C1, '\n' )

    C2 = CConic( 0.2, name = 'C2', foci = ( CPoint( ( 0, 0.4 ) ), CPoint( ( 0, -0.4 ) ) ) )
    print( C2, '\n' )

    C3 = CConic( degenerate = ( CLine( ( 1.0, -1.0, 0.0 ) ), CLine( ( 1.0, 1.0, 0.0 ) ) ),
                 name = 'C3' )
    print( C3, '\n' )

    C1.update_origin()
    print( C1, '\n' )

    C4 = C3.copy()
    C4.name = 'C3.cp'
    print( C4, '\n' )

    C5 = C1.copy()
    C5.name = 'C1.cp'
    print( C5, '\n' )

    x = np.linspace( -1.2, 1.2, 7 )
    lp1, lp2 = C3.sequence( list( x ) )
    for p in lp1:
        print( p.gform )
    print()
    for p in lp2:
        print( p.gform )
    print()

    print( 'Path codes:' )
    print( f'Path.MOVETO: {Path.MOVETO}' )
    print( f'Path.LINETO: {Path.LINETO}' )
    print( f'Path.CLOSEPOLY: {Path.CLOSEPOLY}' )
    print( f'Path.STOP: {Path.STOP}' )
    print()

    lp = C0.sequence( list( x ) )
    for p in lp[ 0 ]:
        print( p.gform )
    print()

    lp1, lp2 = C1.sequence( list( x ) )
    for p in lp1:
        print( p.gform )
    print()
    for p in lp2:
        print( p.gform )
    print()

    C6 = CConic( name = 'C6' )
    print( C6.is_fullrank )

    p1 = CPoint( ( 1, 0 ), name = 'p1' )
    l1: CLine = C6 * p1
    p: CPoint = C6 * l1
    print( p1, l1, p, sep = '\n' )
    print()

    p2 = CPoint( ( 0, 1 ), name = 'p2' )
    l2: CLine = C6 * p2
    p: CPoint = C6 * l2
    print( p2, l2, p, sep = '\n' )
    print()

    p3 = CPoint( ( np.sqrt(2) / 2, np.sqrt(2) / 2 ), name='p3' )
    l3: CLine = C6 * p3
    p: CPoint = C6 * l3
    print( p3, l3, p, sep = '\n' )
    print()

    print( CPoint( ( 0, 0 ) ) in C6 )
    print( CPoint( ( 1, 1 ) ) in C6 )
    print( p1 in C6 )
    print( p2 in C6 )
    print( p3 in C6 )
    print()

    print( f'The area of {C0.name} is {C0.area()}' )
    print( f'The area of {C1.name} is {C1.area()}' )
    print( f'The area of {C2.name} is {C2.area()}' )
    print( f'The area of {C3.name} is {C3.area()}' )
    print( f'The area of {C4.name} is {C4.area()}' )
    print( f'The area of {C5.name} is {C5.area()}' )
    print( f'The area of {C6.name} is {C6.area()}' )
    print()

    A = np.zeros( shape = ( 2, 3 ) )
    try:
        CConic.create_from_array( A )
    except CValueError as e:
        print( e, '\n' )

    A = np.zeros( shape = ( 2, 2 ) )
    try:
        CConic.create_from_array( A )
    except CValueError as e:
        print( e, '\n' )

    A = np.zeros( shape = ( 3, 3 ) )
    try:
        CConic.create_from_array( A )
    except CValueError as e:
        print( e, '\n' )

    A[ 0, 1 ] = 1.0
    try:
        CConic.create_from_array( A )
    except CValueError as e:
        print( e, '\n' )

    A = C6.copy()
    A.name = 'A'
    B = CConic.create_from_array( A.gform )
    B.name = 'B'
    print( A, '\n' )
    print( B, '\n' )

    l1 = CLine( ( 1, 0, -1 ) )
    l2 = CLine( ( 2, 0, 2 ) )
    A = CConic( degenerate = ( l1, l2 ), name = 'A' )
    B = CConic.create_from_array( A.gform )
    B.name = 'B'
    print( A, '\n' )
    print( B, '\n' )

    l1 = CLine( ( 1, -1, 1 ) )
    l2 = CLine( ( -3, -3, 3 ) )
    A = CConic( degenerate = ( l1, l2 ), name = 'A' )
    B = CConic.create_from_array( A.gform )
    B.name = 'B'
    print( A, '\n' )
    print( B, '\n' )

    l1 = CLine( ( 1, -1, 1 ) )
    A = CConic( degenerate = ( l1, l1 ), name = 'A' )
    B = CConic.create_from_array( A.gform )
    B.name = 'B'
    print( A, '\n' )
    print( B, '\n' )

    # Testing multiplication operator.
    C7 = CConic( name = 'C7 ')
    C8 = 5.0 * C7
    C8.name = 'C8'
    print( C7, '\n' )
    print( '5.0 * C7 =', C8, '\n' )

    l1 = CLine( ( 1, -1, 1 ) )
    l2 = CLine( ( -1, -1, 1 ) )
    C9 = CConic( degenerate = ( l1, l2 ), name = 'C9' )
    C10 = 3.0 * C9
    C10.name = 'C10'
    print( C9, '\n' )
    print( '3.0 * C9 =', C10, '\n' )
    
    # Testing addition operator.
    C11 = C7 + C9
    C11.name = 'C11'
    print( 'C7 + C9 =', C11, '\n' )

    # Testing linear combintion.
    C12 = 5.0 * C7 + 3.0 * C9
    C12.name = 'C12'
    print('5.0 * C7 + 3.0 * C9 =', C12, '\n')

    # Testing equality.
    print( f'Is {C9.name} equals to {C10.name}? {C9 == C10}' )
    print( f'Is {C7.name} equals to {C8.name}? {C7 == C8}' )
    print( f'Is {C9.name} equals to {C8.name}? {C9 == C8}' )
    print( f'Is {C11.name} equals to {C12.name}? {C11 == C12}', '\n' )
    