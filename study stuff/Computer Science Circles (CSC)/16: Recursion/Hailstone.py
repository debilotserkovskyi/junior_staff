def hailstone(n):
    print(int(n))
    if n % 2 == 0:
        return hailstone(n/2)
    elif n == 1:
        return int(n)
    else:
        return hailstone(3*n+1)
  

print(hailstone(4))
