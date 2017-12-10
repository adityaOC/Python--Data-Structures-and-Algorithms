

def anagramWithSorting(list1, list2):



    list1 = sorted(list1.strip(" ").replace(" ",""))
    list2 = sorted(list2.strip(" ").replace(" ",""))

    if not len(list1) == len(list2):
        print("Not anagram")

        return

    if list1 == list2:
        print("anagram")
    else:
        print("Not anagram")

def anagramCheckWithHashTable(list1,list2):

    list1 = list1.replace(" ","")
    list2 = list2.replace(" ", "")

    dict = {}

    for c in list1:

        if c in dict:
            dict[c] = dict[c] + 1
        else:
            dict[c] = 1

    for c in list2:

        if c in dict:
            dict[c] = dict[c] - 1
        else:
            dict[c] = 1

    status = True
    for key in dict:

        if dict[key] != 0:
            status = False

    if status:
        print("Anagram")
    else:
        print("Not anagram")


anagramCheckWithHashTable("public  relations","crap built on lies")

#anagramWithSorting("public relations","crap built on lies")