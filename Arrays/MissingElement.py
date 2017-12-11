

"""
Problem statement: 
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.

"""
def findMissingElement(originalArr,shuffeledArr):

    originalSum = originalArr[len(originalArr)-1]
    shuffeledSum = 0
    for i in range(len(originalArr)-1):

            originalSum = originalSum + originalArr[i]
            shuffeledSum = shuffeledSum + shuffeledArr[i]


    missingElement = originalSum - shuffeledSum
    print("missing number is: {}".format(missingElement))



findMissingElement([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])



