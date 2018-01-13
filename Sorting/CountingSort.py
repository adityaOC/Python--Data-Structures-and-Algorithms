def countSort(arr,k):
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(k)]

    # For storing the resulting answer since the

    # Store count of each character
    for i in arr:
        count[i] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(1,k):
        count[i] += count[i - 1]

    for i in range(len(arr)-1, -1, -1):

        output[count[arr[i]]-1] = arr[i]
        count[arr[i]]-= 1


    # Build the output character array
    return output


# Driver program to test above function
arr = [0,3,4,3,0,1,0,3,2,2,2,2,2,1,4]
ans = countSort(arr,5)
print("Input unsorted array : {}".format(arr))
print("output sorted array : {}".format(ans))
