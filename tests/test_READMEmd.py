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

def test_Lines():
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

def test_Points_And_Lines():
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

def test_Set_Up():
    from pyConics import CFigure, CAxes
    import numpy as np

    # Set interactive mode.
    # Activate this mode so that it is not necessary to call the show() method.
    # Whether you comment this line or use CFigure.ioff() method, the show()
    # method must be called.
    # CFigure.ion()

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

    #----------------------------------------------------------------------------
    # Next code segment.

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

    #----------------------------------------------------------------------------
    # Next code segment.
    
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

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

def test_Font_Size():
    from pyConics import CFigure, CAxes

    # Set interactive mode.
    # CFigure.ion()

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

    # If CFigure.ion() is on then you need to press a key to continue.
    if ( CFigure.is_interactive() ):
        input( 'Press any key to continue...' )

def test_Plot_Point():
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
    # CFigure.show()

def test_Plot_List_Point():
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
    p = np.array( [ [ 0.3, 0.1 ],       # p = ( 0.3, 0.1 )
                    [ 0.3, 0.2 ],       # p = ( 0.3, 0.2 )
                    [ 0.3, 0.3 ],       # p = ( 0.3, 0.3 )
                    [ 0.3, 0.4 ],       # p = ( 0.3, 0.4 )
                    [ 0.3, 0.5 ] ] )    # p = ( 0.3, 0.5 )

    # Creating a list of points using CPoint.
    p1 = CPoint( ( 0.7, 0.5 ), 'p1' )
    p2 = CPoint( ( 0.7, 0.6 ), 'p2' )
    p3 = CPoint( ( 0.7, 0.7 ), 'p3' )
    p4 = CPoint( ( 0.7, 0.8 ), 'p4' )
    p5 = CPoint( ( 0.7, 0.9 ), 'p5' )
    pl = [ p1, p2, p3, p4, p5 ]

    # Plotting both the lists of points
    ax[ 0 ].plot( p[ :, 0 ], p[ :, 1 ], 'ob', pl, '^m', markersize = 8 )

    # Show Figure on screen.
    # CFigure.show()

def test_Plot_Line():
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
    # CFigure.show()

def test_Plot_List_Line():
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
    # CFigure.show()

def test_Plot_Line_Segment():
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
    # CFigure.show()

def test_Solve_A_Simple_Problem_Of_Geometry():
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
    # CFigure.show()

def test_Conics_Ellipses():
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

def test_Conics_Hyperbole():
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

def test_Conics_Degenerate():
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

def test_Points_Lines_Conics():
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

def test_Envelope():
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

#------------------------------------------------------------------
# For development and test.
#  
if __name__ == '__main__':
    # Test point script for README.md usage.
    # test_Points()
    # test_Lines()
    # test_Points_And_Lines()
    # test_Set_Up()
    # test_Font_Size()
    # test_Plot_Point()
    # test_Plot_List_Point()
    # test_Plot_Line()
    # test_Plot_List_Line()
    # test_Plot_Line_Segment()
    # test_Solve_A_Simple_Problem_Of_Geometry()
    # test_Conics_Ellipses()
    # test_Conics_Hyperbole()
    # test_Conics_Degenerate()
    # test_Points_Lines_Conics()
    test_Envelope()
