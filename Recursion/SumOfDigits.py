def sumOfDigits(n):

    """this function calculates the sum of digits"""

    if n/10 == 0:
        return n
    else:
        lastDigit = n%10
        return lastDigit + sumOfDigits(int(n/10))

print(sumOfDigits(54321))
