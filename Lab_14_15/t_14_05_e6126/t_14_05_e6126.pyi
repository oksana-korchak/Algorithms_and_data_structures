import sys

class Node:
    """ Допоміжний клас, що реалізує вузол черги """
    def __init__(self, item):
        self.item = item # поле для зберігання навантаження
        self.next = None # посилання на наступний вузол черги

class Queue:
    """ Клас, що реалізує чергу елементів
    як рекурсивну структуру """
    def __init__(self):
        self.front = None # Посилання на початок черги
        self.back = None  # Посилання на кінець черги
        # Додаємо лічильник для методу size
        self._size = 0

    def empty(self):
        return self.front is None and self.back is None

    def enqueue(self, item):
        """ Додає елемент у чергу (в кінець)"""
        new_node = Node(item)  # Створюємо новий вузол черги
        if self.empty():
            self.front = new_node  # новий вузол робимо початком черги
        else:
            self.back.next = new_node  # останній вузол черги
                                       # посилається на новий вузол
        self.back = new_node  # Останній вузол вказує на новий вузол
        self._size += 1
        return "ok"

    def dequeue(self):
        """ Прибирає перший елемент з черги
        :return: Навантаження голови черги (перший елемент черги)
        """
        if self.empty():
            return "error"
            # raise Exception("Queue: 'dequeue' applied to empty container")
        current_front = self.front  # запам'ятовуємо поточну голову черги
        item = current_front.item  # запам'ятовуємо навантаження першого вузла
        self.front = self.front.next  # замінюємо перший вузол наступним
        del current_front  # видаляємо запам'ятований вузол
        if self.front is None:  # Якщо голова черги стала порожньою
            self.back = None  # Черга порожня => хвіст черги теж порожній
        self._size -= 1
        return item

    def size(self):
        return self._size

    def clear(self):
        while not self.empty():
            self.dequeue()
        return "ok"

    def get_front(self):
        """ Повертає значення першого елемента без видалення """
        if self.empty():
            return "error"
        return self.front.item

if __name__ == "__main__":
    queue = Queue()

    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue

        command = parts[0]

        if command == "push":
            n = parts[1]
            print(queue.enqueue(n))

        elif command == "pop":
            print(queue.dequeue())

        elif command == "front":
            print(queue.get_front())

        elif command == "size":
            print(queue.size())

        elif command == "clear":
            print(queue.clear())

        elif command == "exit":
            print("bye")
            break