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

    print( f'Are p1 and p2 the same? {p1 == p2}\n' ) # -> False.

    d12 = p1.distance( p2 )
    print( f'Distance from {p1}\nto {p2} is {d12:.4f}.\n' ) # -> d12 = 1.0.

    p3 = Point( ( 1, 1, 0 ), 'p3' ) # Point at the infinity.
    print( p3 ) # -> p3: [1.0000e+00 1.0000e+00 0.0000e+00] -> point at the infinity.
    print()

    print( f'Is p3 a point at infinity? {p3.at_infinity()}.\n' ) # -> True.

    d13 = p1.distance( p3 )
    print( f'Distance from {p1} to\n{p3} is {d13:.4f}.\n' ) # -> d13 = Inf.

def test_Lines():
    from pyConics import Line

    l1 = Line( ( 1, -1, 1 ), 'l1' )          # l1: y = x + 1
    l2 = Line( ( 1.5, -1.5, -1.5 ), 'l2' )   # l2: 1.5y = 1.5x - 1.5
    l3 = Line( ( -1, -1, 1 ), 'l3' )         # l3: y = -x + 1
    l4 = Line( ( -2, -2, 2 ), 'l4' )         # l4: 2y = -2x + 2

    print( l1 ) # -> l1: ( x, y ) | [1.0000e+00 -1.0000e+00 1.0000e+00] * [ x y 1 ]' = 0.
    print( l2 ) # -> l2: ( x, y ) | [1.5000e+00 -1.5000e+00 -1.5000e+00] * [ x y 1 ]' = 0.
    print( l3 ) # -> l3: ( x, y ) | [-1.0000e+00 -1.0000e+00 1.0000e+00] * [ x y 1 ]' = 0.
    print( l4 ) # -> l4: ( x, y ) | [-2.0000e+00 -2.0000e+00 2.0000e+00] * [ x y 1 ]' = 0.
    print()

    # The relationships between two lines lx and ly can be:
    # 1) coincident lines: lx == ly or lx.are_coincident( ly ).
    #    Notice that l4 = 2 * l3. From the projective geometry both lines are
    #    coincident because they satisfy the same equation. 
    print( f'Is l1 == l1? {l1 == l1}.' )
    print( f'Is l3 == l4? {l3 == l4}\n.' )
    # 2) 


    print()

    # Lines at infinity.
    l5 = Line( ( 0, 0, 2 ), 'l5' )
    l6 = Line( ( 1, -1, 1 ), 'l6' )
    print( l5 )
    print( l6 )
    print( f'Is l5 a line at infinity? {l5.at_infinity()}.' )
    print( f'Is l6 a line at infinity? {l6.at_infinity()}.\n' )

    # Distance from l5 at the infinity and l6.
    d56 = l5.distance( l6 )
    print( f'Distance from {l5} to {l6} is {d56}.\n' )

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Test point script for README.md usage.
    print()
    test_Points()
    print()
    test_Lines()
    print()
