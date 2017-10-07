def cumulativeSum(n):

    """this fucntion uses recursion to calculate cumulativeSum
     example n=4 then 4+3+2+1+0 = 10
             n=6 then 6+5+4+3+2+1+0 = 21
     
     """

    if n == 0:
        return 0
    else:
        return n + cumulativeSum(n-1)


print("Cumulative Sum = {}".format(cumulativeSum(6)))


