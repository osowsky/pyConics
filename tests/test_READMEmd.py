#------------------------------------------------------------------
# poetry add --group dev pytest
#

#------------------------------------------------------------------
# Import from...
#

#------------------------------------------------------------------
# Import as...
#

def test_Points():
    from pyConics import Point

    p1 = Point( ( 0.0, 1.0 ), 'p1' ) # p1 = ( 0.0, 1.0 ).
    p2 = Point( ( 1.0, 1.0 ), 'p2' ) # p2 = ( 1.0, 1.0 ).

    print( p1 ) # -> p1: [0.0000e+00 1.0000e+00 1.0000e+00].
    print( p2 ) # -> p2: [1.0000e+00 1.0000e+00 1.0000e+00].
    print()

    print( f'Are p1 and p2 the sames? {p1 == p2}\n' ) # -> False.

    d12 = p1.distance( p2 )
    print( f'Distance from {p1}\nto {p2} is {d12:.4f}.\n' ) # -> d12 = 1.0.

    p3 = Point( ( 1, 1, 0 ), 'p3' ) # Point at the infinity.
    print( p3 ) # -> p3: [1.0000e+00 1.0000e+00 0.0000e+00] -> point at the infinity.
    print()

    print( f'Is p3 a point at the infinity? {p3.at_infinity()}.\n' ) # -> True.

    d13 = p1.distance( p3 )
    print( f'Distance from {p1} to\n{p3} is {d13:.4f}.\n' ) # -> d13 = Inf.

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Test point script for README.md usage.
    print()
    test_Points()
    print()
