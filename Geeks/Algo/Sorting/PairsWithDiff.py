
from Search.BinarySearch import binarySearch

"""
def getPairsWithDefference(arr,k):

    if len(arr)== 1 :
        return None

    pairs = set()
    for n in arr:

        target = n + k


        if binarySearch(arr,target):
            pairs.add((n, target))



    print(pairs)

"""


def getDiffUsingHash(arr,k):
    count = 0
    hashMap = {}
    pairs = set()
    for i in arr:
        hashMap[i] = True

    for n in arr:


        target = n + k
        if target in hashMap:
            maxV = max(target, n)
            minV = min(target, n)
            pairs.add((maxV, minV))

        target = n - k
        if target in hashMap:
            maxV = max(target,n)
            minV  = min(target,n)
            pairs.add((maxV, minV))
    print(pairs)



arr = [8, 12, 16, 4, 0, 20]
k = 4
#quickSort(arr)
#getPairsWithDefference(arr,k)

getDiffUsingHash(arr,k)






