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

    # Used for internal development and test.
    if __name__ == '__main__':
        print( f'Git version  = {ver_git}' )
        print( f'pyPI version = {ver_pypi}' )
        return ver_git == ver_pypi

    # Used for pytest
    assert ver_git == ver_pypi

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Test for to see if git version is equal to pyPI version.
    print( f'Git version is equal to pyPI version? {test_version()}\n' )
    p1 = Point( ( 0, 1 ) )
    p1.are_coincident( p1 )
