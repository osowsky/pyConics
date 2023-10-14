#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'AttributeError', 'TypeError', 'PointTypeError', 'LineTypeError', 'ArgumentsError' ]

#------------------------------------------------------------------
# Child Class AttributeError.
#  
class AttributeError( AttributeError ):
    def __init__( self, *args ) -> None:
        super().__init__( self, args )

        class_name, attrib_name = args
        self.args = ( f'{self.__class__.__name__}: You can not assing a value to {class_name}.{attrib_name} attribute.', )

#------------------------------------------------------------------
# Child Class TypeError.
#  
class TypeError( TypeError ):
    def __init__( self, *args ) -> None:
        super().__init__( self, args )

        class_name, *_ = args
        self.args = ( f'{self.__class__.__name__}: You can not use a \'{class_name}\' type as argument for this function.', )

#------------------------------------------------------------------
# Child Class PointTypeError.
#  
class PointTypeError( TypeError ):
    def __init__( self, *args ) -> None:
        super().__init__( self, args )

        class_name, attrib_name = args
        self.args = ( f'{self.__class__.__name__}: Size mismatch. {class_name}.{attrib_name} attribute gets a tuple with length of 2 or 3.', )
 
#------------------------------------------------------------------
# Child Class LineTypeError.
#  
class LineTypeError( TypeError ):
    def __init__( self, *args ) -> None:
        super().__init__( self, args )

        class_name, attrib_name = args
        self.args = ( f'{self.__class__.__name__}: Size mismatch. {class_name}.{attrib_name} attribute gets a tuple with length of 3.', )
 
#------------------------------------------------------------------
# Child Class ArgumentsError.
#  
class ArgumentsError( Exception ):
    def __init__( self, *args ) -> None:
        super().__init__( self, args )

        fnc_name, *class_names = args
        sz_text = ''
        length = len( class_names )
        for i, name in enumerate( class_names, start = 1 ):
            if ( i == length - 1 ):
                sz_text += str( name ) + ' and '
            elif ( i == length ):
                sz_text += str( name )
            else:
                sz_text += str( name ) + ', '

        self.args = ( f'{self.__class__.__name__}: You can not pass {sz_text} types as arguments to the \'{fnc_name}\' function/method.', )