
class HashTable():

    def __init__(self,size):
        self.size = size
        self.slots =[None]*self.size
        self.data = [None]*self.size

    def put(self,key,data):

        hashValue = self.hashFunction(key)
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:

            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                #collision case, look for next slot
                rehash = self.reHashFunction(key)
                startPosition = rehash
                while self.slots[rehash]!=None and  self.slots[rehash] != key:


                    if self.slots[rehash]==None:
                        self.slots[rehash] = key
                        self.data[rehash] = data
                    else:
                        self.data[rehash] = data
                    rehash = self.reHashFunction(key)
                    if rehash == rehash:
                        return None



        self.displayAllKeys()

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hashFunction(self,key):
        return key%self.size

    def reHashFunction(self,key):
        return  (key+1)%self.size

    def displayAllKeys(self):
        print(self.slots)

    def get(self,key):

        hashValue = self.hashFunction(key)

        if self.slots[hashValue] == key:
            return self.data[hashValue]

        else:
            found = False
            stop  = False
            rehash = self.reHashFunction(key)
            starPosition = rehash

            while self.slots[rehash]!=None and found !=True and stop!=True:

                if self.slots[rehash] == key:
                    return self.data[rehash]
                else:
                    rehash = self.reHashFunction(key)
                    if rehash == starPosition:
                        return None



hash = HashTable(6)
hash.put(1,"one")
hash.put(0,"ZERO")
hash.put(2,"two")
hash.put(3,"three")
hash.put(4,"four")
hash.put(5,"five")
hash.put(6,"six")

print(hash.get(10))
print(hash.get(3))

