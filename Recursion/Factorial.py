
def fact(n):

    """this fucntion uses recursion to calculate factorial of a number"""

    if n == 0:
        return 1
    else:
        return n * fact(n-1)


print("factorial = {}".format(fact(5)))


