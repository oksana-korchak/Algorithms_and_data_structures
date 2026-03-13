EMPTY = "EMPTY"
DELETED = "DELETED"
N = 31 # Просте число, що не перевищує 255
M = 101 # Кількість всіх можливих хешів

class HashTable:
    def __init__(self, size=11):
        self.size: int = size
        self.keys: list = [EMPTY for _ in range(size)]
        self.values: list = [EMPTY for _ in range(size)]
        self.count: int = 0

    def hash(self, key: str):
        h = 0
        for c in key:
            h = (h * N + ord(c)) % self.size
        return h

    def set(self, key: str):
        i = self.hash(key)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == key:
                return

            i = (i + 1) % self.size

        self.keys[i] = key
        self.values[i] = False
        self.count += 1

    def use(self, key: str):
        i = self.hash(key)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == key:
                self.values[i] = True
                return True
            i = (i + 1) % self.size
        return False

    def check_all_words(self):
        used_count = 0
        for i in range(self.size):
            if self.keys[i] != EMPTY and self.values[i] is True:
                    used_count += 1
        return used_count == self.count


def get_words(text):
    words_list = []
    current_word = ""
    for char in text.lower():
        if 'a' <= char <= 'z' or char == "′":
            current_word += char
        else:
            if current_word:
                words_list.append(current_word)
                current_word = ""
    if current_word:
        words_list.append(current_word)

    return words_list

if __name__ == '__main__':
    hash_table = HashTable(3001)
    n, m = [int(x) for x in input().split()]

    # Додавання слів у словник
    for i in range(n):
        word = input().strip().lower()
        hash_table.set(word)

    # Читання і перевірка тексту
    OK = True
    for j in range(m):
        line = input()
        words = get_words(line)
        for word in words:
            # Слова нема в словнику
            if not hash_table.use(word):
                OK = False

    if not OK:
        print("Some words from the text are unknown.")
    elif not hash_table.check_all_words():
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")


