


def getMax(arr):

    if len(arr) == 1:
        return arr[0]
    #base case
    if len(arr)==2:
        return max(arr[0],arr[1])

    mid = len(arr)//2
    maxLeft = getMax(arr[:mid])
    maxRight = getMax(arr[mid:])

    return max(maxLeft,maxRight)


#arr = [8,2,4,5,10,11,1,3,9]
arr = [1000, 11, 445, 1, 330, 3000]
print(getMax(arr))

