# Week 4, Session 2: Task 2

# Given incomplete function point_properties(x1,y1,x2,y2) that takes the coordinates
# of two points (𝑥1,𝑦1) and (𝑥2,𝑦2) and returns both the distance between
# the points and the coordinates of the midpoint. The formula to find
# mid point of x = (x1+x2)/2, y = (y1+y2)/2. Return the midpoint as a tuple.
# The formula to find the distance between the two point,
# distance = √((x2 – x1)² + (y2 – y1)²). You can use math.sqrt() to find
# the square root of a number. The function returns the two values in the
# order: distance, midpoint

import math


def point_properties(x1, y1, x2, y2):
    # complete your code here

    return dist, mid_point


# Check if correct output is produced
dist, mid = point_properties(0, 0, 4, 3)    # dist=5.0, mid = (2.0, 1.5)
