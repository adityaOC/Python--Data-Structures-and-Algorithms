

def sortInWaveForm(arr):


    right = len(arr)-1

    for i in range(0,len(arr),2):

            if i>0 and arr[i]<arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]


            if i<right and arr[i]<arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

    print(arr)




#90 10 49 1 5 2 23
arr = [10, 90, 49, 2, 1, 5, 23]
sortinWaveForm(arr)




