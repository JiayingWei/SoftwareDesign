# -*- coding: utf-8 -*-
"""
Random_art.py

@author: jiayingwei, adapted from amonmillner's work, adapted from pruvolo's work
"""

# you do not have to use these particular modules, but they may help
from random import randint
import math
import Image

def build_random_function(min_depth, max_depth):
    """ Creates a random function composed of products, cos(pi * var), and sins(pi * var)) using recursion 
        to a random depth between the minimum and maximum depth provided
    """
    operations = ["prod","cos_pi","sin_pi"]
    if max_depth > 0:   #picks a random depth between the min and max provided
        min_depth = randint(min_depth,max_depth)
        max_depth = 0
    theOp = operations[randint(0,len(operations)-1)]
    if min_depth == 1:    #basecase for recursion
        variables = ["x","y"]
        if theOp == "prod":
            return [theOp, variables[randint(0,len(variables)-1)] , variables[randint(0,len(variables)-1)] ]
        else:
            return [theOp, variables[randint(0,len(variables)-1)]] 
    if theOp == "prod":    #recursive part
        return [theOp, build_random_function(min_depth -1, 0) , build_random_function(min_depth -1, 0) ]
    else:
        return [theOp, build_random_function(min_depth -1, 0)]

def evaluate_random_function(f, x, y):
    """ Calculates the output of [x,y] after interperating f as a mathmatical equation f(x,y)
    """
    if f[0] == "x":     #basecase for recursion
        return x
    if f[0] == "y":
        return y
    if f[0] == "prod":    #recursive portions
        return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)
    if f[0] == "sin_pi":
        return math.sin(math.pi * evaluate_random_function(f[1], x, y))
    if f[0] == "cos_pi":
        return math.cos(math.pi * evaluate_random_function(f[1], x, y))

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    """
    return (float(val) - input_interval_start) * (output_interval_end - output_interval_start) / (input_interval_end - input_interval_start) + output_interval_start
    
def paint(image_size_px, min_depth, max_depth):
    im = Image.new("RGB",(image_size_px,image_size_px))
    pixels = im.load()
    R = build_random_function(min_depth,max_depth)      #creates the random functions for the RBG layers
    B = build_random_function(min_depth,max_depth)
    G = build_random_function(min_depth,max_depth)
    for x in range(0,image_size_px):                    #iterates through all the pixels
        for y in range(0,image_size_px):
            mx = remap_interval(x,1,image_size_px,-1,1)
            my = remap_interval(y,1,image_size_px,-1,1)
            rpx = remap_interval(evaluate_random_function(R,mx,my),-1,1,1,image_size_px)    #runs the x and y values through the random recursive functions
            bpx = remap_interval(evaluate_random_function(B,mx,my),-1,1,1,image_size_px)
            gpx = remap_interval(evaluate_random_function(G,mx,my),-1,1,1,image_size_px)
            pixels[x,y] = (int(rpx),int(bpx),int(gpx))  #remaps all the colors
    im.save("images/test18.jpg")

imgsquarepx = 500   #size of art nxn
min_depth = 1       #depth of recursion
max_depth = 10

paint(imgsquarepx,min_depth,max_depth)

