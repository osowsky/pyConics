#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'origin' ]

#------------------------------------------------------------------
# Import from...
#  
from dataclasses import dataclass

#------------------------------------------------------------------
# Import as...
#  
import numpy as np

#------------------------------------------------------------------
# Data Class Origin.
#  
@dataclass
class Origin:
    x: float = 0.0
    y: float = 0.0

    def change_point( self, point: np.ndarray ) -> np.ndarray:
        return point - np.array( ( self.x, self.y, 0.0 ) )
    
    def change_line( self, line: np.ndarray ) -> np.ndarray:
        c = ( line[ 0 ] * self.x ) - self.y
        return line + np.array( ( 0.0, 0.0, c ) )

    def reset( self ) -> None:
        self.x = 0.0
        self.y = 0.0

#--------------------------------------------------------------
# Global variable.
#
origin = Origin()
