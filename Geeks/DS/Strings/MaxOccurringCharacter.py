
def getMaxOccuringChar(string):
    maxCount = 0
    maxChar = ''
    hashValues = {}
    for c in string:

        if c in hashValues:
            hashValues[c] += 1
        else:
            hashValues[c] = 1

        if hashValues[c] > maxCount:
            maxCount = hashValues[c]
            maxChar = c



    print("maxChar = {}, maxCount = {}".format(maxChar,maxCount))

def getSecondMostFreqChar(string):
    maxCount = 0
    secdondMaxCount = 0
    maxChar = ''
    secondMaxChar = ''
    hashValues = {}

    for c in string:
        if  c in hashValues:
            hashValues[c]+=1
        else:
            hashValues[c] = 1

        if hashValues[c] > maxCount:
            maxCount = hashValues[c]
            maxChar = c
        elif hashValues[c]> secdondMaxCount and  hashValues[c] != maxCount:
            secdondMaxCount = hashValues[c]
            secondMaxChar = c

    if secdondMaxCount == 0:
        print("No sec most freq char")
    else:
        print("second max char is  {} count = {}".format(secondMaxChar,secdondMaxCount))





string = 'aabababa'

getMaxOccuringChar(string)

getSecondMostFreqChar(string)



