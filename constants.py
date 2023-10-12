#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'const' ]

#------------------------------------------------------------------
# Import from...
#  
from dataclasses import dataclass
from os.path import basename, splitext

if ( __name__ == '__main__' ) or \
    ( __name__ == splitext( basename( __file__ ) )[ 0 ] ):
    from errors import AttributeError
else:
    from .errors import AttributeError

#------------------------------------------------------------------
# Import as...
#  
import numpy as np

#------------------------------------------------------------------
# Data Class Origin.
#  
@dataclass
class Constants:
    _inf: float = np.Inf
    _pi : float = np.pi

    @property
    def inf( self ) -> float:
        return self._inf
    
    @inf.setter
    def inf( self, inf_number: float ) -> None:
       raise AttributeError( self.__class__.__name__, Constants.inf.fset.__name__ )
    
    @property
    def pi( self ) -> float:
        return self._pi
    
    @pi.setter
    def pi( self, pi_number: float ) -> None:
       raise AttributeError( self.__class__.__name__, Constants.pi.fset.__name__ )
    

#--------------------------------------------------------------
# Global variable.
#
const = Constants()

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    print( f'The value of infinity is {const.inf}' )
    print( f'Is infinity equals to 0.0? {const.inf == 0.0}' )
    try:
        const.inf = 0.0
    except AttributeError as e:
        print( e )
    
    print( f'The value of pi is {const.pi:.6f}' )
    try:
        const.pi = 0.0
    except AttributeError as e:
        print( e )
    