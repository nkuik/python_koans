#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
def triangle(a, b, c):
    if ((a <= 0) or (b <= 0) or (c <= 0) or
        (a + b < c) or (b + c < a) or (c + a < b)):
        raise TriangleError
    else:
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
class TriangleError(Exception):
    pass
