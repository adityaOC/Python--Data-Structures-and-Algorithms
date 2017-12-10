
def arrayPairSum(arr,sum):

    if len(arr) < 2:
        return

    seen = set()
    pairs = set()
    for num in arr:

        target = sum - num

        if target not in seen:
            seen.add(num)
        else:
            pairs.add((min(num,target), max(num,target)))

    print(pairs)


arrayPairSum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)




