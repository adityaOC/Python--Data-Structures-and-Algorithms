
def quickSort(arr):

   
    #todo: check for single element in array
    quickSortHelper(arr,0,len(arr)-1)





def quickSortHelper(arr,first,last):

    if first < last:

        partitionPosition = partition(arr, first, last)
        quickSortHelper(arr,first,partitionPosition-1)
        quickSortHelper(arr,partitionPosition+1,last)




def partition(arr, first, last):
    pivotvalue = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


arr = [2,5,4,6,7,3,1,4,12,11]
quickSort(arr)
print(arr)





