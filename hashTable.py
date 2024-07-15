class HashTable:
    def __init__(self, max: int) -> None:
        self.MAX = max
        self.arr = [None for i in range(self.MAX)]

    def getHash(self, key: str):
        h = 0
        for char in key:
            h += ord(char)  # ord gives the number ASCII
        return h % self.MAX

    def __setitem__(self, key: str, value: int):
        h = self.getHash(key)
        self.arr[h] = value

    def __getitem__(self, key: str):
        h = self.getHash(key)
        return self.arr[h]

    def __delitem__(self, key: str):
        h = self.getHash(key)
        self.arr[h] = None


table = HashTable(100)

# INSERT ELEMENT
table["july 14"] = 130

print(table["july 14"])

# DELETE ELEMENT
del table["july 14"]

print(table["july 14"])
