#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'CFigure' ]

#------------------------------------------------------------------
# Import from ...
#  
from pyConics.errors import ValueError
from matplotlib import pyplot as plt
from pyConics.plotting.axes import CAxes

#------------------------------------------------------------------
# Import from...
# We use here TYPE_CHECKING constant to avoid circular import  
# exceptions.
#
from typing import TYPE_CHECKING
if TYPE_CHECKING:
   ... # Do nothing here, because there are no pyConics modules
       # here to be imported.    

#------------------------------------------------------------------
# Import as ...
#  
import pyautogui as gui
import matplotlib as mpl
import numpy as np

#------------------------------------------------------------------
# Class CFigure.
#  
class CFigure:
    def __init__( self, size: tuple[ float, float ] = ( 0.0, 0.0 ), unit: str = '' ) -> None:
        self._axes: list[ CAxes ] = []

        w, h = size
        if ( size == ( 0.0, 0.0 ) ):
            self._fig = plt.figure( layout = 'constrained' )
        elif ( unit == 'inche' ):
            if ( w == 0.0 ):
                w = h
            elif ( h == 0.0 ):
                h = w
            self._fig = plt.figure( figsize = ( w, h ), layout = 'constrained' )
        elif ( unit == '' ):
            if ( ( abs( w ) > 1.0 ) or ( abs( h ) > 1.0 ) ):
                raise ValueError( self.__class__.__name__, 'when unit=\'\', size argument must not be greater than 1.' )
            if ( w == 0.0 ):
                w = h
            elif ( h == 0.0 ):
                h = w
            width, height = gui.size()
            dpi = mpl.rcParams[ 'figure.dpi' ]
            w = round( w * ( width / dpi ), 1 )
            h = round( h * ( height / dpi ), 1 )
            self._fig = plt.figure( figsize = ( w, h ), layout = 'constrained' )
        else:
            raise ValueError( self.__class__.__name__, 'unit argument must be either an empty string or \'inche\'.' )

    def __repr__( self ) -> str:
        l = len( self._axes )
        return f'{self.__class__.__name__} class with {l} CAxes classes.'

    @staticmethod
    def show( blocking: bool = True ) -> None:
        plt.show( block = blocking )

    def get_pyplot_figure( self ) -> plt.Figure: #type: ignore
        return self._fig

    def get_pyplot_axes( self ) -> list[ plt.Axes ]: #type: ignore
        return self._fig.get_axes()

    @property
    def axes( self ) -> list[ CAxes ]:
        return self._axes

    def create_axes( self, n_axes: tuple[ int, int ] = ( 1, 1 ) ):
        self._fig.subplots( n_axes[ 0 ], n_axes[ 1 ] )

        for ax in self._fig.axes:
            # Set some properties of the axes.
            ax.grid( visible = True, which = 'both', axis = 'both' )
            ax.axis( 'scaled' ) # it works better than 'equal'.
            ax.set_xlim( ( 0.0, 1.0 ) )
            ax.set_ylim( ( 0.0, 1.0 ) )
            ax.set_xticks( np.round( np.linspace( 0, 1, 11 ), 1 ) )
            ax.set_yticks( np.round( np.linspace( 0, 1, 11 ), 1 ) )
            ax.tick_params( axis = 'x', labelsize = 8 )
            ax.tick_params( axis = 'y', labelsize = 8 )
            ax.set_xlabel( 'x-axis', fontsize = 8 )
            ax.set_ylabel( 'y-axis', fontsize = 8 )
            ax.set_title( 'axes title', fontsize = 9 )

            # Create a CAxes class for each axes.
            self._axes.append( CAxes( ax ) )

    def update_canvas( self ) -> None:
        self._fig.canvas.draw()
        self._fig.canvas.flush_events()


#------------------------------------------------------------------
# For development and test.
#  
if ( __name__  == '__main__' ):
    # Create figures.
    # f1 = CFigure( size = ( 6.4, 4.8 ), unit = 'inche' )
    # print( f1 )
    width = 0.35
    f2 = CFigure( (width, 16.0 / 9.0 * width ) )

    # Get the pyPlot's Figure class.
    pp_fig2 = f2.get_pyplot_figure()

    # Create the axes from f2.
    f2.create_axes( ( 2, 2 ) )
    print( f2 )

    # Get a list of CAxes class.
    axes = f2.axes
    print( axes )
    for ax in axes:
        print( ax )
        print( ax.get_pyplot_axes() )

    # Get a list of pyPlot's Axes class.
    # print( f2.get_pyplot_axes() )
    # print( pp_fig2.get_axes() )

    # Display all Figures.
    CFigure.show( False )

    # Change the x- and y-axis limits of axes[ 0 ].
    axes[ 0 ].xlim = ( 0, 2 )
    axes[ 0 ].ylim = ( -1, 1 )
    input( 'Press any key to continue...' )

    # Change the x- and y-ticks of axes[ 0 ].
    xtick = np.linspace( 0, 2, 11 )
    ytick = np.linspace( -1, 1, 11 )
    axes[ 0 ].xticks = xtick
    axes[ 0 ].yticks = ytick

    # Redraw all figure to update its canvas.
    f2.update_canvas()
    input( 'Press any key to continue...' )

    # Plot a point and a line on axes[ 0 ].
    x = 1.0
    y = 0.0
    axes[ 0 ].plot( x, y, 'ob', markersize = 12 )
    f2.update_canvas()
    x = np.linspace( 0, 2, 11 )
    y = -x + 1
    axes[ 0 ].plot( x, y, 'r-', linewidth = 0.5 )
    f2.update_canvas()
    input( 'Press any key to continue...' )

    # Plot a line on axes[ 3 ].
    x = np.linspace( 0.0, 1.0, 11 )
    y = x
    axes[ 3 ].plot( x, y, 'sr-', linewidth = 2, markersize = 8 )
    f2.update_canvas()
    input( 'Press any key to continue...' )
