# Solution of project euler problem 7

def isPrime(k):
    if k <2: return "Neither prime nor composite"
    for i in range(2, int(k**0.5)+1):
        if (k % i) == 0:
            return False
    else:
        return True

def nthPrime(n):
    prime_count = 0
    prime = 1
    while prime_count < n:
        prime +=1
        if isPrime(prime):
            prime_count +=1
    return prime

print(nthPrime(10001))


