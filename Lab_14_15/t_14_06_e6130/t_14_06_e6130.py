import sys

class Node:
    """ Допоміжний клас - вузол деку """
    def __init__(self, item):
        self.item = item # поле, що містить елемент деку
        self.next = None # наступний вузол
        self.prev = None # попередній вузол

class Deque:
    """ Реалізує дек як рекурсивну структуру. """
    def __init__(self):
        self.front = None # Посилання на перший елемент деку
        self.back = None  # Посилання на останній елемент деку
        self._size = 0

    def empty(self):
        return self.front is None and self.back is None

    def appendleft(self, item):
        """ Додає елемент до початку деку"""

        node = Node(item)       # створюємо новий вузол деку
        node.next = self.front  # наступний вузол нового - елемент, що є першим
        if not self.empty():        # якщо додаємо до непорожнього деку
            self.front.prev = node  # новий вузол стає попереднім для першого
        else:
            self.back = node  # якщо додаємо дані до порожнього деку,
                              # новий вузол є останнім
        self.front = node  # новий вузол стає першим у деку
        self._size += 1
        return "ok"

    def appendright(self, item):
        """ Додає елемент у кінець деку """
        node = Node(item)
        node.prev = self.back
        if not self.empty():
            self.back.next = node
        else:
            self.front = node
        self.back = node
        self._size += 1
        return "ok"

    def popleft(self):
        """ Вилучає елемент з початку деку."""

        if self.empty():
            return "error"
            # raise Exception('popleft: Дек порожній')
        node = self.front       # node - перший вузол деку
        item = node.item        # запам'ятовуємо навантаження
        self.front = node.next  # першим стає наступний вузлом деку
        if self.front is None:  # якщо в деку був 1 елемент
            self.back = None    # дек стає порожнім
        else:
            self.front.prev = None  # інакше перший елемент посилається на None
        del node                    # Видаляємо вузол
        self._size -= 1
        return item

    def pop_right(self):
        """ Вилучає елемент з кінця деку """
        if self.empty():
            return "error"

        node = self.back
        item = node.item
        self.back = node.prev

        if self.back is None:
            self.front = None
        else:
            self.back.next = None

        del node
        self._size -= 1
        return item

    def get_front(self):
        if self.empty():
            return "error"
        return self.front.item

    def get_back(self):
        if self.empty():
            return "error"
        return self.back.item

    def size(self):
        return self._size

    def clear(self):
        """ Очищує дек, видаляючи по черзі """
        while not self.empty():
            self.popleft()
        return "ok"

if __name__ == "__main__":
    dq = Deque()

    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue

        command = parts[0]

        if command == "push_front":
            print(dq.appendleft(parts[1]))
        elif command == "push_back":
            print(dq.appendright(parts[1]))
        elif command == "pop_front":
            print(dq.popleft())
        elif command == "pop_back":
            print(dq.pop_right())
        elif command == "front":
            print(dq.get_front())
        elif command == "back":
            print(dq.get_back())
        elif command == "size":
            print(dq.size())
        elif command == "clear":
            print(dq.clear())
        elif command == "exit":
            print("bye")
            break