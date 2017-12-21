

def sortDictionarybyValues(dict):

    newKey = dict.keys()
    keys = []

    for k in newKey:
        keys.append(k)


    for outer in range(len(keys)-1):
        minPos = outer
        #print(keys[outer])
        #break

        for inner  in range(outer + 1,len(keys)):

            if dict[keys[inner]] > dict[keys[minPos]]:
                minPos = inner

        temp = keys[outer]
        keys[outer] = keys[minPos]
        keys[minPos] = temp


    result = []
    for k in keys:
        n = dict[k]

        for i in range(n):
            result.append(k)
    print(result)









dict = {2:3,3:4,12:2,4:1}

sortDictionarybyValues(dict)


