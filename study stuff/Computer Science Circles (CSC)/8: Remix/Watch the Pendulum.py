import math

l = float(input())
a = float(input())

for t in range(10):
    x = l * math.cos(a * math.cos(t * math.sqrt(9.8/l))) - l * math.cos(a)
    print(x)
    