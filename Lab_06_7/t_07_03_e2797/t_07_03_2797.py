EMPTY = "EMPTY"

class HashTable:
    def __init__(self, size=11):
        self.size: int = size
        self.keys: list = [EMPTY for _ in range(size)]
        self.count: int = 0

    def hash(self, key: int):
        return key % self.size

    def set(self, key: int):
        i = self.hash(key)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == key:
                return

            i = (i + 1) % self.size
        self.keys[i] = key
        self.count += 1

if __name__ == '__main__':
    n = int(input())
    tel_nums = [int(x) for x in input().split()]

    hash_table = HashTable(200003)

    for num in tel_nums:
        hash_table.set(num)

    print(hash_table.count)