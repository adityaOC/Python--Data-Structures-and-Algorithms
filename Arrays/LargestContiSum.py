
def largestContiSum(arr):

    #edge case
    if len(arr)<1 :
        return 0


    max_sum = current_sum = arr[0]

    for n in arr[1:]:

        current_sum = max(current_sum + n,n)

        max_sum = max(current_sum,max_sum)

    print(max_sum)

largestContiSum([1,2,-5,3,4,])

