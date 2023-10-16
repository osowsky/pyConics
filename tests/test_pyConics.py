#------------------------------------------------------------------
# poetry add --group dev pytest
#

#------------------------------------------------------------------
# Import from...
#
from pyConics import Point, Line, origin

#------------------------------------------------------------------
# Import as...
#
import pyConics as con
import subprocess as sp

def _get_git_version() -> str:
    r = sp.run( [ 'git', 'tag' ], capture_output = True, text = True )
    ver = r.stdout[ ::-1 ]
    v_end   = ver.find( '-' )
    v_start = ver.find( 'v' )
    ver = ver[ v_end + 1 : v_start ]
    ver = ver[ ::-1 ]
    return ver


def test_version():
    ver_git = _get_git_version()
    ver_pypi = con.__version__

    # Test it.
    res = ver_git == ver_pypi

    # Used for internal development and test.
    if __name__ == '__main__':
        # You can see the result.
        print( f'Git version  = {ver_git}' )
        print( f'pyPI version = {ver_pypi}' )
        print( f'Git version is equal to pyPI version? {res}' )

    # Used for pytest.
    assert res

def test_origin():
    # Points.
    p1 = Point( ( 1, 3 ), 'p1' )
    p2 = Point( ( 0, 4 ), 'p2' )
    p3 = Point( ( -2, 0 ), 'p3' )
    p4 = Point( ( 2, 0 ), 'p4' )
    p5 = Point( ( 0, -4 ), 'p5' )

    # Lines.
    l1 = p2 * p3
    l2 = p4 * p5
    l3 = Line( ( 2, 1, 0 ), 'l3' )
    l4  = Line( ( 1, 0, -2 ), 'l4' )
    l5 = Line( ( 0, 1, -4 ), 'l5' )
    l6 = Line( ( 1, -1, 0 ), 'l6' )

    assert p1 == p2

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Test to check if git version is equal to pyPI version.
    print()
    test_version()
    print()
    test_origin()
    print()
