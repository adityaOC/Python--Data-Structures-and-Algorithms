


def getNonRepChar(string,k):

    size= len(string)
    maxLen = 256

    count = [0] * maxLen
    indexes = [0] * maxLen

    for i in range(maxLen-1):

        count[i] = 0
        indexes[i] =size

    n = 0
    for c in string:

        count[ord(c)] +=1

        if count[ord(c)] == 1:
            indexes[ord(c)] = n

        if count[ord(c)] == 2:
            indexes[ord(c)] = size

        n +=1


    indexes.sort()

    print(" non rep char : {}".format(string[indexes[k]]))


string = 'geeksfozrgeeks'

getNonRepChar(string,4)
