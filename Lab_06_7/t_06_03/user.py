
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

EMPTY = "EMPTY"
DELETED = "DELETED"
N = 31 # Просте число, що не перевищує 255
M = 100007 # Кількість всіх можливих хешів
#M = 101

def is_prime(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class BookHashTable:
    def __init__(self, size=M):
        self.size: int = size
        self.keys: list = [EMPTY for _ in range(size)]
        self.values: list = [EMPTY for _ in range(size)]
        self.count: int = 0

    def hash(self, key: str):
        h = 0
        for c in key:
            h = (h * N + ord(c)) % self.size
        return h

    def rehash(self):
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2

        _keys = self.keys
        _values = self.values
        self.__init__(self.size)

        for i in range(len(_keys)):
            if _keys[i] not in (EMPTY, DELETED):
                self.set(_keys[i], _values[i])

    def set(self, key: str, value: str) -> None:
        if self.count > 0.7 * self.size:
            self.rehash()

        i = self.hash(key)
        j = -1
        while self.keys[i] not in (EMPTY, DELETED):
            if self.keys[i] == key:
                self.values[i] = value
                return

            if j == -1 and self.keys[i] is DELETED:
                j = i

            i = (i + 1) % self.size

        if j == -1:
            j = i
            self.count += 1

        self.keys[j] = key
        self.values[j] = value

    def get(self, key: str) -> str | None:
        i = self.hash(key)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == key:
                return self.values[i]
            i = (i + 1) % self.size
        return None

    def delete(self, key: str) -> None:
        i = self.hash(key)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == key:
                self.keys[i] = DELETED
                self.values[i] = DELETED
                return
            i = (i + 1) % self.size

    def findByAuthor(self, author):
        books = []
        for i in range(self.size):
            key = self.keys[i]
            if key not in (EMPTY, DELETED):
                if self.values[i] == author:
                    title = self.keys[i][len(author) + 1:]
                    #title = key.split("|", 1)[1]
                    books.append(title)
        books.sort()
        return books


hash_table = BookHashTable()

def init():
    """ Викликається 1 раз на початку виконання програми. """
    pass


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    key = author + "|" + title
    hash_table.set(key=key, value=author)


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    key = author + "|" + title
    val = hash_table.get(key)
    return val == author


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    key = author + "|" + title
    hash_table.delete(key=key)


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    return hash_table.findByAuthor(author)

