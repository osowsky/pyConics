#------------------------------------------------------------------
# Import it to be able to pass an object of same class as argument
# to a member function
from __future__ import annotations

#------------------------------------------------------------------
# Everything that can be visible to the world.
#  
__all__ = [ 'cofactor', 'minor', 'rank', 'is_symmetric',
            'real_eigenvecs', 'real_eigenvals' ]

#------------------------------------------------------------------
# Import from...
#
from numpy import linalg as LA

#------------------------------------------------------------------
# Import from...
# We use here TYPE_CHECKING constant to avoid circular import  
# exceptions.
#
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    ... # Do nothing here, because there are no pyConics modules
        # here to be imported.

from pyConics.tolerance import ctol
from pyConics.errors import CValueError

#------------------------------------------------------------------
# Import as...
#
import numpy as np

def is_symmetric( M: np.ndarray ) -> bool:
    return np.allclose( M, M.T )

def rank( M: np.ndarray ) -> int:
    nrows, ncols = M.shape
    if ( nrows != ncols ):
        return 0

    n = LA.norm( M )
    if ( ctol.iszero( float( n ) ) ):
        return 0

    if ( not ctol.iszero( LA.det( M ) ) ):
        return nrows

    # Calc rank by using the eigenvalues.
    if ( is_symmetric( M ) ):
        eigs = LA.eigvalsh( M )
    else:
        eigs = LA.eigvals( M )
    eigs = ctol.adjust2relzeros( eigs )
    rk: int = 0
    for ev in eigs:
        if ( ev != 0.0 ):
            rk += 1
    return rk

def minor( M: np.ndarray, row: int, col: int ) -> float:
    nrows, ncols = M.shape
    if (nrows != ncols):
        raise CValueError( M.__class__.__name__,
                          f'The matrix must be symmetric.' )
    n = nrows

    rows = []
    cols = []
    for i in range( n ):
        for j in range( n ):
            if ( i == row ):
                continue
            if ( j == col ):
                continue

            rows.append( i )
            cols.append( j )
    ind = ( np.array( rows ), np.array( cols ) )
    M1 = M[ ind[ 0 ], ind[ 1 ] ].reshape( ( n - 1, n - 1 ) )

    d = LA.det( M1 )
    return 0.0 if ( ctol.iszero( d ) ) else d

def cofactor( M: np.ndarray ) -> np.ndarray:
    nrows, ncols = M.shape
    if ( nrows != ncols ):
        raise CValueError( M.__class__.__name__,
                          f'The matrix must be symmetric.' )
    n = nrows

    C = np.ndarray( shape = M.shape, dtype = np.double )
    for i in range( n ):
        for j in range( n ):
            C[ i ][ j ] = ( ( -1.0 ) ** ( i + j ) ) * minor( M, i, j )
    return ctol.adjust2relzeros( C )

def real_eigenvals( M: np.ndarray ) -> tuple[ float, ...]:
    eigenvalues, *_ = LA.eig( M )
    
    # Are the eigenvalues zero?
    eigs = np.zeros( shape = ( eigenvalues.size ), dtype = np.double )
    for i, e in enumerate( eigenvalues ):
        if ( ctol.iszero( float( LA.norm( e ) ) ) ):
            continue

        z = complex( e )
        if ( ctol.is_real( z ) ):
            eigs[ i ] = z.real
    return tuple( eigs )

def real_eigenvecs( M: np.ndarray ) -> tuple[ tuple[ float, ...], ...]:
    eigenvalues = real_eigenvals( M )
    *_, eigenvectors = LA.eig( M )

    # Check only the real eigenvalues.
    evec = []
    for i, e in enumerate( eigenvalues ):
        eigs = np.zeros( shape = ( len( eigenvalues ) ), dtype = np.double )
        if ( e == 0.0 ):
            evec.append( tuple( eigs ) )
            continue
        
        # v must be assessed.
        v = eigenvectors[ :, i ]
        for j in range( v.size ):
            z = complex( v[ j ] )
            if ( ctol.is_real( z ) == False ):
                eigs = np.zeros( shape = ( len( eigenvalues ) ), dtype = np.double )
                break
            else:
                eigs[ j ] = z.real
        evec.append( tuple( eigs ) )

    return tuple( evec )

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Testing rank function.
    A = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}' )
    A = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[1, 0, 0], [2, 0, 0], [0, 0, 0]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[1, 0, 0], [2, 0, 0], [3, 0, 0]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[0, 0, 1], [0, 0, 2], [0, 0, 3]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[0, 0, 1], [2, 0, 0], [3, 0, 0]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[1, 2, 0], [2, 4, 0], [3, 6, 0]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[1, 2, 0], [2, 4, 0], [0, 0, 5]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[1, 2, 0], [1, 3, 0], [0, 0, 5]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array([[0, 0, 1], [0, 0, 2], [4, 4, 0]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    A = np.array( [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] )
    print( f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}' )
    A = np.array([[40, -17, 166], [-17, -20, -125], [166, -125, 580]])
    print(f'Rank of Matrix A: {rank( A )} --- Det of A: {LA.det( A ):.2f} --- Is symmetric: {is_symmetric( A )}')
    print()

    # Testing minor function.
    A = np.array( [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] )
    for i in range( 3 ):
        for j in range( 3 ):
            print( f'Minor of ( { i }, { j } ) is {minor( A, i, j ):.2f}' )
    print()

    # Testing cofactor matrix.
    C = cofactor( A )
    print( C, '\n' )
    
    # Testing real eigenvalues and real eigenvectors.
    A = np.array( [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] )
    eigs = real_eigenvals( A )
    print( f'Real eigenvalues: {eigs} --- Rank: {LA.matrix_rank( A )}' )
    eigs = real_eigenvecs(A)
    print('Real eigenvectors:', *eigs, sep='\n')
    print()

    A = np.array( [ [ 1, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ] ] )
    eigs = real_eigenvals( A )
    print( f'Real eigenvalues: {eigs} --- Rank: {LA.matrix_rank( A )}' )
    eigs = real_eigenvecs(A)
    print('Real eigenvectors:', *eigs, sep='\n')
    print()

    A = np.array( [ [ 1, 1, 0 ], [ 0, 1, 1 ], [ 1, 0, 1 ] ] )
    eigs = real_eigenvals( A )
    print(f'Real eigenvalues: {eigs} --- Rank: {LA.matrix_rank( A )}', )
    eigs = real_eigenvecs( A )
    print( 'Real eigenvectors:', *eigs, sep='\n' )
    print()
