from swampy.TurtleWorld import *

def my_square(x,y,side_length): #takes as input the coordinates of the lower lefthand corner and the side length of a square and draws the square to the Turtle world canvas
    world = TurtleWorld()
    bob = Turtle()
    sides_of_square = 4
    for i in range(sides_of_square):
        fd(bob, dist=side_length)
        lt(bob, angle=90)

def my_regular_polygon(x,y,side_length,number_of_sides):
    world = TurtleWorld()
    bob = Turtle()
    exterior_angle = 360/number_of_sides
    for i in range(number_of_sides):
        fd(bob, dist=side_length)
        lt(bob, angle=exterior_angle)


def my_circle(x,y,radius):
    from math import pi
    approximation = 30
    side_length = 2 * pi * radius / approximation
    my_regular_polygon(x,y-radius,side_length,approximation)

def snow_flake_side(turtle, l, level):
    """ Draw a side of the snowflake curve with side length l and recursion depth of level """

    print 'chicken'

def snow_flake(turtle,l,level):
    if level == 0:
        return
    else:
        fd(turtle, dist= snow_flake(turtle, l/3, level-1))
        rt(turtle, angle=60)
        fd(turtle, dist=snow_flake(turtle, l/3, level-1))
        rt(turtle, angle=120)
        fd(turtle, dist=snow_flake(turtle, l/3, level-1))
        rt(turtle, angle=60)
        fd(turtle, dist=snow_flake(turtle, l/3, level-1))




snow_flake('bob', 30, 3)