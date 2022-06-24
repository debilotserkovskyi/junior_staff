def digitalSum(n: int):
    if n < 10:
        return n
    return n % 10 + digitalSum(n // 10)


def digitalRoot(n):
    if n < 10:
        return n
    else:
        n = digitalRoot(digitalSum(n))
        return n
