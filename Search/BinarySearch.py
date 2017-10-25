

def BinarySearch(arr,element):

    if len(arr) == 0:
        return False


    mid = len(arr)//2

    if arr[mid] == element:
        return True

    else:
        if element < arr[mid]:
            return  BinarySearch(arr[:mid],element)
        else:
            return BinarySearch(arr[mid+1:],element)



result = BinarySearch([1,2,3,4,5,6,7,8,9],7)

if result:
    print("found")
else:
    print("not found")

