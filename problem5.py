#Project Euler solution of problem 5
def checkdivisible(num):
    for i in range(2,21):
        if num%i != 0:
            return False
    return True

num = 20
while True:
    if checkdivisible(num):
        break
    else:
        num = num + 1

print(num)