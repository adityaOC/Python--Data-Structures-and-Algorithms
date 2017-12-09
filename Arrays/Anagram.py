

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



anagramWithSorting("public relations","crap built on lies")