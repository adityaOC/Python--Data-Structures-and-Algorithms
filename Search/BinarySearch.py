

def binarySearch(arr,element):

    if len(arr) == 0:
        return False


    mid = len(arr)//2

    if arr[mid] == element:
        return True

    else:
        if element < arr[mid]:
            return  binarySearch(arr[:mid],element)
        else:
            return binarySearch(arr[mid+1:],element)


"""
result = binarySearch([1,2,3,4,5,6,7,8,9],7)

if result:
    print("found")
else:
    print("not found")

"""