from math import factorial


def choose(n:int, k:int):
    return factorial(n)/(factorial(n-k)*factorial(k))
