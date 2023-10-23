#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'CAxes' ]

#------------------------------------------------------------------
# Import from ...
#  
from matplotlib import pyplot as plt

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
import numpy as np

#------------------------------------------------------------------
# Class CFigure.
#  
class CAxes:
    def __init__( self, axes: plt.Axes ) -> None: #type: ignore
        self._axes = axes
        self._xres = 1000
        self._yres = 1000

    def __repr__( self ) -> str:
        return f'{self.__class__.__name__} class.'

    def get_pyplot_axes( self ) -> plt.Axes: #type: ignore
        return self._axes

    @property
    def xlim( self ) -> tuple[ float, float ]:
        return self._axes.get_xlim()
     
    @xlim.setter
    def xlim( self, xl: tuple[ float, float ] ) -> None:
        self._axes.set_xlim( xl )

    @property
    def ylim( self ) -> tuple[ float, float ]:
        return self._axes.get_ylim()
    
    @ylim.setter
    def ylim( self, yl: tuple[ float, float ] ) -> None:
        self._axes.set_ylim( yl )
    
    @property
    def xticks( self ) -> np.ndarray:
        return self._axes.get_xticks()
    
    @xticks.setter
    def xticks( self, xt: np.ndarray ) -> None:
        self._axes.set_xticks( xt )

    @property
    def yticks( self ) -> np.ndarray:
        return self._axes.get_yticks()
    
    @yticks.setter
    def yticks( self, yt: np.ndarray ) -> None:
        self._axes.set_yticks( yt )

    @property
    def resolution( self ) -> tuple[ int, int ]:
        return ( self._xres, self._yres )
    
    def plot( self, *args, scalex = True, scaley = True, data = None, **kwargs ) -> None:
        self._axes.plot( *args, scalex, scaley, data, **kwargs ) # type: ignore

#------------------------------------------------------------------
# For development and test.
#  
if ( __name__  == '__main__' ):
    ...
