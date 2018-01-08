"""

note this solution only determines if there is overlap preset or not

and does not tell which pairs overlap

https://www.geeksforgeeks.org/check-if-any-two-intervals-overlap-among-a-given-set-of-intervals/

"""

def bubbleSortTupl(arr):

    for outer in range(len(arr)-1):
        for inner in range (len(arr)-1):
            a,b = arr[inner]
            c,d = arr[inner+1]

            if a> c:
                temp = arr[inner]
                arr[inner] = arr[inner + 1]
                arr[inner + 1] = temp




arr = [(1,3), (5,7), (2,4), (6,8)]
#arr2 = [(1,3), (7,9), (4,6), (10,13)]
arr = [(6,8),(1,3),(2,4),(4,7)]
bubbleSortTupl(arr)

for a,b in arr:
    print(a,b)
print("________________________")

overlap = False
for i in range(1,len(arr)):
    startOfFirst, endOfFirst=  arr[i-1]
    startOfSecond, endOfSecond = arr[i]

    if endOfFirst>startOfSecond:
        overlap =True

    i+=1

if overlap:
    print("Overlap present")
else:
    print("overlap not present")





