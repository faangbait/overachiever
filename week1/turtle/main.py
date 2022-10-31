import turtle
from functools import partial

turtle.delay(0)
turtle.speed(0)
turtle.bgcolor(0.1, 0.1, 0.1)
turtle.title("Alfy.io bootcamp submission - week 1 - turtle")

def draw_shape(sides, fill=(0,0,0)):
    """
        Draws a polygon with a given number of sides and fills it with the specified color.
        
        Args:
            sides (int)
                The number of sides in the shape
            fill (float, float, float)
                The RGB color of the fill
    """
    angle = 360 / sides
    t.fillcolor(fill)
    t.begin_fill()
    for _ in range(sides):
        t.forward(EDGE_LENGTH)
        t.right(angle)
    t.end_fill()

# Declare constants

EDGE_LENGTH = 80 # Sets the length of the edge. Reduce for smaller screens.
COLOR1 = (160/255, 116/255, 69/255)
COLOR2 = (233/255, 245/255, 235/255)
COLOR3 = (40/255, 75/255, 77/255)

# The sides of a hex, square, and triangle are unchanging, so we declare these as partials.
hexagon = partial(draw_shape, 6)
square = partial(draw_shape, 4)
triangle = partial(draw_shape, 3)


def draw_pattern():
    """
        Draws a tesselated pattern consisting of a hex, six squares, and six triangles.
        Inspiration from the floor of the Archeological Museum in Seville, Spain.

        Notable differences: the museum features a true rhombitrihexagonal tiling, which means
        the triangles would never connect. In this implementation, they do connect. I preferred the
        look of the "undrawn" white triangles.
    """
    t.pendown()
    hexagon(COLOR1)
    t.right(120)
    square(COLOR2)
    t.right(90)
    triangle(COLOR3)
    move_to_next_vertex()
    square(COLOR2)
    t.right(90)
    triangle(COLOR3)
    move_to_next_vertex()
    square(COLOR2)
    t.right(90)
    triangle(COLOR3)
    move_to_next_vertex()
    square(COLOR2)
    t.right(90)
    triangle(COLOR3)
    move_to_next_vertex()
    square(COLOR2)
    t.right(90)
    triangle(COLOR3)
    move_to_next_vertex()
    square(COLOR2)
    t.right(90)
    triangle(COLOR3)
    move_to_next_vertex()
    t.right(240)
    move_to_next_pattern()

def move_to_next_vertex():
    """Moves the turtle to the next corner of the current hex and orients"""
    t.left(90)
    t.forward(EDGE_LENGTH)
    t.left(60)

def move_to_absolute_center():
    t.home()
    t.penup()
    t.left(90)
    t.forward(EDGE_LENGTH)
    t.left(30)
    t.forward(EDGE_LENGTH)
    t.left(90)
    t.forward(EDGE_LENGTH)
    t.right(60)
    t.forward(EDGE_LENGTH)
    t.right(60)
    t.forward(EDGE_LENGTH)
    t.right(60)
    t.pendown()

def move_to_next_pattern():
    """Moves the turtle to the top-left corner of the next hex and orients"""
    t.penup()
    t.forward(EDGE_LENGTH)
    t.left(30)
    t.forward(EDGE_LENGTH)
    t.left(60)
    t.forward(EDGE_LENGTH)
    t.left(30)
    t.forward(EDGE_LENGTH)
    t.right(60)
    t.pendown()

if __name__ == "__main__":
    """
        This could be improved by using recursion to create an ever-expanding tesselation.
        In this implementation, we simply draw a center pattern before drawing six edge patterns.
    """
    t = turtle.Turtle()

    # draw center pattern
    move_to_absolute_center()
    draw_pattern()
    t.penup()
    t.home()
    # draw surrounding patterns
    for _ in range(6):
        draw_pattern()

    # add a title
    move_to_absolute_center()
    t.penup()
    t.forward(EDGE_LENGTH)
    t.right(120)
    font_height = EDGE_LENGTH // 10
    t.forward(EDGE_LENGTH+(font_height*1.5))
    t.write("Alfy.io", align='center', font=('arial', font_height, 'bold'))
    
    # move the turtle off the image
    t.penup()
    t.setpos(9999,9999)
    turtle.mainloop()
