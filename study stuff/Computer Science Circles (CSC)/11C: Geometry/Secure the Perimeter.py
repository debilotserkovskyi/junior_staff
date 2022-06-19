import math


def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def distance2D(x1, y1, x2, y2):
    return hypotenuse(a=x1-x2, b=y1-y2)


def trianglePerimeter(xA, yA, xB, yB, xC, yC):
    return distance2D(xA,yA, xB, yB) + distance2D(xB, yB, xC, yC) + distance2D(xC, yC, xA,yA)
