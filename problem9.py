# solution to project euler problem 9 

def check_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def main():
    for i in range(1, 1000):
        for j in range(i, 1000 - i):
            for k in range(j, 1000 - j):
                if i + j + k == 1000:
                    if check_pythagorean_triplet(i, j, k):
                        print(i * j * k) 

main()