#!/usr/bin/env python
# -*- coding: utf-8 -*-


# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal


def triangle(a, b, c):
    if (a == b) and (a == c):
        return 'equilateral'
    elif (
            ((a == b) or (a == c) or (b == c)) and
            ((b == c) or (b == a) or (a == c))
         ):
        return 'isosceles'
    else:
        return 'scalene'



# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
