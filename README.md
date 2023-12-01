# pyConics

`pyConics` handles points, lines and conics by using algebraic geometry
 and homogeneous coordinates (projective geometry).

------------

## An overview

`pyConics` is a personal project that I have been working on since 2020. Its main goal
is to provide a tool based on algebraic geometry and linear algebra for manipulating
two-dimensional geometric forms such as points, lines, conics and pencil of conics.

It is worth noting that all of the geometric forms in `pyConics` lie in a Projective
space, therefore they are represented by homogeneous coordinates and/or by an homogeneous
system of linear equations.

When the `pyConics` package is finished, it will serve as a basis for the development
of a much larger project that consists of solving the problem of multilateration (MLAT),
also known as hyperbolic positioning. In other words, it is a method of locating an object
by getting the time difference of arrival (TDOA) of a signal emitted from the object to
three or more receivers/stations.

Additionally, in version 0.2.6, this package can be used by high school and undergraduate
students to solve two-dimensional Cartesian geometry problems with points and lines,
such as:

1) find a line that passes through two given points.
2) find the point of intersection of two given lines.
3) given a point and a straight line, find a line that crosses this point and is
perpendicular to the given line.

In version 1.0.0, besides you being able to solve the problems as above, you will also
be able to graph these results, allowing you to illustrate and insert them into
any kind of document.

In version 1.1.0, a class that handles and works with conics sections has been
incorporated into the `pyConics` package. Now, you can:

- create non-degenerate and degenerate ellipses and hyberbolas.
- print them on screen.
- find out whether a point belongs to them or not.
- get their envelope and print it on screen.
- from a point named *pole* with respect to a given conic, find out its *polar*
line and vice versa.
- get the area of an ellipse.

In version 1.2.0, you will be able to:

- check whether two conics are the same or not.
- create a new conic that is a linear combination of two other conics.
- get the points of intersection between a conic and a line.
- create a `CConic` object from a bidimensional `numpy` array. 

------------

## Installation

From a local directory clones this project by using http:

```bash
$ git clone https://github.com/osowsky/pyConics.git
```
or by using ssh:

```bash
$ git clone git@github.com:osowsky/pyConics.git
```

You can install this package, as well:

```bash
$ pip install pyConics
```

<span style="color:green">**NOTE:**<br></span>
*`pyConics` has been tested on Windows 10 and Ubuntu 22.04 OSes. If something is
going wrong with other OS, please reach me out so that I can fix your problem.* 

<span style="color:red">**WARNING:**<br></span>
*If you, like me, enjoy working with Linux OSes without a GUI (Graphical User Interface)
such as Ubuntu OS on WSL2 (Windows Subsystem for Linux) and intend to install the
`pyConics` package on it, then you will need to run the procedure below so that
`pyConics` can work correctly.*

```bash
$ sudo apt-get install x11-xserver-utils
$ sudo apt-get install python3-tk python3-dev
$ xhost +
$ touch ~/.Xauthority
$ pip install pyConics
```

------------

## Usage

`pyConics` can be used to handle points, lines and conics by using algebraic
geometry and homogeneous coordinates.

<span style="color:red">**WARNING:**<br></span>
*To avoid any class name conflicts from other packages, from the version 1.0.0
onwards, the `Point` and `Line` classes had their names changed to `CPoint` and
`CLine`, respectively. For this reason, all of the examples in this file,
`README.md`, had to be rewritten. I apologize for that.*

------------

### Working with points *(v0.2.6 onwards)*

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

------------

- **How to work with points in `pyConics`.**

```python
    from pyConics import CPoint

    p1 = CPoint( ( 0.0, 1.0 ), 'p1' ) # p1 = ( 0.0, 1.0 ).
    p2 = CPoint( ( 1.0, 1.0 ), 'p2' ) # p2 = ( 1.0, 1.0 ).

    print( p1 ) # -> p1: [0.0000e+00 1.0000e+00 1.0000e+00].
    print( p2 ) # -> p2: [1.0000e+00 1.0000e+00 1.0000e+00].
    print()

    print( f'Are p1 and p2 the same? {p1 == p2}\n' ) # -> False.

    d12 = p1.distance( p2 )
    print( f'Distance from {p1}\nto {p2} is {d12:.4f}.\n' ) # -> d12 = 1.0.

    p3 = CPoint( ( 1, 1, 0 ), 'p3' ) # Point at the infinity.
    print( p3 ) # -> p3: [1.0000e+00 1.0000e+00 0.0000e+00] -> point at the infinity.
    print()

    print( f'Is p3 a point at infinity? {p3.at_infinity()}.\n' ) # -> True.

    d13 = p1.distance( p3 )
    print( f'Distance from {p1} to\n{p3} is {d13:.4f}.\n' ) # -> d13 = Inf.
```

------------

### Working with lines *(v0.2.6 onwards)*

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

------------

- **How to work with lines in `pyConics`.**

```python
    from pyConics import CLine

    l1 = CLine( ( 1, -1, 1 ), 'l1' )         # l1: y = x + 1
    l2 = CLine( ( 1.5, -1.5, -1.5 ), 'l2' )  # l2: 1.5y = 1.5x - 1.5
    l3 = CLine( ( -1, -1, 1 ), 'l3' )        # l3: y = -x + 1
    l4 = CLine( ( 2, 2, -2 ), 'l4' )         # l4: 2y = -2x + 2

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
    l5 = CLine( ( 0, 0, 2 ), 'l5' )
    l6 = CLine( ( 1, -1, 1 ), 'l6' )
    print( l5 )
    print( l6 )
    print( f'Is l5 a line at infinity? {l5.at_infinity()}.' )
    print( f'Is l6 a line at infinity? {l6.at_infinity()}.\n' )

    # Distance from l5 at infinity and l6.
    d56 = l5.distance( l6 )
    print( f'Distance from {l5} to {l6} is {d56}.\n' )
```

------------

### Working with points and lines *(v0.2.6 onwards)*

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
% \def\arraystretch{2.5}
\begin{array}{ccc}
\text{vector in }\mathcal{R}^3 & \text{point} & \text{line}\newline
\hline\hline
[\begin{array}{ccc}
\alpha & \beta & 0.0
\end{array}]^{T} & \text{point at infinity} & \text{line passing through the origin}\newline
\hline
[\begin{array}{ccc}
0.0 & 0.0 & \gamma
\end{array}]^{T} & \text{point at origin with }\gamma=1.0 & \text{line at infinity}\newline
\hline
[\begin{array}{ccc}
0.0 & 0.0 & 0.0
\end{array}]^{T} & \text{point at infinity} & \text{line at infinity}\newline
\hline
\end{array}
$$

------------

- **How to work with points and lines in `pyConics`.**

```python
    from pyConics import CPoint, CLine

    # Points.
    p1 = CPoint( ( 1, 3 ), 'p1' )   # p1 = ( 1, 3 )
    p2 = CPoint( ( 0, 4 ), 'p2' )   # p2 = ( 0, 4 )
    p3 = CPoint( ( -2, 0 ), 'p3' )  # p3 = ( -2, 0 )
    p4 = CPoint( ( 2, 0 ), 'p4' )   # p4 = ( 2, 0 )
    p5 = CPoint( ( 0, -4 ), 'p5' )  # p5 = ( 0, -4 )

    # Lines.
    l1 = CLine( ( 2, -1, 4 ), 'l1' )   #l1: y = 2x + 4
    l2 = CLine( ( 2, -1, -4 ), 'l2' )  #l2: y = 2x - 4
    l3 = CLine( ( 2, 1, 0 ), 'l3' )    #l3: y = -2x
    l4 = CLine( ( 1, 0, -2 ), 'l4' )   #l4: x = 2
    l5 = CLine( ( 0, 1, -4 ), 'l5' )   #l5: y = 4
    l6 = CLine( ( 3, -1, 0 ), 'l6' )   #l6: y = 3x

    # Test whether a point is in or is not in a Line.
    print( l1, p1, p2, p3, sep='\n' )
    print( f'Is p1 in l1? {p1 in l1}.' )    # p1 belongs to l1: False
    print( f'Is p2 in l1? {p2 in l1}.' )    # p2 belongs to l1: True
    print( f'Is p3 in l1? {p3 in l1}.\n' )  # p3 belongs to l1: True
    print( l6, p1, p4, sep='\n' )
    print( f'Is p1 in l6? {p1 in l6}.' )    # p1 belongs to l6: True
    print( f'Is p4 in l6? {p4 in l6}.\n' )  # p4 belongs to l6: False
    print( l4, p4, sep='\n' )
    print( f'Is p4 in l4? {p4 in l4}.\n' )  # p4 belongs to l4: True
    print( l5, p2, sep='\n' )
    print( f'Is p2 in l5? {p2 in l5}.\n' )  # p2 belongs to l5: True

    # Use the cross product to handle points and lines.
    # 1) the cross product between two points gives us a line that
    #    passes through these points.
    l: CLine = p2 * p3
    l.name = 'l'
    print( l1, l, sep='\n' )
    print( f'Are l and l1 coincident? {l==l1}.\n' )
    l: CLine = p4 * p5
    l.name = 'l'
    print( l2, l, sep='\n' )
    print( f'Are l and l2 coincident? {l==l2}.\n' )

    # 2) the cross product between two lines gives us their point
    #    of intersection.
    p: CPoint = l1 * l3
    p.name = 'p'
    print( l1, l3, p, sep='\n' )
    print( f'Is p in l1? {p in l1}.' )
    print( f'Is p in l3? {p in l3}.\n' )
    p: CPoint = l2 * l4
    p.name = 'p'
    print( l2, l4, p4, p, sep='\n' )
    print( f'Is p in l2? {p in l2}.' )
    print( f'Is p in l4? {p in l4}.' )
    print( f'Are p and p4 coincident? {p==p4}.\n' )

    # Two parallel lines have their point of intersection at infinity.
    # So, ...
    p: CPoint = l1 * l2
    p.name = 'p'
    print( l1, l2, p, sep='\n' )
    print( f'Is p in l1? {p in l1}.' )
    print( f'Is p in l2? {p in l2}.' )
    print( f'Is p in l4? {p in l4}.' )
    print( f'Is p at infinity? {p.at_infinity()}.\n' )

    # 3) the cross product between a point and a line gives us a
    #    line which is perpendicular to that line and passes
    #    through that point.
    l: CLine = l2 * p2
    l.name = 'l'
    print( p2, l2, l, sep='\n' )
    print( f'Is p2 in l? {p2 in l}.' )
    print( f'Are l2 and l perpendicular? {l2 + l}.\n' )
    p: CPoint = l2 * l
    p.name = 'p'
    print( l2, l, p, sep='\n' )
    print( f'Is p in l? {p in l}.' )
    print( f'Is p in l2? {p in l2}.' )

    # Getting the distance between p2 and l2.
    print( f'Distance from p2 to l2 = {p2.distance( l2 ):.4f}.' )
    print( f'Distance from p2 to p  = {p2.distance( p ):.4f}.\n' )
```

------------

### Creating and setting up the CFigure and CAxes Classes *(v1.0.0 onwards)*

Two classes have been developed for this version, namely `CFigure` and `CAxes`,
so that it is now possible to graph points and lines from the `CPoint` and
`CLine` classes, respectively.
Both are derived from pyPlot classes. Therefore, they are very similar to
those existing in pyPlot. Actually, you can use the `get_pyplot_figure()` and
`get_pyplot_axes()` methods to obtain an instance of pyPlot's `Figure` and
`Axes` Classes, respectively, and work directly with them as if you were
using pyPlot.

In this section, code segments will be used for each sub-section, so if you
want to get the result shown in our image, the current code segment must be
inserted below the previous one.

Let's know how to set up these classes.

------------

- **Creating an empty figure and its four axes.**

```python
    from pyConics import CFigure, CAxes
    import numpy as np

    # Set interactive mode.
    # Activate this mode so that it is not necessary to call the show() method.
    # Whether you comment this line or use CFigure.ioff() method, the show()
    # method must be called.
    CFigure.ion()

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f1: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # Create a 2x2 grid of axes from f1.
    f1.create_axes( ( 2, 2 ) )

    # Get the tuple of CAxes classes for the 2x2 grid.
    axes = f1.axes

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/fig-4axes-empty.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/fig-4axes-empty.jpeg"/>
</p>

------------

- **Changing the x- and y-axis limits and ticks of an axes.**

```python
    # Changing the x- and y-axis limits and the
    # x- and y-ticks of axes[ 0 ].
    axes[ 0 ].xlim = ( 0, 2 )
    axes[ 0 ].ylim = ( -1, 1 )
    xtick = np.linspace( 0, 2, 11 )
    ytick = np.linspace( -1, 1, 11 )
    axes[ 0 ].xticks = xtick
    axes[ 0 ].yticks = ytick

    # Changing the x- and y-axis limits and the
    # x- and y-ticks of axes[ 1 ].
    axes[ 1 ].xlim = ( -1, 1 )
    axes[ 1 ].ylim = ( -1, 1 )
    xtick = np.linspace( -1, 1, 11 )
    ytick = np.linspace( -1, 1, 11 )
    axes[ 1 ].xticks = xtick
    axes[ 1 ].yticks = ytick

    # Changing the x- and y-axis limits and the
    # x- and y-ticks of axes[ 2 ].
    axes[ 2 ].xlim = ( -10, 10 )
    axes[ 2 ].ylim = ( -10, 10 )
    xtick = np.linspace( -10, 10, 11 )
    ytick = np.linspace( -10, 10, 11 )
    axes[ 2 ].xticks = xtick
    axes[ 2 ].yticks = ytick

    # Changing the x- and y-axis limits and the
    # x- and y-ticks of axes[ 3 ].
    # Note that the dimension of the plot box has
    # changed. This is because the aspect ration of
    # the CAxes class has equal scaling ( x/y-scaling = 1.0).
    # This makes circles circular, not elliptical.
    axes[ 3 ].xlim = ( -7, 7 )
    axes[ 3 ].ylim = ( -10, 10 )
    xtick = np.linspace( -7, 7, 5 )
    ytick = np.linspace( -10, 10, 11 )
    axes[ 3 ].xticks = xtick
    axes[ 3 ].yticks = ytick

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/change-lim-and-ticks.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/change-lim-and-ticks.jpeg"/>
</p>

------------

- **Changing title, x-label, and y-label of an axes.**

```python
    # Changing the title of axes[ 0 ].
    axes[ 0 ].title = 'The tittle is hello, world!'

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # Changing the x- and y-label of axes[ 1 ].
    axes[ 1 ].xlabel = 'this is a physical quantity'
    axes[ 1 ].ylabel = 'this is another physical quantity'

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # Using latex language in axes[ 2 ].
    axes[ 2 ].title = f'alpha is written as $\\alpha$'
    axes[ 2 ].xlabel = f'beta is written as $\\beta$'
    axes[ 2 ].ylabel = f'gamma is written as $\\gamma$'

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/add-title-labels.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/add-title-labels.jpeg"/>
</p>

<span style="color:green">**NOTE:**<br></span>
*The `CAxes` class in `pyConics` has setters for its title, xlabel, ylabel, xticks,
and yticks that do not allow you to change their font size directly, i.e., the
`pyConics` fixed the font size of these attributes by default, namely:*

- *title: fontsize = 9.*
- *x- and y-labels: fontsize = 8.*
- *x- and y-ticks: fontsize = 8.*

If, for any reason, you need to change one of these default font sizes, you must get
the `Axes` object that belongs to the `pyPlot` by mean of the `CAxes`'s `get_pyplot_axes()`
method and then call the method that does this task.

An example code to do this is shown below.

```python
    from pyConics import CFigure, CAxes

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f1: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f1.
    # The title font size is 9.
    f1.create_axes( ( 1, 1 ) )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f1.axes

    # Get the pyPlot's axes.
    pp_ax = ax[ 0 ].get_pyplot_axes()

    # Changing the font size of the title in pyPlot's Axes.
    # Now, the title font size is 16.
    pp_ax.set_title( pp_ax.get_title(), fontsize = 16 ) 

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/title-size-changed.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/title-size-changed.jpeg"/>
</p>

------------

### Drawing points (`CPoint`) and lines (`CLine`) on CAxes Class *(v1.0.0 onwards)*

Once you have already learned how to create and set up the `CFigure` and
`CAxes` classes, you are able to learn how to use the `plot()` method in
`CAxes` class for drawing points and lines inside the `CPoint` and
`CLine` classes, respectively.

This `plot()` method has been derived from the `pyPlot`'s `plot()` method.
Therefore, everything you did with `pyPlot`'s `plot()`, you can continue
to do with `plot()` method that belongs to the `CAxes` class. 

In addition, `CAxes.plot()` method can receive either a point such as `CPoint`, a
straight line such as `Cline`, a list of points such as `list[CPoint]` or a
list of straight lines such as `list[CLine]` as argument to be plotted on
screen (into a `CAxes` class).

Now, let's start.

------------

- **Plotting a `CPoint` and a `numpy` point.**

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint
    import numpy as np 

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Creating a point using numpy.
    p1 = np.array( [ 0.5, 0.6 ] )       # p1 =( 0.5, 0.6 ) 

    # Creating a point using CPoint.
    p2 = CPoint( ( 0.5, 0.4 ), 'p2' )   # p2 =( 0.5, 0.4 )

    # Plotting both points
    ax[ 0 ].plot( p1[ 0 ], p1[ 1 ], 'ob', p2, 'om' )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/points.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/points.jpeg"/>
</p>

------------

- **Plotting a list of `CPoint` and a list of `numpy` points.**

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint
    import numpy as np 

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Creating a list of points using numpy.
    p = np.array( [ [ 0.3, 0.1 ],       # p[ 0 ] = ( 0.3, 0.1 )
                    [ 0.3, 0.2 ],       # p[ 1 ] = ( 0.3, 0.2 )
                    [ 0.3, 0.3 ],       # p[ 2 ] = ( 0.3, 0.3 )
                    [ 0.3, 0.4 ],       # p[ 3 ] = ( 0.3, 0.4 )
                    [ 0.3, 0.5 ] ] )    # p[ 4 ] = ( 0.3, 0.5 )

    # Creating a list of points using CPoint.
    p1 = CPoint( ( 0.7, 0.5 ), 'p1' )   # p1 = ( 0.7, 0.5 )
    p2 = CPoint( ( 0.7, 0.6 ), 'p2' )   # p2 = ( 0.7, 0.6 )
    p3 = CPoint( ( 0.7, 0.7 ), 'p3' )   # p3 = ( 0.7, 0.7 )
    p4 = CPoint( ( 0.7, 0.8 ), 'p4' )   # p4 = ( 0.7, 0.8 )
    p5 = CPoint( ( 0.7, 0.9 ), 'p5' )   # p5 = ( 0.7, 0.9 )
    pl = [ p1, p2, p3, p4, p5 ]

    # Plotting both the list of points
    ax[ 0 ].plot( p[ :, 0 ], p[ :, 1 ], 'ob', pl, '^m', markersize = 8 )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/point-list.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/point-list.jpeg"/>
</p>

------------

- **Plotting a `CLine` and a `numpy` line.**

A `CLine` is drawn with a number of points determined by the *clinesamples*
parameter, with its default value being 11.

```python
    from pyConics import CFigure, CAxes
    from pyConics import CLine
    import numpy as np 

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Creating a line using numpy.
    x_i, x_f = ax[ 0 ].xlim
    x = np.linspace( x_i, x_f, 11 )
    y = 1.05 * x                            #  y = 1.05x

    # Creating a line using CLine.
    l1 = CLine( ( 1.05, 1.0, -1.0 ), 'l1' ) # y = -1.05x + 1.0 

    # Plotting both lines ( clinesamples = 11 )
    ax[ 0 ].plot( x, y, 'ob-', l1, 'sm-', linewidth = 0.5, markersize = 6 )

    # Plotting a vertical line with clinesamples = 21
    l2 = CLine( ( 1.0, 0.0, -0.8 ), 'l2' )  # x = 0.8 for all y.
    ax[ 0 ].plot( l2, '^y-', clinesamples = 21, linewidth = 0.5, markersize = 6 )

    # Show Figure on screen.
    CFigure.show()
```
<p align="center">
    <!-- <img src="./docs/figs/howto-plot/lines.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/lines.jpeg"/>
</p>

------------

- **Plotting a list of `CLine`.**

```python
    from pyConics import CFigure, CAxes
    from pyConics import CLine
    import numpy as np 

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Create some lines and add them to a list.
    l1 = CLine(( 0.0, 1.0, -0.1 ), 'l1' )   # y = 0.1 for all x
    l2 = CLine(( 0.0, 1.0, -0.9 ), 'l2' )   # y = 0.9 for all x
    l3 = CLine(( 1.0, 0.0, -0.1 ), 'l3' )   # x = 0.1 for all y
    l4 = CLine(( 1.0, 0.0, -0.9 ), 'l4' )   # x = 0.9 for all y
    l = [ l1, l2, l3, l4 ]
    ax[ 0 ].plot( l, 'ob-', clinesamples = 11, linewidth = 0.5, markersize = 4 )

    # Create some others lines and add them to a list.
    l5 = CLine(( 1.0, 1.0, -1.0 ), 'l5' )   # y = -x + 1
    l6 = CLine(( 1.0, -1.0, 0.0 ), 'l6' )   # y = x
    l = [ l5, l6 ]
    ax[ 0 ].plot( l, 'or:', clinesamples = 21, linewidth = 1.0, markersize = 6 )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/line-list.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/line-list.jpeg"/>
</p>

------------

- **Plotting line segments through a sequence of points.**

When you are using the `plot()` method to graph a line, the result on screen
is a straight line that crosses the entire range of the $x$-axis and $y$-axis.  

However, if you only want to get a few points from this line (line segment),
you might want to use the `sequence()` method of the `CLine` class.

For instance, given a `CLine` $l$ and a sequence $x = [ x_1, x_2, \cdots, x_{n-1}, x_n ]$,
the `sequence()` method retuns a list of `CPoint` $p_s$ such that,

$$
p_s = \lbrack
\begin{array}{ccccc}
\text{CPoint}( ( y_1, x_1 ), & \text{CPoint}( ( y_2, x_2 ) ), & \cdots, &
\text{CPoint}( ( y_{n-1}, x_{n-1} ), & \text{CPoint}( ( y_{n}, x_{n} ) )
\end{array}
\rbrack
$$

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    import numpy as np 

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Create some lines.
    l1 = CLine(( 0.0, 1.0, -0.1 ), 'l1' )   # y = 0.1 for all x
    l2 = CLine(( 1.0, 0.0, -0.1 ), 'l2' )   # x = 0.1 for all y
    l3 = CLine(( 1.0, -1.0, 0.0 ), 'l3' )   # y = x

    # Plot that lines.
    ax[ 0 ].plot( l1, 'b-', linewidth = 1.5 )
    ax[ 0 ].plot( l2, 'b-', linewidth = 1.5 )
    ax[ 0 ].plot( l3, 'b-', linewidth = 1.5 )

    # Create a range from 0.3 to 0.8 with step = 0.5.
    x = np.linspace( 0.3, 0.8, 11 )

    # Get a sequence of points form these lines.
    ps1 = list( l1.sequence( list( x ) ) )
    ps2 = list( l2.sequence( list( x ) ) )
    ps3 = list( l3.sequence( list( x ) ) )

    # Plot these line segments as a sequence of points.
    ax[ 0 ].plot( ps1, 'ro', markersize = 6 )
    ax[ 0 ].plot( ps2, 'ro', markersize = 6 )
    ax[ 0 ].plot( ps3, 'ro', markersize = 6 )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/line-segment.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/line-segment.jpeg"/>
</p>

<span style="color:green">**NOTE:**<br></span>
*It is worth mentioning that, when you have a line $l$ that is parallel to the
$y$-axis, the input sequence $x$ will be assigned to a variable $y$ that will
sweep the $y$-axis instead of the $x$-axis. For a better understanding, pay
attention to the variable `l2` in the code segment as above.*

------------

- **Solving a simple problem of geometry with points and lines.**

Finally, this is the last subsection about how to draw points (`CPoint`) and
lines (`CLine`) on `CAxes` class. Here, you are going to learn how to solve
a simple problem of geometry using `pyConics`. Are you ready? Let's do it.

------------

*Problem formulation:*

Given two points $p_1=( -0.4, 0.6 )$ and $p_2=( 0.0, -0.8 )$ and a line
$l_1 = ( 0.9, -1.0, 0.1 )$ as shown in the figure below, solve the following
geometry problems:

1. Get a line $l_2$ that passes through these points.
2. Get a point $p_3$ that is the point of intersection between the lines
$l_1$ and $l_2$.
3. Get a line $l_3$ that passes through the point $p_1$ and is perpendicular
to the line $l_1$. 

Graph $l_2$, $p_3$, and $l_3$ on the same canvas and also evaluate the results
with the `in` operator and the `are_perpendicular()` method.

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/geometry-problem-q.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/geometry-problem-q.jpeg"/>
</p>

------------

*Problem resolution:*

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    import numpy as np 

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Define a title.
    ax[ 0 ].title = 'A Simple Problem of Geometry with Points and Lines'

    # Change its axis.
    ax[ 0 ].xlim = ( -1, 1 )
    ax[ 0 ].xticks = np.linspace( -1, 1, 11 )
    ax[ 0 ].ylim = ( -1, 1 )
    ax[ 0 ].yticks = np.linspace( -1, 1, 11 )

    # Create and plot the geometric forms of the problem.
    p1 = CPoint( ( -0.4, 0.6 ), 'p_1' )
    p2 = CPoint( ( 0.0, -0.8 ), 'p_2' )
    l1 = CLine( ( 0.9, -1.0, 0.1 ), 'l_1' ) # y = 0.9x + 0.1
    ax[ 0 ].plot( p1, 'or', p2, 'or', l1, 'b-', clinesamples = 21 )
    ax[ 0 ].text( p1.x, p1.y, f'${p1.name}$', ha = 'left', va = 'bottom' )
    ax[ 0 ].text( p2.x, p2.y, f'${p2.name}$', ha = 'left', va = 'bottom' )
    ls = l1.sequence( [ 0.6 ] )[ 0 ]
    ax[ 0 ].text( ls.x, ls.y, f'${l1.name}$', ha = 'right', va = 'bottom' )

    # Solving the problem (1):
    l2: CLine = p1 * p2
    l2.name = 'l_2'
    print( l2 )
    ax[ 0 ].plot( l2, 'y-', clinesamples = 21 )
    ls = l2.sequence( [ -0.1 ] )[ 0 ]
    ax[ 0 ].text( ls.x, ls.y, f'${l2.name}$', ha = 'left', va = 'bottom' )
    print( 'Evaluating the result for the problem (1):' )
    print( f'Does p1 lie in l2? {p1 in l2}' ) # True
    print( f'Does p2 lie in l2? {p2 in l2}' ) # True
    print()

    # Solving the problem (2):
    p3: CPoint = l1 * l2
    p3.name = 'p_3'
    print( p3 )
    ax[ 0 ].plot( p3, 'om' )
    ax[ 0 ].text( p3.x, p3.y, f'${p3.name}$', ha = 'right', va = 'bottom' )
    print( 'Evaluating the result for the problem (2):' )
    print( f'Does p3 lie in l1? {p3 in l1}' ) # True
    print( f'Does p3 lie in l2? {p3 in l2}' ) # True
    print()

    # Solving the problem (3):
    l3: CLine = p1 * l1
    l3.name = 'l_3'
    print( l3 )
    ax[ 0 ].plot( l3, 'g-' )
    ls = l3.sequence( [ 0.4 ] )[ 0 ]
    ax[ 0 ].text( ls.x, ls.y, f'${l3.name}$', ha = 'left', va = 'bottom' )
    print( 'Evaluating the result for the problem (3):' )
    print( f'Does p1 lie in l3? {p1 in l3}' )           # True
    print( f'Are l1 and l3 perpendicular? {l1 + l3}' )  # True
    print()

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot/geometry-problem-a.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot/geometry-problem-a.jpeg"/>
</p>

------------

### Working with conics *(v1.1.0 onwards)*

Finally, in this version, the main goal of `pyConics` has been achieved, in which you
will be able to plot conics on the screen and perform simple operations with them.

However, before introducing its use through code segments, the basic theory about conics
in a two-dimensional space will be explained next.

A quadric surface in a two-dimensional space over the real field, also known as conic
sections (ellipses, parabolas, and hyperboles), is defined by the following algebraic equation:

$$
\begin{array}{cccccccccccc}
A \cdot x^{2} & + & B \cdot y^{2} & + & C \cdot x \cdot y & D \cdot x & + & E \cdot y & + & F & = & 0
\end{array}
$$

where $A,\enspace B,\enspace C,\enspace D,\enspace E,\enspace F\enspace\in\enspace\mathcal{R}$

The representation in homogeneous coordinates of the above polynomial equation can be rewritten
in its matricial quadratic form, as follows:

$$
C:\left\lbrace\enspace (\enspace x,\enspace y\enspace)\enspace|\enspace
\left[\begin{array}{ccc}
\enspace\ x \enspace\\
\enspace\ y \enspace\\
\enspace\ 1 \enspace\\
\end{array}\right]^{T}\times\enspace
\left[\begin{array}{ccc}
\enspace A & C / 2 & D / 2 \enspace \\
\enspace C / 2 & B & E / 2 \enspace \\
\enspace D / 2 & E / 2 & F\enspace \\
\end{array}\right]\times
\left[\begin{array}{c}
\enspace\ x \enspace\\
\enspace\ y \enspace\\
\enspace\ 1 \enspace\\
\end{array}\right]\enspace=\enspace 0
\enspace\right\rbrace
$$

The latter equation will be used to represent ellipses and hyperboles in `pyConics`'s
`CConic` class, which can be either non-degenerate or
[degenerate](https://en.wikipedia.org/wiki/Degenerate_conic).

<span style="color:green">**NOTE:**<br></span>
*A conic is said to be non-degenerate if it is represented by a non-singular matrix,
whereas a degenerate conic is represented by a singular matrix. Over the real field,
there are only three types of degenerate conics, namely:*

- *two concurrent lines, where the rank of its matrix is equal to two.*
- *two parallel lines that are distinct, where the rank of its matrix is equal to two.*
- *two parallel lines that are coincident, where the rank of its matrix is equal to one.*

------------

- **Plotting non-degenerate ellipses with `CConic`.**

Some non-degenerate ellipses will be drawn on the screen. You can see from the code
below that this task is really simple when `pyConics` is used.
​
```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    from pyConics import CConic
    from pyConics import cconst

    import numpy as np

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Define a title.
    ax[ 0 ].title = 'Plotting non-degenerate ellipses.'

    # Change its axis.
    ax[ 0 ].xlim = ( -10, 10 )
    ax[ 0 ].xticks = np.linspace( -10, 10, 21 )
    ax[ 0 ].ylim = ( -10, 10 )
    ax[ 0 ].yticks = np.linspace( -10, 10, 21 )

    # Create and plot a circle with radius = 1, and center at ( 0, 0 )
    C0 = CConic( name = 'C0' )
    xy = CPoint( ( 0.0, 0.0 ) )
    print( C0 )
    print( f'The rank of {C0.name} is {C0.rank}.\n' )
    
    ax[ 0 ].plot( xy, 'ob', C0, '-b',
                  cconicsamples = ( 101, 101 ), markersize = 3 )

    # Create and plot a circle with radius = 3.5, and center at( 5.5, 4.5 )
    xy = CPoint( ( 5.5, 4.5 ) )
    C1 = CConic( 3.5, center = xy, name = 'C1' )
    print( C1 )
    print(f'The rank of {C1.name} is {C1.rank}.\n')
    ax[ 0 ].plot( xy, 'or', C1, '-r',
                  cconicsamples = ( 101, 101 ), markersize = 3 )

    # Create and plot an ellipse with vertex = 4, focal distance = 3.5,
    # center at( 0.0, 0.0 ), and angle = +30 degrees ( counterclockwise ).
    xy = CPoint( ( 0.0, 0.0 ) )
    C2 = CConic( 4.0, 3.5, 30 / 180 * cconst.pi, center = xy, name = 'C2' )
    print( C2 )
    print( f'The rank of {C2.name} is {C2.rank}.\n' )
    ax[ 0 ].plot( C2, '-g', cconicsamples = ( 101, 101 ) )

    # Create and plot an ellipse with vertex = 5,
    # foci = [ ( -8, -2 ), ( -2, -8 ) ], and angle = -45 degrees ( clockwise ) .
    f1 = CPoint( ( -8.0, -2.0 ) )
    f2 = CPoint( ( -2.0, -8.0 ) )
    C3 = CConic( 5.0, foci = ( f1, f2 ), name = 'C3' )
    print( C3 )
    print( f'The rank of {C3.name} is {C3.rank}.\n' )
    ax[ 0 ].plot( [ f1, f2 ], 'oy', C3, '-y', cconicsamples = ( 101, 101 ), markersize = 3 )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot-conics/conic-ellipse.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot-conics/conic-ellipse.jpeg"/>
</p>

------------

- **Plotting non-degenerate hyperbolas with `CConic`.**

Just as it was easy to build ellipses using `pyConics`. Building hyperbolas will be as well. Pay attention to the code below to see how this is done.

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    from pyConics import CConic
    from pyConics import cconst

    import numpy as np

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Define a title.
    ax[ 0 ].title = 'Plotting non-degenerate hyperboles.'

    # Change its axis.
    ax[ 0 ].xlim = ( -10, 10 )
    ax[ 0 ].xticks = np.linspace( -10, 10, 21 )
    ax[ 0 ].ylim = ( -10, 10 )
    ax[ 0 ].yticks = np.linspace( -10, 10, 21 )

    # Create and plot a hyperbole with vertex = 1.0, focal distance = 1.5,
    # and center at ( 0, 0 )
    xy = CPoint( ( 0.0, 0.0 ) )
    C0 = CConic( 1, 1.5, center = xy, name = 'C0' )
    print( C0 )
    print( f'The rank of {C0.name} is {C0.rank}.\n' )
    ax[ 0 ].plot( xy, 'ob', C0, '-b', cconicsamples = ( 101, 101 ), markersize = 3 )

    # Create and plot a hyperbole with vertex = 1.0, focal distance = 2.5,
    # and center at ( 6.5, 4.5 )
    xy = CPoint( ( 6.5, 4.5 ) )
    C1 = CConic( 1.0, 2.5, center = xy, name = 'C1' )
    print( C1 )
    print( f'The rank of {C1.name} is {C1.rank}.\n' )
    ax[ 0 ].plot( xy, 'or', C1, '-r', cconicsamples = ( 101, 101 ), markersize = 3 )

    # Create and plot a hyperbole with vertex = 1.5, focal distance = 1.7
    # center at ( -7.0, 3.0 ), and angle = +30 degrees ( counterclockwise ).
    xy = CPoint( ( -7.0, 3.0 ) )
    C2 = CConic( 1.5, 1.7, 30 / 180 * cconst.pi, center = xy, name = 'C2' )
    print( C2 )
    print( f'The rank of {C2.name} is {C2.rank}.\n' )
    ax[ 0 ].plot( xy, 'og', C2, '-g', cconicsamples = ( 101, 101 ), markersize = 3 )

    # Create and plot a hyperbole with vertex = 1.5,
    # foci = [ ( -7, -3 ), ( -3, -7 ) ], and angle = -45 degrees ( clockwise ).
    f1 = CPoint( ( -7.0, -3.0 ) )
    f2 = CPoint( ( -3.0, -7.0 ) )
    C3 = CConic( 1.5, foci = ( f1, f2 ), name = 'C3' )
    print( C3 )
    print( f'The rank of {C3.name} is {C3.rank}.\n' )
    ax[ 0 ].plot( [ f1, f2 ], 'oy', C3, '-y', cconicsamples = ( 101, 101 ), markersize = 3 )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot-conics/conic-hyperbole.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot-conics/conic-hyperbole.jpeg"/>
</p>

------------

- **Plotting degenerate conics with `CConic`.**

Recalling, over the real field, there are only three types of degenerate conics:

- two concurrent lines, where the rank of its matrix is equal to two.
- two parallel lines that are distinct, where the rank of its matrix is equal to two.
- two parallel lines that are coincident, where the rank of its matrix is equal to one.

In the code below, these three types are going to be drawn.

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    from pyConics import CConic
    from pyConics import cconst

    import numpy as np

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Define a title.
    ax[ 0 ].title = 'Plotting degenerate conics.'

    # Change its axis.
    ax[ 0 ].xlim = ( -10, 10 )
    ax[ 0 ].xticks = np.linspace( -10, 10, 21 )
    ax[ 0 ].ylim = ( -10, 10 )
    ax[ 0 ].yticks = np.linspace( -10, 10, 21 )

    # Create and plot two distinct, parallel lines.
    l1 = CLine( ( 1, 0, -1 ) )  # x = 1 for all y.
    l2 = CLine( ( 1, 0, -4 ) )  # x = 4 for all y.
    C0 = CConic( degenerate = ( l1, l2 ), name = 'C0' )
    print( C0 )
    print( f'The rank of {C0.name} is {C0.rank}.\n' )
    ax[ 0 ].plot( C0, '-b', cconicsamples = ( 11, 11 ) )

    # Create and plot two concurrent lines.
    p1 = CPoint( ( -5, -2 ) )
    p2 = CPoint( ( -7, 3 ) )
    p3 = CPoint( ( 0, 2 ) )
    l1: CLine = p1 * p2
    l2: CLine = p1 * p3
    C1 = CConic( degenerate = ( l1, l2 ), name = 'C1' )
    print( C1 )
    print( f'The rank of {C1.name} is {C1.rank}.\n' )
    ax[ 0 ].plot( [ p1, p2, p3 ], 'or', C1, '-r',
                  cconicsamples = ( 11, 11 ), markersize = 3 )

    # Create and plot two coincident, parallel lines.
    p1 = CPoint( ( -8, -9 ) )
    p2 = CPoint( ( 6, 4 ) )
    l1: CLine = p1 * p2
    C2 = CConic( degenerate = ( l1, l1 ), name = 'C2' )
    print( C2 )
    print( f'The rank of {C2.name} is {C2.rank}.\n' )
    ax[ 0 ].plot( [ p1, p2 ], 'og', C2, '-g',
                 cconicsamples = ( 11, 11 ), markersize = 3 )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot-conics/conic-degenerate.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot-conics/conic-degenerate.jpeg"/>
</p>

------------

- **Working with points, lines, and conics.**

In this section, you are going to learn how to work with points, lines, and conics
at the same time.

After plotting a circle on the screen, a region painted blue will be used along
with the `sequence()` method in `CConic` class to get all points on that region and
that lie in the circle.

Next, those points in the blue region will be tested to check if they really
belong to the conic named `C0`. This test is going to be performed by the `in`
operator (`__contains__` dunder) of the `CConic` class.

<span style="color:red">**WARNING:**<br></span>
*The `CConic.sequence()` method calls the `pyPlot.contour()` method to return
a sequence of `CPoint` points which lie in `C0`. The latter method uses an
approximation algorithm to join points of a function of two variables which are
on the same level curve. Therefore, the condition for a point to belong to a
conic depends on the resolution (step) used in the `numpy`'s `linspace()` method
which creates the range on the x- and y-axis that are passed as arguments to
the `sequence()` and `contour()` functions.*

*The larger the step, the better the result. Try increasing the step from 19 to 51
and see the new results obtained in the console.*

Finally, using the multiplication operator (`__mul__` dunder) you will be able
to perform operations between a conic and a point (`CConic * CPoint`) and between
a conic and a straight line (`CConic * CLine`), namely:

1. Given a conic $C$ and a point $p \in C$, the $C * p$ operation,
`CConic * CPoint`, will return a line $l$, `CLine`, where $l$ will be
tangent to the given conic $C$ at the given point $p$.

2. Given a non-degenerate conic $C$ and a line $l$, where $l$ is tangent to $C$
at a point $p$ to be determinated, the $C * l$ operation, `CConic * CLine`, will
return the unknown point $p$, `CPoint`, that belongs to the conic $C$ and to the
line $l$.

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    from pyConics import CConic
    from pyConics import cconst

    import numpy as np

    import matplotlib.patches as patches
    from matplotlib.path import Path

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Define a title.
    ax[ 0 ].title = 'Working with points, lines, and conics all together.'

    # Change its axis.
    ax[ 0 ].xlim = ( -10, 10 )
    x = np.linspace( -10, 10, 21 )
    ax[ 0 ].xticks = x
    ax[ 0 ].ylim = ( -10, 10 )
    y = np.linspace( -10, 10, 21 )
    ax[ 0 ].yticks = y

    # Create a circle with radius = 5, and center at ( 0, 0 ).
    radius = 7.0
    C0 = CConic( radius, name = 'C0' )
    ax[ 0 ].plot( C0, 'b-' )

    # Create a region where the sequence() method will be used.
    x = np.linspace( -4.0, 6.0, 19 )
    y = np.linspace( -6.5, 6.5, 19 )
    verts = [
                ( x[ 0 ], y[ 0 ] ),   # left, bottom
                ( x[ 0 ], y[ -1 ] ),  # left, top
                ( x[ -1 ], y[ -1 ] ), # right, top
                ( x[ -1 ], y[ 0 ] ),  # right, bottom
                ( x[ 0 ], y[ 0 ] ),   # ignored
            ]
    codes = [
                Path.MOVETO,
                Path.LINETO,
                Path.LINETO,
                Path.LINETO,
                Path.CLOSEPOLY,
            ]
    rect = Path( verts, codes )
    patch = patches.PathPatch( rect, linewidth = 0.0 )
    ax[ 0 ].get_pyplot_axes().add_patch( patch )

    # Get the points belonging to C0 and that are within the blue region.
    lst = C0.sequence( list( x ), list( y ) )
    for lp in lst:
        ax[ 0 ].plot( list( lp ), 'or', markersize = 4 )

    # Test those points to check if they really belong to C0.
    # Warning: The condition so that a points belongs to a conic depends on
    # the resolution (step) used in linspace() method applied to the sequence()
    # method.
    # The larger the step, the better the result.
    # Try changing the step from 19 to 51 steps and see the new results.
    for lp in lst:
        for p in lp:
            print( f'Does p=({p.x:.4f}, {p.y:.4f}) lie in {C0.name}? {p in C0}' )
    print()

    # Create a point that belongs to C0. So, get the line that is tangent to C0
    # at that point.
    p1 = CPoint( ( -radius, 0 ), name = 'p1' )
    l1: CLine = C0 * p1
    l1.name = 'l1'
    ax[ 0 ].plot( p1, 'og', l1, '-g', linewidth = 1.5, markersize = 5 )
    print( f'Does {p1.name}=({p1.x:.4f}, {p1.y:.4f}) lie in {l1}? {p1 in l1}' )
    print( f'Does {p1.name}=({p1.x:.4f}, {p1.y:.4f}) lie in {C0.name}? {p1 in C0}' )
    print()
    
    # Create another point that belongs to C0. So, get the line that is tangent
    # to C0 at that other point.
    l2 = CLine( ( 1, 1, radius * np.sqrt( 2 ) ),
                name = 'l2' )  # y = -x - ( 7 * sqrt( 2 ) )
    p2: CPoint = C0 * l2
    p2.name = 'p2'
    ax[ 0 ].plot( p2, 'oy', l2, '-y', linewidth = 1.5, markersize = 5 )
    print( f'Does {p2.name}=({p2.x:.4f}, {p2.y:.4f}) lie in {l2}? {p2 in l2}' )
    print( f'Does {p2.name}=({p2.x:.4f}, {p2.y:.4f}) lie in {C0.name}? {p2 in C0}' )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot-conics/points-lines-conics.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot-conics/points-lines-conics.jpeg"/>
</p>

------------

- **Creating an envelope of non-degenerate conic.**

By definition, the envelope of a curve $C$ is given by a sequence of curves $l$ that
touch each point $p$ in $C$.

Here, the envelope of an ellipse is going to be plotted on screen. First, an
ellipse will be created. Then, the `CConic.sequence()` method is called to return
a set of points, where these points belong to that ellipse. Next, the multiplication
operator will be used between the ellipse and the points to return a set of lines,
where each of those lines is going to be tangent to the conic. Finally, by using
the `CAxes.plot()` method, all lines will be plotted on screen, thus drawing the
envelope of the ellipse. 

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    from pyConics import CConic
    from pyConics import cconst

    import numpy as np

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Define a title.
    ax[ 0 ].title = 'Creating an envelope of an ellipse.'

    # Change its axis.
    ax[ 0 ].xlim = ( -10, 10 )
    ax[ 0 ].xticks = np.linspace( -10, 10, 21 )
    ax[ 0 ].ylim = ( -10, 10 )
    ax[ 0 ].yticks = np.linspace( -10, 10, 21 )

    # Create and plot an ellipse with vertex = 5, focal distance = 3.5,
    # center at( 0.0, 0.0 ), and angle = +30 degrees ( counterclockwise ).
    xy = CPoint( ( 0.0, 0.0 ) )
    C = CConic( 5.0, 3.5, 30 / 180 * cconst.pi, center = xy, name = 'C' )
    print( C )
    print( f'The rank of {C.name} is {C.rank}.\n' )
    ax[ 0 ].plot( C, '-b', cconicsamples = ( 101, 101 ), linewidth = 0.5 )

    # Create a region where the sequence() method will be used.
    x = np.linspace( -10.0, 10.0, 37 )
    y = np.linspace( -10.0, 10.0, 37 )

    # Get the points belonging to C.
    lst = C.sequence( list( x ), list( y ) )
    for lp in lst:
        # For each list of points create a list of tangent lines.
        ll = []
        for p in lp:
            l: CLine = C * p # l is a line tangent to C at the point p in C.
            ll.append( l )

        # Create the envelope of C.
        ax[ 0 ].plot( list( ll ), '-r', clinesamples = 7, linewidth = 1.0 )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/howto-plot-conics/ellipse-envelope.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/howto-plot-conics/ellipse-envelope.jpeg"/>
</p>

------------

- **Poles and polars of non-degenerate conic sections.**

By definition, a *pole* and *polar* are respectively a point and a line that have
a unique reciprocal relationship with respect to a given conic section.
For further reading, visit these external links:

- [Pole and polar - Wikipedia](https://en.wikipedia.org/wiki/Pole_and_polar)
- [Polar -- from Wolfram MathWorld](https://mathworld.wolfram.com/Polar.html)

This reciprocal relationship is valid only for non-degenerate conics. For
degenerate conics it is possible to obtain their "reciprocal" straight line from
a point, but the inverse is not possible since degenerate conics are represented
by singular matrices.

In fact, the terms *pole* and *polar* with respect to a given conic could not
even be used when referring to degenerate conics.

In this section, only the concept of *pole* and *polar* for non-degenerate conics
will be presented through the multiplication operator between conics and points
and conics and lines.

In the next section, the results of using the multiplication operator between
conics and points for degenerate conics will be presented. As stated before, this
operator cannot be used in multiplication between conics and lines, given that
such conics are degenerate.

It is worth noting that this reciprocity relationship has a very interesting
property that will be used in the implementation of a method in the `CConic` class
(not in this version, namely 1.1.0). This new method will allow getting the points
of intersection between a given non-degenerate conic and a line.

Now you are ready, let's start learning these new concepts about conics.

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    from pyConics import CConic
    from pyConics import cconst

    import numpy as np

    # Set interactive mode.
    # Activate this mode so that it is not necessary to call the show() method.
    # Whether you comment this line or use CFigure.ioff() method, the show()
    # method must be called.
    CFigure.ion()

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.25
    f: CFigure = CFigure( (width, 3.5 * width ) )

    # Create a 2x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 2, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Define titles.
    ax[ 0 ].title = 'Poles and polars of an ellipse.'
    ax[ 1 ].title = 'Poles and polars of a hyperbole.'

    # Change their axis.
    ax[ 0 ].xlim = ( -10, 10 )
    ax[ 1 ].xlim = ( -10, 10 )
    ax[ 0 ].xticks = np.linspace( -10, 10, 21 )
    ax[ 1 ].xticks = np.linspace( -10, 10, 21 )
    ax[ 0 ].ylim = ( -10, 10 )
    ax[ 1 ].ylim = ( -10, 10 )
    ax[ 0 ].yticks = np.linspace( -10, 10, 21 )
    ax[ 1 ].yticks = np.linspace( -10, 10, 21 )

    # Create and plot an ellipse with vertex = ve, focal distance = 5,
    # center at cCe, and angle = +45 degrees ( counterclockwise ).
    ve = 6
    cCe = -5.0
    xy = CPoint( ( cCe, cCe ) )
    Ce = CConic( ve, 5.0, 45 / 180 * cconst.pi, center = xy, name = 'Ce' )
    print( Ce )
    print( f'The rank of {Ce.name} is {Ce.rank}.\n' )
    ax[ 0 ].plot( Ce, '-b', cconicsamples = ( 101, 101 ), linewidth = 1.0 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # Creating and plotting a sequence of pairs of pole-polar for the ellipse.
    polar = CLine( ( 1, 1, 10 ), 'polar' )
    pole: CPoint = Ce * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'ob', polar, '--b', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    pole = CPoint( ( -3.5, -3.5, 1 ), 'pole' )
    polar: CLine = Ce * pole
    polar.name = 'polar'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'or', polar, '--r', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    polar = CLine( ( 1, 1, 6 ), 'polar' )
    pole: CPoint = Ce * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'oy', polar, '--y', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    pole = CPoint( ( -2.0, -2.0, 1 ), 'pole' )
    polar: CLine = Ce * pole
    polar.name = 'polar'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'og', polar, '--g', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    polar = CLine( ( 1, 1, 2 ), 'polar' )
    pole: CPoint = Ce * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'om', polar, '--m', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    coord = cCe + np.sqrt( ( ve ** 2 ) / 2 )
    pole = CPoint( ( coord, coord, 1 ), 'pole' )
    polar: CLine = Ce * pole
    polar.name = 'polar'
    print( f'Does the {pole.name} lie in {Ce.name}? {pole in Ce}' )
    print( f'Does the {pole.name} lie in {polar.name}? {pole in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'ok', polar, '--k', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    polar = CLine( ( 0, 0, 1 ), 'polar' )
    pole: CPoint = Ce * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'oc', polar, '--c', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # Create and plot a hyperbole with vertex = vh, focal distance = 5,
    # center at cCh, and angle = -45 degrees ( clockwise ).
    vh = 4.0
    cCh = 4.0
    xy = CPoint( ( -cCh, cCh ) )
    Ch = CConic( vh, 5.0, -45 / 180 * cconst.pi, center = xy, name = 'Ch' )
    print( Ch )
    print(f'The rank of {Ch.name} is {Ch.rank}.\n')
    ax[1].plot( Ch, '-b', cconicsamples = ( 101, 101 ), linewidth=1.0 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # Creating and plotting a sequence of pairs of pole-polar for the ellipse.
    polar = CLine( ( 1, -1, 8 ), 'polar' )
    pole: CPoint = Ch * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'ob', polar, '--b', linewidth = 1.0, markersize = 3)

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    pole = CPoint( ( -3.0, 3.0, 1 ), 'pole' )
    polar: CLine = Ch * pole
    polar.name = 'polar'
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'or', polar, '--r', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    polar = CLine( ( 1, -1, 5 ), 'polar' )
    pole: CPoint = Ch * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'oy', polar, '--y', linewidth = 1.0, markersize = 3)

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    pole = CPoint( ( -2.0, 2.0, 1 ), 'pole' )
    polar: CLine = Ch * pole
    polar.name = 'polar'
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'og', polar, '--g', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    polar = CLine( ( 1, -1, 3 ), 'polar' )
    pole: CPoint = Ch * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'om', polar, '--m', linewidth = 1.0, markersize = 3)

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    coord = -cCh + np.sqrt( ( vh ** 2 ) / 2 )
    pole = CPoint( ( coord, -coord, 1 ), 'pole' )
    polar: CLine = Ch * pole
    polar.name = 'polar'
    print( f'Does the {pole.name} lie in {Ch.name}? {pole in Ch}' )
    print( f'Does the {pole.name} lie in {polar.name}? {pole in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'ok', polar, '--k', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    polar = CLine( ( 0, 0, 1 ), 'polar' )
    pole: CPoint = Ch * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'oc', polar, '--c', linewidth = 1.0, markersize = 3 )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/poles-and-polar/poles-polars-non-degenerate.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/poles-and-polar/poles-polars-non-degenerate.jpeg"/>
</p>

------------

- **"Poles" and "polars" of degenerate conics.**

As said earlier, in this section you are going to see how to get the "*polar*" line
$l$ from its "*pole*" $p$ with respect to a given degenerate conic $C$. Notice that,
the inverse operation is not allowed, because the conic $C$ is represented by a
singular matrix.

Over the real field, there are three types of degenerate conics. Each of them behaves
differently with regard to their "*polar*" lines and "*poles*", namely:

1. Two distinct, and parallel lines $f$ and $g$,
such that $f \neq g$, and $f \parallel g$.
    - "*poles*" in the range between $f$ and $g$ will return "*polar*" lines $h$
     outside this range, such that $h \parallel f$, and $h \parallel g$.
    - "*poles*" outside the range between $f$ and $g$ will return "*polar*" lines $h$
     in the range between $f$ and $g$, such that $h \parallel f$, and $h \parallel g$.
    - "*poles*" in $f$ or $g$ will return "*polar*" lines $h$, such that
    $h = f$ or $h = g$, respectively.
    - "*poles*" in the middle of the range between $f$ and $g$ will return "*polar*"
    lines at infinity.
    - "*poles*" at infinity will return "*polar*" lines $h$ in the middle of the range
     between $f$ and $g$.
2. Two concurrent lines $f$ and $g$,
such that $f \neq g$, and $f \nparallel g$.
    - "*poles*" in $f$ or $g$ will return "*polar*" lines $h$, such that
    $h = f$ or $h = g$, respectively.
    - the "*pole*" in $f$ and $g$, point of intersection, will return a "*polar*"
     line $h$, such that $h$ is at infinity.
    - "*poles*" outside $f$ and $g$ will return "*polar*" lines $h$, such that
    $h$ will pass through the point of intersection.

3. Two coincident lines $f$ and $g$, such that $f = g$.
    - "*poles*" in $f = g$ will return "*polar*" lines $h$, such that
    $h$ is at infinity.
    - "*poles*" outside $f = g$ will return "*polar*" lines $h$, such that
    $h = f = g$. 

See the example below for a better understanding.

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    from pyConics import CConic
    from pyConics import cconst

    import numpy as np

    # Set interactive mode.
    # Activate this mode so that it is not necessary to call the show() method.
    # Whether you comment this line or use CFigure.ioff() method, the show()
    # method must be called.
    CFigure.ion()

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.25
    f: CFigure = CFigure( (width, 3.5 * width ) )

    # Create a 2x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 2, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Define titles.
    ax[ 0 ].title = '"Poles" and "polars" of two distinct, and parallel lines.'
    ax[ 1 ].title = '"Poles" and "polars" of two concurrent lines.'

    # Change their axis.
    ax[ 0 ].xlim = ( -10, 10 )
    ax[ 1 ].xlim = ( -10, 10 )
    ax[ 0 ].xticks = np.linspace( -10, 10, 21 )
    ax[ 1 ].xticks = np.linspace( -10, 10, 21 )
    ax[ 0 ].ylim = ( -10, 10 )
    ax[ 1 ].ylim = ( -10, 10 )
    ax[ 0 ].yticks = np.linspace( -10, 10, 21 )
    ax[ 1 ].yticks = np.linspace( -10, 10, 21 )

    # Create and plot a degenerate conic represented by two distinct, and
    # parallel lines.
    f1 = CLine( ( 1, 0, -1 ), name = 'f1' )
    g1 = CLine( ( 1, 0, -7 ), name = 'g1' )
    C1 = CConic( degenerate = ( f1, g1 ), name = 'C1' )
    print( C1 )
    print( f'The rank of {C1.name} is {C1.rank}.\n' )
    ax[ 0 ].plot( C1, '-b', cconicsamples = ( 101, 101 ), linewidth = 1.0 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # Creating and plotting a sequence of pairs of pole-polar for this degenerate
    # conic.
    pole = CPoint( ( -15, 0, 0 ), 'pole' )
    polar: CLine = C1 * pole
    polar.name = 'polar'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'ob', polar, '--b', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    pole = CPoint( ( -5.0, 0 ), 'pole' )
    polar: CLine = C1 * pole
    polar.name = 'polar'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'or', polar, '--r', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    pole = CPoint( ( 0.0, 0.0 ), 'pole' )
    polar: CLine = C1 * pole
    polar.name = 'polar'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'og', polar, '--g', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    pole = CPoint( ( 1.0, 0.0 ), 'pole' )
    polar: CLine = C1 * pole
    polar.name = 'polar'
    print( f'Does the {pole.name} lie in {C1.name}? {pole in C1}' )
    print( f'Does the {pole.name} lie in {polar.name}? {pole in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'om', polar, '--m', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    pole = CPoint( ( 2.5, 0.0 ), 'pole' )
    polar: CLine = C1 * pole
    polar.name = 'polar'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'ok', polar, '--k', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    pole = CPoint( ( 4.0, 0.0 ), 'pole' )
    polar: CLine = C1 * pole
    polar.name = 'polar'
    print( polar )
    print( pole, '\n' )
    ax[ 0 ].plot( pole, 'oc', polar, '--c', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    # The operation CConic * CLine can not be performed because the conic C1
    # is not full rank. Therefore, if you do this operation, the point returned
    # will be a point at infinity. See the example above:
    polar = CLine( ( 1, 0, 8 ), 'polar' )
    pole: CPoint = C1 * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    # Create and plot a degenerate conic represented by two concurrent lines.
    f2 = CLine( ( 2.5, 1, 14.5 ), name = 'f2' )
    g2 = CLine( ( 0.8, -1, 2 ), name = 'g2' )
    C2 = CConic( degenerate = ( f2, g2 ), name = 'C2' )
    print( C2 )
    print( f'The rank of {C2.name} is {C2.rank}.\n' )
    ax[ 1 ].plot( C2, '-b', cconicsamples = ( 101, 101 ), linewidth = 1.0 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # Creating and plotting a sequence of pairs of pole-polar for this degenerate
    # conic.
    # A point in g2 is going to return the "polar" g2.
    pole = CPoint( ( 0, 2 ), 'pole' )
    polar: CLine = C2 * pole
    polar.name = 'polar'
    print( f'Does the {pole.name} lie in {C2.name}? {pole in C2}' )
    print( f'Does the {pole.name} lie in {polar.name}? {pole in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'or', polar, '--r', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # A point in f2 is going to return the "polar" f2.
    pole = CPoint( ( -7, 3 ), 'pole' )
    polar: CLine = C2 * pole
    polar.name = 'polar'
    print( f'Does the {pole.name} lie in {C2.name}? {pole in C2}' )
    print( f'Does the {pole.name} lie in {polar.name}? {pole in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'or', polar, '--r', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

    # A point in f2 and g2 is going to return the "polar" at infinity.
    pole = CPoint( ( -5, -2 ), 'pole' )
    polar: CLine = C2 * pole
    polar.name = 'polar'
    print( f'Does the {pole.name} lie in {C2.name}? {pole in C2}' )
    print( f'Does the {pole.name} lie in {polar.name}? {pole in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'or', polar, '--r', linewidth = 1.0, markersize = 3 )

    # Any points outside the lines g2 and f2 will return a "polar" line that
    # passes through the point of intersection between g and f.
    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    # Point of intersection.
    p_i = CPoint( ( -5, -2 ), 'p_i' )
    print( p_i, '\n' )

    pole = CPoint( ( 0, 0 ), 'pole' )
    polar: CLine = C2 * pole
    polar.name = 'polar'
    print( f'Does the {p_i.name} lie in {polar.name}? {p_i in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'og', polar, '--g', linewidth = 1.0, markersize = 3 )

    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    pole = CPoint( ( -5, 7 ), 'pole' )
    polar: CLine = C2 * pole
    polar.name = 'polar'
    print( f'Does the {p_i.name} lie in {polar.name}? {p_i in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'om', polar, '--m', linewidth = 1.0, markersize = 3 )

    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    pole = CPoint( ( -9, -2 ), 'pole' )
    polar: CLine = C2 * pole
    polar.name = 'polar'
    print( f'Does the {p_i.name} lie in {polar.name}? {p_i in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'ok', polar, '--k', linewidth = 1.0, markersize = 3 )

    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    pole = CPoint( ( -5, -7 ), 'pole' )
    polar: CLine = C2 * pole
    polar.name = 'polar'
    print( f'Does the {p_i.name} lie in {polar.name}? {p_i in polar}' )
    print( polar )
    print( pole, '\n' )
    ax[ 1 ].plot( pole, 'oc', polar, '--c', linewidth = 1.0, markersize = 3 )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    # Again, the operation CConic * CLine can not be performed because the
    # conic C2 is not full rank. See the example above:
    polar = CLine( ( 1, 0, 8 ), 'polar' )
    pole: CPoint = C2 * polar
    pole.name = 'pole'
    print( polar )
    print( pole, '\n' )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    # Create a degenerate conic represented by two coincident lines.
    f3 = CLine( ( 13, -14, -22 ), name = 'f3' )
    C3 = CConic( degenerate = ( f3, f3 ), name = 'C3' )
    print( C3 )
    print( f'The rank of {C3.name} is {C3.rank}.\n' )

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    # For points in C3, the "polar" lines that are returned are at infinity.
    # See the examples in the console.
    pole = CPoint( ( 6, 4 ), name = 'pole' )
    print( pole )
    print(f'Does the {pole.name} lie in {C3.name}? {pole in C3}')
    polar: CLine = C3 * pole
    polar.name = 'polar'
    print( polar, '\n' )

    pole = CPoint( ( -8, -9 ), name = 'pole' )
    print( pole )
    print(f'Does the {pole.name} lie in {C3.name}? {pole in C3}')
    polar: CLine = C3 * pole
    polar.name = 'polar'
    print(polar, '\n')

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input('Press any key to continue...')

    # For points outside C3, the "polar" lines that are returned are
    # the same as f3. See the examples in the console.
    pole = CPoint( ( 2, -3 ), name = 'pole' )
    print( pole )
    polar: CLine = C3 * pole
    polar.name = 'polar'
    print( polar )
    print(f'Does {f3} equal to {polar}? {f3 == polar}', '\n' )

    pole = CPoint( ( 0, 0 ), name = 'pole' )
    print( pole )
    polar: CLine = C3 * pole
    polar.name = 'polar'
    print( polar )
    print(f'Does {f3} equal to {polar}? {f3 == polar}', '\n' )

    pole = CPoint( ( -5, 9, 0 ), name = 'pole' )
    print( pole )
    polar: CLine = C3 * pole
    polar.name = 'polar'
    print( polar )
    print(f'Does {f3} equal to {polar}? {f3 == polar}', '\n' )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/poles-and-polar/poles-polars-degenerate.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/poles-and-polar/poles-polars-degenerate.jpeg"/>
</p>

------------

- **Getting the area of the conics.**

The area $A$ of the conics is given by:

1. if the conic is a hyperbole, two distinct, and parallel lines, or two
concurrent lines, then $A = \infty$.
2. if the conic is two coincident lines, then $A = 0$.
3. if the conic is an ellipse/circle, then
$$
A = \frac{ \pi }{ \sqrt{-\text{det}( C )} }\enspace,
$$
where $A$ is a symmetric matrix that represents the conic.

<span style="color:green">**NOTE:**<br></span>
*The area of the conics is invariant under rotation and translation transformations.*

```python
    from pyConics import CFigure, CAxes
    from pyConics import CPoint, CLine
    from pyConics import CConic
    from pyConics import cconst

    import numpy as np

    # Create an empty figure.
    # Its width and height are relative to the screen size.
    width = 0.35
    f: CFigure = CFigure( (width, 16.0 / 9.0 * width ) )

    # Create a 1x1 grid of axes from f.
    # The title font size is 9.
    f.create_axes( ( 1, 1 ) )

    # Get the tuple of CAxes classes for the 1x1 grid.
    ax = f.axes

    # Define a title.
    ax[ 0 ].title = 'Area of conics.'

    # Change its axis.
    ax[ 0 ].xlim = ( -10, 10 )
    ax[ 0 ].xticks = np.linspace( -10, 10, 21 )
    ax[ 0 ].ylim = ( -10, 10 )
    ax[ 0 ].yticks = np.linspace( -10, 10, 21 )

    # Create and plot a circle.
    xy = CPoint( ( 0.0, 0.0 ) )
    C0 = CConic( 3.0, name = 'C0' )
    A = C0.area()
    print( C0 )
    print( f'The rank of {C0.name} is {C0.rank}.' )
    print( f'The area of {C0.name} is {A:0.4f}.\n' )
    ax[ 0 ].plot( C0, '-b', cconicsamples = ( 101, 101 ), linewidth = 1.0 )
    ax[ 0 ].text( xy.x - 1.0, xy.y, f'A={A:0.2f}' )

    # Create and plot an ellipse.
    xy = CPoint( ( 0.0, 7.0 ) )
    C1 = CConic( 3.0, 2.0, center = xy, name = 'C1' )
    A = C1.area()
    print( C1 )
    print( f'The rank of {C1.name} is {C1.rank}.' )
    print( f'The area of {C1.name} is {A:0.4f}.\n' )
    ax[ 0 ].plot( C1, '-r', cconicsamples = ( 101, 101 ), linewidth = 1.0 )
    ax[ 0 ].text( xy.x - 1.0, xy.y, f'A={A:0.2f}' )

    # Create and plot the same ellipse as C1, but it will be rotated and
    # tranlated.
    xy = CPoint( ( 7.0, 7.0 ) )
    C2 = CConic( 3.0, 2.0, 60.0 / 180.0 * cconst.pi, xy, name = 'C2' )
    A = C2.area()
    print( C2 )
    print( f'The rank of {C2.name} is {C2.rank}.' )
    print( f'The area of {C2.name} is {A:0.4f}.\n' )
    ax[ 0 ].plot( C2, '-r', cconicsamples = ( 101, 101 ), linewidth = 1.0 )
    ax[ 0 ].text( xy.x - 1.0, xy.y, f'A={A:0.2f}' )

    # Create and plot a hyperbole.
    xy = CPoint( ( -7.0, 6.0 ) )
    C3 = CConic( np.sqrt( 2.0 ), 3.0, -45.0 / 180.0 * cconst.pi, xy, name = 'C3' )
    A = C3.area()
    print( C3 )
    print( f'The rank of {C3.name} is {C3.rank}.' )
    print( f'The area of {C3.name} is {A:0.4f}.\n' )
    ax[ 0 ].plot( C3, '-g', cconicsamples = ( 101, 101 ), linewidth = 1.0 )
    ax[ 0 ].text( xy.x - 0.5, xy.y, f'A={A:0.2f}' )

    # Create and plot a degenerate conic with two coincident lines.
    p1 = CPoint( ( 9, 5 ) )
    p2 = CPoint( ( 3, -9 ) )
    g: CLine = p1 * p2
    C4 = CConic( degenerate = ( g, g ), name = 'C4' )
    A = C4.area()
    print( C4 )
    print( f'The rank of {C4.name} is {C4.rank}.' )
    print( f'The area of {C4.name} is {A:0.4f}.\n' )
    ax[ 0 ].plot( C4, '-y', cconicsamples = ( 101, 101 ), linewidth = 1.0 )
    ax[ 0 ].text( 7, 0, f'A={A:0.2f}' )

    # Create and plot a degenerate conic with two distinct, and parallel lines.
    l1 = CLine( ( 0, 1, 9 ) )
    l2 = CLine( ( 0, 1, 7 ) )
    C5 = CConic( degenerate = ( l1, l2 ), name = 'C5' )
    A = C5.area()
    print( C5 )
    print( f'The rank of {C5.name} is {C5.rank}.' )
    print( f'The area of {C5.name} is {A:0.4f}.\n' )
    ax[ 0 ].plot( C5, '-m', cconicsamples = ( 101, 101 ), linewidth = 1.0 )
    ax[ 0 ].text( -8, -8, f'A={A:0.2f}' )

    # Create and plot a degenerate conic with two distinct, and parallel lines.
    l1 = CLine( ( 1, 1, 9 ) )
    l2 = CLine( ( 1, -1, 5 ) )
    C6 = CConic( degenerate = ( l1, l2 ), name = 'C6' )
    A = C6.area()
    print( C6 )
    print( f'The rank of {C6.name} is {C6.rank}.' )
    print( f'The area of {C6.name} is {A:0.4f}.\n' )
    ax[ 0 ].plot( C6, '-c', cconicsamples = ( 101, 101 ), linewidth = 1.0 )
    ax[ 0 ].text( -6.6, -2, f'A={A:0.2f}' )

    # Show Figure on screen.
    CFigure.show()
```

<p align="center">
    <!-- <img src="./docs/figs/utils/cconic-area.jpeg"/> -->
    <img src="https://raw.githubusercontent.com/osowsky/pyConics/main/docs/figs/utils/cconic-area.jpeg"/>
</p>

------------

## Contributing

Interested in contributing? Check out the [contributing guidelines](https://raw.githubusercontent.com/osowsky/pyConics/main/CONTRIBUTING.md).
Please note that this project is released with a [Code of Conduct](https://raw.githubusercontent.com/osowsky/pyConics/main/CONDUCT.md).
By contributing to this project, you agree to abide by its terms.

------------

## License

`pyConics` was created by Jefferson Osowsky.
It is licensed under the terms of the [GNU General Public License v3.0 license](https://raw.githubusercontent.com/osowsky/pyConics/main/LICENSE).

------------

## Credits

`pyConics` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/)
and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

`pyConics` has used the following Python packages since its creation:

- [`numpy`](https://numpy.org/doc/stable/)
- [`matplotlib (pyPlot)`](https://matplotlib.org/stable/tutorials/pyplot.html)
- [`PyAutoGUI`](https://pyautogui.readthedocs.io/en/latest/#)
- [`pytest`](https://docs.pytest.org/en/7.4.x/)
