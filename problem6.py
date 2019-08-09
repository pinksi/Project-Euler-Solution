# Solution of project euler problem 6

def calculateSquares(num):
    return num * num;

def calculateDifference(num1, num2):
    return (num1-num2) if num1 > num2 else (num2 - num1)

def calculateSOS():
    sum1 =0; sum2 = 0;
    for i in range(1,101,1):
        sum1 = sum1 + calculateSquares(i);
        sum2 = sum2 + i;
    sum2 = calculateSquares(sum2)

    result = calculateDifference(sum1, sum2)
    print(result)

calculateSOS()