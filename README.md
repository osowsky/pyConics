# pyConics

`pyConics` handles points, lines and conics by using algebraic geometry
 and homogeneous coordinates.

## Installation

From a local directory clones this project:

```bash
git clone https://github.com/osowsky/pyConics.git (by using http)
or
git clone git@github.com:osowsky/pyConics.git (by using ssh)
```

You can install this package, as well:

```bash
pip install pyConics
```

## Usage

`pyConics` can be used to handle points, lines and conics by using algebraic
geometry and homogeneous coordinates.

### Working with points

The representation in homogeneous coordinates of a Cartesian point
$\,p = (\,\alpha\,,\,\beta\,)$, where $\alpha,\;\beta\;\in\;\mathcal{R}$,
is given by the following vector in $\mathcal{R}^3$:

$$
p\,=\left[\begin{array}{cc}
\alpha & \beta & 1.0
\end{array}\right]^{T}
$$

If you wanted to represent a point $p$ at infinity, you would define a
vector as follows:
$$
p\,=\left[\begin{array}{cc}
\alpha & \beta & 0.0
\end{array}\right]^{T},
$$
where $\alpha,\;\beta\;\in\;\mathcal{R}$

How to work with points in `pyConics`.

```python
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
```

### Working with lines

```python
from pyConics import Line

l1 = Line( ( 1, -1, 1 ), 'l1' )    # l1: y = x + 1.
l2 = Line( ( 1, -1, -1 ), 'l2' )   # l2: y = x - 1
l3 = Line( ( -1, -1, 1 ), 'l3' )   # l3: y = -x + 1
l4 = Line( ( -2, -2, 2 ), 'l4' )   # l4: 2y = -2x + 2 -> l4 = l3

print( l1 ) # -> l1: ( x, y ) | [1.0000e+00 -1.0000e+00 1.0000e+00] * [ x y 1 ]' = 0.
print( l2 ) # -> l2: ( x, y ) | [1.0000e+00 -1.0000e+00 -1.0000e+00] * [ x y 1 ]' = 0.
print( l3 ) # -> l3: ( x, y ) | [-1.0000e+00 -1.0000e+00 1.0000e+00] * [ x y 1 ]' = 0.
print( l4 ) # -> l4: ( x, y ) | [-2.0000e+00 -2.0000e+00 2.0000e+00] * [ x y 1 ]' = 0.
print()












print( f'Are p1 and p2 the same? {p1 == p2}\n' ) # -> False.

d12 = p1.distance( p2 )
print( f'Distance from {p1}\nto {p2} is {d12:.4f}.\n' ) # -> d12 = 1.0.

p3 = Point( ( 1, 1, 0 ), 'p3' ) # Point at the infinity.
print( p3 ) # -> p3: [1.0000e+00 1.0000e+00 0.0000e+00] -> point at the infinity.
print()

print( f'Is p3 a point at the infinity? {p3.at_infinity()}.\n' ) # -> True.

d13 = p1.distance( p3 )
print( f'Distance from {p1} to\n{p3} is {d13:.4f}.\n' ) # -> d13 = Inf.
```

## Contributing

Interested in contributing? Check out the contributing guidelines.
Please note that this project is released with a Code of Conduct.
By contributing to this project, you agree to abide by its terms.

## License

`pyConics` was created by Jefferson Osowsky.
It is licensed under the terms of the GNU General Public License v3.0 license.

## Credits

`pyConics` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/)
and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
