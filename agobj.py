#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'AGObj' ]

#------------------------------------------------------------------
# Import from...
#  
from abc import ABC, abstractmethod
from varname import varname
from errors import AttributeError

#------------------------------------------------------------------
# Import as...
#  
import numpy as np

#------------------------------------------------------------------
# Abstract Base Class AGObj.
#  
class AGObj( ABC ):
    @abstractmethod
    def __init__( self, name: str = '' ) -> None:
        self.name = name

        # The AGObject has a name.
        if ( len( self.name ) == 0 ):
            # A name has not given yet.
            self.name = str( varname( frame = 2 ) )
            

        # Create a zero-dimensional array that will represent
        # a geometric form such as point, line and conics.
        # Each child class will redim this array.
        self._gform = np.ndarray( shape = ( 0, 0 ) )
        
        # Save the original geo form. So, we are able
        # to return its value from origin.
        self._from_origin =  np.ndarray( shape = ( 0, 0 ) )

    @abstractmethod
    def __repr__( self ) -> str:
        # Each child class will implement this method.
        return super().__repr__()
    
    @abstractmethod
    def update_origin( self ) -> None:
        # Each child class will implement this method.
        pass # Do nothing.

    @abstractmethod
    def cross( self, other ):
        pass

    @abstractmethod
    def __mul__( self, other ):
        pass

    @property
    def name( self ) -> str:
       return self._name
    
    @name.setter
    def name( self, name: str ) -> None:
       self._name = name

    @property
    def gform( self ) -> np.ndarray:
       return self._gform
    
    @gform.setter
    def gform( self, gform: np.ndarray ) -> None:
       raise AttributeError( self.__class__.__name__, AGObj.gform.fset.__name__ )

    @property
    def from_origin( self ) -> np.ndarray:
       return self._from_origin
    
    @from_origin.setter
    def from_origin( self, from_origin: np.ndarray ) -> None:
       raise AttributeError( self.__class__.__name__, AGObj.from_origin.fset.__name__ )
