

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




print("_____________________")

INSIDE = 0  #0000
LEFT = 1    #0001
RIGHT = 2   #0010
BOTTOM = 4  #0100
TOP = 8     #1000


code = INSIDE

code |= LEFT

res = 8 & 3
print(code)
