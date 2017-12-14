

def selection_sort(arr):

    for outer in range(len(arr)-1):
        minPos = outer

        for inner in range(outer + 1,len(arr)):

            if arr[inner]< arr[minPos]:
                minPos = inner

        temp = arr[outer]
        arr[outer] = arr[minPos]
        arr[minPos] = temp



arr = [3,3,2,7,6,8,12,40,21]
selection_sort(arr)
print(arr)




