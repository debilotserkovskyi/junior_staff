def hailstone(n):
    if n % 2 == 0:
        return hailstone(n/2)
    elif n == 1:
        return n
    else:
        return hailstone(3*n+1)
  

print(hailstone(5))
