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
from pyConics.errors import CConicTypeError
from pyConics.origin import corigin
from pyConics.tolerance import ctol
from pyConics.conics.utils import create_conic_from_lines, create_conic
from pyConics.conics.utils import rank

#------------------------------------------------------------------
# Import as...
#
import numpy as np
np.set_printoptions( formatter = { 'float': lambda x: "{0:0.4e}".format( x ) } )

#------------------------------------------------------------------
# Class CConic.
#  
class CConic( CAGObj ):
    from pyConics.point import CPoint
    from pyConics.line import CLine

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
        from pyConics.point import CPoint

        # Precedence for creating the conic:
        # 1) First: the parameter degenerate was defined.
        # 2) Second: the parameter foci, and a were defined.
        # 3) Third: the parameters a, c, center and angle were defined.
        # 4) Fourth: if no parameter was defined, then a circle is created.
        super().__init__( name )

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
                f1: CPoint = foci[ 0 ]
                f2: CPoint = foci[ 1 ]
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

        # Get the matrix rank.
        self._rank = rank( self._gform )

    def __repr__( self ) -> str:
        # # return an info messsage for this class.
        info = f'{self.name}: ( x, y ) | [ x y 1 ] *\n{self.gform} * [ x y 1 ].T = 0'
        return info

    @property
    def is_degenerate( self ) -> bool:
        return False if ( self._lines4deg is None ) else True
    
    @property
    def rank( self ) -> int:
        return self._rank
    
    def is_fullrank( self ) -> bool:
        nrow, *_ = self._gform.shape
        return True if ( nrow == self._rank ) else False

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
            C._lines4deg = self._lines4deg
            C._gform = create_conic_from_lines( C._lines4deg )
        else:
            C._gform = self._gform.copy()
        
        return C

    def sequence( self, x: list[ float ], /,
                  y: list[ float ] | None = None
                ) -> tuple[ tuple[ CPoint, ... ], ... ]:
        from pyConics.point import CPoint
        
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
            return ( tuple( [] ), tuple( [] ) )

        # Build the lists.
        xy1 = []
        xy2 = []
        if ( idx.size == 1 ):
            for _xy in v:
                p = CPoint( ( _xy[ 0 ], _xy[ 1 ] ), shift_origin = False )
                xy1.append( p )
        elif ( idx.size == 2 ):
            for _xy in v[ idx[ 0 ] : idx[ 1 ] ]:
                p = CPoint( ( _xy[ 0 ], _xy[ 1 ] ), shift_origin = False )
                xy1.append( p )
            for _xy in v[ idx[ 1 ] : ]:
                p = CPoint((_xy[0], _xy[1]), shift_origin=False)
                xy2.append( p )
    
        return ( tuple( xy1 ), tuple( xy2 ) )

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

    lp1, lp2 = C0.sequence( list( x ) )
    for p in lp1:
        print( p.gform )
    print()
    for p in lp2:
        print( p.gform )
    print()

    lp1, lp2 = C1.sequence( list( x ) )
    for p in lp1:
        print( p.gform )
    print()
    for p in lp2:
        print( p.gform )
    print()
