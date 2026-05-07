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


if __name__ == "__main__":
    input_data = sys.stdin.read().split()

    # Кількість карт в колоді
    n = int(input_data[0])
    half_n = n // 2

    q1 = Queue()
    q2 = Queue()

    # Заповнюємо колоди гравців
    for i in range(1, half_n + 1):
        q1.enqueue(int(input_data[i]))

    for i in range(half_n + 1, n + 1):
        q2.enqueue(int(input_data[i]))

    moves = 0
    max_moves = 200000

    while not q1.empty() and not q2.empty() and moves < max_moves:
        moves += 1

        # Гравці відкривають по одній верхній карті
        card1 = q1.dequeue()
        card2 = q2.dequeue()

        # 0 (наймолодша) б'є n-1 (найстаршу)
        if card1 == 0 and card2 == n - 1:
            winner = 1
        elif card2 == 0 and card1 == n - 1:
            winner = 2
        # Більша карта перемагає
        elif card1 > card2:
            winner = 1
        else:
            winner = 2

        # Переможець кладе карти під низ своєї колоди
        # Спочатку карту 1-го гравця
        if winner == 1:
            q1.enqueue(card1)
            q1.enqueue(card2)
        else:
            q2.enqueue(card1)
            q2.enqueue(card2)

    if moves >= max_moves:
        print("draw")
    elif q1.empty():
        print(f"second {moves}")
    else:
        print(f"first {moves}")
