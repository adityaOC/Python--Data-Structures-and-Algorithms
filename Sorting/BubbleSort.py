

def bubbleSort(arr):

    for outer in range(len(arr)-1):
        for inner in range (len(arr)-1):

            if arr[inner]> arr[inner + 1]:
                temp = arr[inner]
                arr[inner] = arr[inner + 1]
                arr[inner + 1] = temp

    print(arr)



list = [5,4,3,2,1]

bubbleSort(list)




