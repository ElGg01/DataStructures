class HashTable:
    def __init__(self, max: int) -> None:
        self.MAX = max
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self, key: str):
        h = 0
        for char in key:
            h += ord(char)  # ord gives the number ASCII
        return h % self.MAX

    def __setitem__(self, key: str, value: int):
        h = self.getHash(key)

        found = False

        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key: str):
        h = self.getHash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key: str):
        h = self.getHash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


table = HashTable(100)

# INSERT ELEMENT
table["july 14"] = 130

print(table["july 14"])

# DELETE ELEMENT
del table["july 14"]

print(table["july 14"])
