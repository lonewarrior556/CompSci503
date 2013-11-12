

# Exercise 15.1. Write a function called distance_between_points that takes 
# two Points as arguments and returns the distance between them.

def distance_between_points(a,b):
    x=abs(a[0]-b[0])
    y=abs(a[1]-b[1])
    c=(x**2+y**2)**.5
    return c

# Exercise 15.2. Write a function named move_rectangle that takes a Rectangle 
# and two numbers named dx and dy. It should change the location of the 
# rectangle by adding dx to the x coordinate of corner and adding dy to the 
# y coordinate of corner.

def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y+=dy
    

# Exercise 15.3. Write a version of move_rectangle that creates and returns a 
# new Rectangle instead of modifying the old one.

def move_rectangle2(rect,dx,dy):
    import copy
    nrect=copy.deepcopy(rect)
    nrect.corner.x+=dx
    nrect.corner.y+=dy
    return nrect


# Exercise 15.4. Swampy (see Chapter 4) provides a module named World, which 
# defines a user- defined type also called World. You can import it like this:

# from swampy.World import World
# Or, from World import World

# The following code creates a World object and calls the mainloop method, 
# which waits for the user.

# world = World()
# world.mainloop()

# A window should appear with a title bar and an empty square. We will use this 
# window to draw Points, Rectangles and other shapes. Add the following lines 
# before calling mainloop and run the program again.

# canvas = world.ca(width=500, height=500, background='white')
# bbox = [[-150,-100], [150, 100]]
# canvas.rectangle(bbox, outline='black', width=2, fill='green4')

# You should see a green rectangle with a black outline. The first line 
# creates a Canvas, which appears in the window as a white square. The 
# Canvas object provides methods like rectangle for drawing various shapes.
# bbox is a list of lists that represents the “bounding box” of the rectangle. 
# The first pair of coordinates is the lower-left corner of the rectangle; 
# the second pair is the upper-right corner.
# You can draw a circle like this:

# canvas.circle([-25,0], 70, outline=None, fill='red')

# The first parameter is the coordinate pair for the center of the circle; 
# the second parameter is the radius.
# If you add this line to the program, the result should resemble the 
# national flag of Bangladesh 

# 1. Write a function called draw_rectangle that takes a Canvas and a Rectangle 
# as arguments and draws a representation of the Rectangle on the Canvas.

# 2. Add an attribute named color to your Rectangle objects and modify 
# draw_rectangle so that it uses the color attribute as the fill color.

# 3. Write a function called draw_point that takes a Canvas and a Point as 
# arguments and draws a representation of the Point on the Canvas.

# 4. Define a new class called Circle with appropriate attributes and 
# instantiate a few Circle objects. Write a function called draw_circle that 
# draws circles on the canvas.

# 5. Write a program that draws the national flag of the Czech Republic. 
# Hint: you can draw a polygon like this:

# points = [[-150,-100], [150, 100], [150, -100]]
# canvas.polygon(points, fill='blue')

