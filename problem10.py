# Solution of project euler problem 10 [Summation of primes]

def isPrime(num):
    if num > 1:
        if num == 2: return True
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

sum = 0
for i in range(1, 2000000):
    if isPrime(i):
        sum = sum + i
print("The sum of all primes below two million is:", sum)

