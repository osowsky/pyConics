#------------------------------------------------------------------
# poetry add --group dev pytest
#

#------------------------------------------------------------------
# Import from...
#
from pyConics import CPoint, CLine, origin

#------------------------------------------------------------------
# Import as...
#
import pyConics as con
import subprocess as sp
import numpy as np

def _get_git_version() -> str:
    r = sp.run( [ 'git', 'tag' ], capture_output = True, text = True )
    ver_list = r.stdout.splitlines()
    while ( len( ver_list[ -1 ] ) == 0 ):
        l = len( ver_list[ -1 ] )
        ver_list = ver_list[ 0 : l - 1 ]

    ver_full = ver_list[ -1 ]
    ver = ''
    for dig in ver_full:
        if ( dig in '01234567890.' ):
            ver += dig
            continue

        if ( dig == '-' ):
            break

    return ver


def test_version():
    ver_git = _get_git_version()
    ver_pypi = con.__version__

    # Used for internal development and test.
    if __name__ == '__main__':
        # You can see the result.
        print( f'Git version  = {ver_git}' )
        print( f'pyPI version = {ver_pypi}' )
        print( f'Git version is equal to pyPI version? {ver_git == ver_pypi}' )

    # Used for pytest.
    assert ver_git == ver_pypi

def test_cconst():
    from pyConics import cconst

    assert cconst.inf == np.Inf
    assert cconst.pi == np.pi
    assert cconst.titlesize == 9
    assert cconst.labelsize == 8
    assert cconst.tickssize == 8
    assert cconst.textsize  == 10
    print( 'Global variable cconst is ok.' )

def test_ctol():
    from pyConics import ctol

    assert ctol.eps_iszero == 1e-4
    assert ctol.eps_relzero == 1e-5
    print( 'Global variable ctol is ok.' )

def test_origin():
    # Points.
    p1 = CPoint( ( 1, 3 ), 'p1' )
    p2 = CPoint( ( 0, 4 ), 'p2' )
    p3 = CPoint( ( -2, 0 ), 'p3' )
    p4 = CPoint( ( 2, 0 ), 'p4' )
    p5 = CPoint( ( 0, -4 ), 'p5' )

    # Lines.
    l1 = p2 * p3
    l2 = p4 * p5
    l3 = CLine( ( 2, 1, 0 ), 'l3' )
    l4 = CLine( ( 1, 0, -2 ), 'l4' )
    l5 = CLine( ( 0, 1, -4 ), 'l5' )
    l6 = CLine( ( 1, -1, 0 ), 'l6' )

    # assert p1 == p2

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Test to check if git version is equal to pyPI version.
    print()
    test_version()
    print()

    # Test to check if global variable cconst is ok.
    test_cconst()
    print()

    # Test to check if global variable ctol is ok.
    test_ctol()
    print()

    # Test to check if he shift of origin is working well.
    test_origin()
    print()
