#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'AttributeError', 'TypeError', 'PointTypeError', 'LineTypeError' ]

#------------------------------------------------------------------
# Child Class AttributeError.
#  
class AttributeError( AttributeError ):
    ...
    def __init__( self, *args ) -> None:
        class_name, attrib_name = args
        self.args = ( f'{self.__class__.__name__}: You can not assing a value to {class_name}.{attrib_name} attribute.', )

#------------------------------------------------------------------
# Child Class TypeError.
#  
class TypeError( TypeError ):
    ...
    def __init__( self, *args ) -> None:
        class_name, *_ = args
        self.args = ( f'{self.__class__.__name__}: You can not use a \'{class_name}\' type as argument for this function.', )

#------------------------------------------------------------------
# Child Class PointTypeError.
#  
class PointTypeError( TypeError ):
    ...
    def __init__( self, *args ) -> None:
        class_name, attrib_name = args
        self.args = ( f'{self.__class__.__name__}: Size mismatch. {class_name}.{attrib_name} attribute gets a tuple with length of 2 or 3.', )
 
#------------------------------------------------------------------
# Child Class LineTypeError.
#  
class LineTypeError( TypeError ):
    ...
    def __init__( self, *args ) -> None:
        class_name, attrib_name = args
        self.args = ( f'{self.__class__.__name__}: Size mismatch. {class_name}.{attrib_name} attribute gets a tuple with length of 3.', )
 
