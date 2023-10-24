#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'const' ]

#------------------------------------------------------------------
# Import from...
#  
from dataclasses import dataclass

#------------------------------------------------------------------
# Import from...
# We use here TYPE_CHECKING constant to avoid circular import  
# exceptions.
#
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    ... # Do nothing here, because there are no pyConics modules
        # here to be imported.

from pyConics.errors import AttributeError

#------------------------------------------------------------------
# Import as...
#  
import numpy as np

#------------------------------------------------------------------
# Data Class CConstants.
#  
@dataclass
class CConstants:
    _inf: float = np.Inf
    _pi : float = np.pi

    @property
    def inf( self ) -> float:
        return self._inf
    
    @property
    def pi( self ) -> float:
        return self._pi
    

#--------------------------------------------------------------
# Global variable.
#
const = CConstants()

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    print( f'The value of infinity is {const.inf}' )
    print( f'Is infinity equals to 0.0? {const.inf == 0.0}' )

    print( f'The value of pi is {const.pi:.6f}' )
