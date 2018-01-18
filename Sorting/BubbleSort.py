

def bubbleSort(arr):

    for outer in range(len(arr)-1,0,-1):
        for inner in range (outer):

            if arr[inner]> arr[inner + 1]:
                temp = arr[inner]
                arr[inner] = arr[inner + 1]
                arr[inner + 1] = temp

    print(arr)



list = [5,4,3,2,1,10,23,50,33]

bubbleSort(list)


def sortStringForString(str):

    for outer in range(len(str)-1,0,-1):
        for inner in range(outer):
            temp1 =ord(str[inner])
            temp2 = ord(str[inner+1])

            if ord(str[inner])> ord(str[inner+1]):
                temp = str[inner]
                str[inner] = str[inner + 1]
                str[inner + 1] = temp


    print(str)



str = ['d','c','b','a']


sortStringForString(str)




















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
