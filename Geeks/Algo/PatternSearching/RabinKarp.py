
import  math

str = "abcd"




def rabinKarp(string, pattern,primeNumber):

    patternHash = hashV(pattern,primeNumber)
    print(patternHash)

    curruntHash = hashV("a",primeNumber)
    if patternHash == curruntHash:
        return True

    upto = len(string) - (len(pattern)-1)

    for i in range(1,upto):

        curruntHash = hashRoll(string,i,pattern,curruntHash,primeNumber)

        if curruntHash == patternHash:
            return True

    return False



def hashV(string,primeNumber):

    hashV = 0
    for i in range(len(string)):
        hashV += ord(string[i]) * math.pow(primeNumber, i)

    return hashV

def hashRoll(string, index,pattern,currentHash,primeNumber):

    hashV = currentHash - ord(string[index-1])
    hashV = hashV/primeNumber

    hashV = hashV + ord(string[index + (len(pattern)-1)]) * pow(primeNumber,len(pattern)-1)

    return hashV



print(rabinKarp("abcd","b",3))





