
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


    """
    for key in hashValues:

        if hashValues[key] > maxCount:
            maxCount = hashValues[key]
            maxChar = key

    """
    print("maxChar = {}, maxCount = {}".format(maxChar,maxCount))


string = 'Max occurring character'

getMaxOccuringChar(string)


