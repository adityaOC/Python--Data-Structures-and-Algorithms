
def sort(arr):

    low = 0
    mid = 0
    high = len(arr)-1

    while mid<=high:

        if arr[mid] == 0:

            temp = arr[mid]
            arr[mid] = arr[low]
            arr[low] = temp
            low+=1
            mid+=1
        elif arr[mid] == 1:
            mid += 1

        else:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp

            high -= 1



arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort(arr)
print(arr)
