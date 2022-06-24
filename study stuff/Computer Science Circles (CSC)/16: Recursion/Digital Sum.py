def digitalSum(n:int):
    if n < 10:
        return n
    return n % 10 + digitalSum(n//10)
    
