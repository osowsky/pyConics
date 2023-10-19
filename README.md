# pyConics

`pyConics` handles points, lines and conics by using algebraic geometry
 and homogeneous coordinates (projective geometry).

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
$p = (\enspace\alpha,\enspace\beta\enspace)$, where
$\alpha,\enspace\beta\enspace\in\enspace\mathcal{R}$,
is given by the following vector in $\mathcal{R}^3$:

$$
p=\left[\begin{array}{cc}
\enspace\alpha & \beta & 1.0\enspace
\end{array}\right]^{T}
$$

If you want to represent a point $p$ at infinity, you must define a
vector as follows:

$$
p=\left[\begin{array}{cc}
\enspace\alpha & \beta & 0.0\enspace
\end{array}\right]^{T},
$$

where $\enspace\alpha,\enspace\beta\enspace\in\enspace\mathcal{R}$

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

The representation in homogeneous coordinates of a Cartesian line
$l:\beta y=\alpha x + \gamma$, where
$\alpha,\enspace\beta,\enspace\gamma\in\enspace\mathcal{R}$,
is given by the following vector in $\mathcal{R}^3$:

$$
l=\left[\begin{array}{cc}
\enspace\alpha & -\beta & \gamma\enspace
\end{array}\right]^{T}
$$

The vector above satisfies the following homogeneous expression for straight lines
in projective geometry:

$$
l:\left\lbrace\enspace (\enspace x,\enspace y\enspace)\enspace|\enspace
\left[\begin{array}{cc}
\enspace\alpha & -\beta & \gamma\enspace
\end{array}\right]\times
\left[\begin{array}{c}
\enspace\ x \enspace\\
\enspace\ y \enspace\\
\enspace\ 1 \enspace\\
\end{array}\right]\enspace=\enspace 0
\enspace\right\rbrace
$$

If you want to represent a line $l$ at infinity, you must define a
vector as follows:

$$
l\enspace=\left[\begin{array}{cc}
\enspace 0.0 & 0.0 & \gamma\enspace
\end{array}\right]^{T},
$$

where $\enspace\gamma\enspace\in\enspace\mathcal{R}$

How to work with lines in `pyConics`.

```python
    from pyConics import Line

    l1 = Line( ( 1, -1, 1 ), 'l1' )         # l1: y = x + 1
    l2 = Line( ( 1.5, -1.5, -1.5 ), 'l2' )  # l2: 1.5y = 1.5x - 1.5
    l3 = Line( ( -1, -1, 1 ), 'l3' )        # l3: y = -x + 1
    l4 = Line( ( 2, 2, -2 ), 'l4' )         # l4: 2y = -2x + 2

    print( l1 ) # -> l1: ( x, y ) | [1.0000e+00 -1.0000e+00 1.0000e+00] * [ x y 1 ]' = 0.
    print( l2 ) # -> l2: ( x, y ) | [1.5000e+00 -1.5000e+00 -1.5000e+00] * [ x y 1 ]' = 0.
    print( l3 ) # -> l3: ( x, y ) | [-1.0000e+00 -1.0000e+00 1.0000e+00] * [ x y 1 ]' = 0.
    print( l4 ) # -> l4: ( x, y ) | [2.0000e+00 2.0000e+00 -2.0000e+00] * [ x y 1 ]' = 0.
    print()

    # The relationships between two lines lx and ly can be:
    # 1) coincident lines: lx == ly or lx.are_coincident( ly ).
    #    Notice that l4 = -2 * l3. From the projective geometry both lines are
    #    coincident because they satisfy the same equation. 
    print( f'Is l1 == l1? {l1 == l1}.' )
    print( f'Is l3 == l4? {l3 == l4}.' )
    print( f'Is l1 == l2? {l1 == l2}.\n' )

    # 2) parallel lines: lx // ly or lx.are_parallel( ly ).
    #    Notice that coincident lines are parallel ones, as well.
    print( f'Is l1 // l2? {l1 // l2}.' )
    print( f'Is l2 // l3? {l2 // l3}.' )
    print( f'Is l3 // l4? {l3 // l4}.\n' )

    # 3) concurrent lines: lx.are_concurrent( ly )
    print( f'Are l1 and l2 concurrent lines? {l1.are_concurrent( l2 )}.' )
    print( f'Are l2 and l3 concurrent lines? {l2.are_concurrent( l3 )}.' )
    print( f'Are l3 and l4 concurrent lines? {l3.are_concurrent( l4 )}.\n' )

    # 4) perpendicular lines: lx + ly or lx.are_perpendicular( ly ).
    print( f'Is l1 + l3? {l1 + l3}.' )
    print( f'Is l2 + l4? {l2 + l4}.' )
    print( f'Is l3 + l4? {l3 + l4}.\n' )

    # Euclidean distance between lines.
    # Notice that, from the theory the distance between two concurrent
    # lines is equal to zero. 
    print( f'Distance from l1 to l2 is {l1.distance( l2 ):.4f}.' )
    print( f'Distance from l2 to l3 is {l2.distance( l3 ):.4f}.' )
    print( f'Distance from l3 to l4 is {l3.distance( l4 ):.4f}.\n' )

    # Lines at infinity.
    l5 = Line( ( 0, 0, 2 ), 'l5' )
    l6 = Line( ( 1, -1, 1 ), 'l6' )
    print( l5 )
    print( l6 )
    print( f'Is l5 a line at infinity? {l5.at_infinity()}.' )
    print( f'Is l6 a line at infinity? {l6.at_infinity()}.\n' )

    # Distance from l5 at infinity and l6.
    d56 = l5.distance( l6 )
    print( f'Distance from {l5} to {l6} is {d56}.\n' )
```

### Working with points and lines

Now that I have introduced you to the concepts of points and lines in projective
geometry and how you should work with them. The next step is to know how to use
both geometric shapes together.

However, before we start this step I must answer a question that you may be
wondering. If points and lines have the same vector representation, i.e., they
are both vectors in $\mathcal{R}^3$, how will I know if I am using a point
or a line?

A generic answer would be: The context will tell you whether the vectors in
$\mathcal{R}^3$ are points or lines.
For instance, the cross product operation can be used with the following
operands:

1. two points: The result is a straight line $l$ that passes through both points.
2. two lines: The result is the point of intersection $p$ between both lines.
3. a point $p$ and a line $l$: The result is a line that is perpendicular to
the straight line $l$ and passes through the point $p$.

Finally, the Table below shows six interesting interpretations about vector
representation of points and lines, four of which are not well-posed in
two-dimensional Euclidean Geometry, namely point and line at infinity.

$$
\def\arraystretch{2.5}
\begin{array}{ccc}
\text{vector in }\mathcal{R}^3 & \text{point} & \text{line} \\
\hline\hline
[\begin{array}{ccc}
\alpha & \beta & 0.0
\end{array}]^{T} & \text{point at infinity} & \text{line passing through the origin}\\
\hline
[\begin{array}{ccc}
0.0 & 0.0 & \gamma
\end{array}]^{T} & \text{point at origin when }\gamma=1.0 & \text{line at infinity}\\
\hline
[\begin{array}{ccc}
0.0 & 0.0 & 0.0
\end{array}]^{T} & \text{point at infinity} & \text{line at infinity}\\
\hline
\end{array}
$$

How to work with points and lines in `pyConics`.

```python
from pyConics import Point, Line
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
