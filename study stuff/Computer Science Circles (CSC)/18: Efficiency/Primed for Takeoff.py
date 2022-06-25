isPrime = [True] * 1000001


def isItPrime(N):  # same as before
    for D in range(2, N):
        if (D * D > N):  # first added line
            break  # second added line
        if N % D == 0:
            return False
    return True
    

for i in range(1000001):
    if isItPrime(i):
        isPrime[i] = False
    
print(isPrime)
