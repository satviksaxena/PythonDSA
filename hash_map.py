class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    # This __getitem__ is one of the way to call these values as a list ans not use def get and set function
    def __getitem__(self,key):
        h = self.get_hash(key)
        # return self.arr[h]
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        # self.arr[h] = val
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]= (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

