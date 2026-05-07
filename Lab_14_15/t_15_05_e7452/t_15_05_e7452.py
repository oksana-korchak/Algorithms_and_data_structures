import sys

class Node:
    """Вузол двозв'язного списку."""
    def __init__(self, data):
        self.data = data
        self.next = None  # наступний елемент
        self.prev = None  # попередній елемент

    def __repr__(self):
        return f"Node({self.data})"


class DoublyLinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.current = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.first is None

    def move_to_first(self):
        if self.is_empty():
            raise IndexError("Список порожній")
        self.current = self.first

    def move_to_last(self):
        if self.is_empty():
            raise IndexError("Список порожній")
        self.current = self.last

    def move_to_next(self):
        if self.current is None:
            raise RuntimeError("Поточний елемент не визначений")
        if self.current.next is None:
            raise StopIteration("next = None")
        self.current = self.current.next

    def move_to_prev(self):
        if self.current is None:
            raise RuntimeError("Поточний елемент не визначений")
        if self.current.prev is None:
            raise StopIteration("prev = None")
        self.current = self.current.prev

    def get_current(self):
        if self.current is None:
            raise RuntimeError("Поточний елемент не визначений")
        return self.current.data

    def insert_before_current(self, data):
        """Вставити новий елемент перед поточним"""
        new_node = Node(data)

        if self.is_empty():
            # Список порожній — новий вузол стає єдиним
            self.first = self.last = self.current = new_node

        elif self.current is None:
            raise RuntimeError("Поточний елемент не визначений")

        else:
            prev_node = self.current.prev  # може бути None (current == head)

            # Зв'язуємо new_node - current
            new_node.next = self.current
            self.current.prev = new_node

            # Зв'язуємо prev_node - new_node
            new_node.prev = prev_node
            if prev_node:
                prev_node.next = new_node
            else:
                self.first = new_node

        self.size += 1

    def insert_after_current(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.first = self.last = self.current = new_node

        elif self.current is None:
            raise RuntimeError("Поточний елемент не визначений")
        else:
            next_node = self.current.next

            # Зв'язуємо current - new_node
            self.current.next = new_node
            new_node.prev = self.current

            # Зв'язуємо new_node - next_node
            new_node.next = next_node
            if next_node:
                next_node.prev = new_node
            else:
                # current був хвостом — оновлюємо first
                self.last = new_node

        self.size += 1

    def delete_current(self):
        if self.current is None:
            raise RuntimeError("Поточний елемент не визначений")

        removed_data = self.current.data
        prev_node = self.current.prev
        next_node = self.current.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.first = next_node  # видаляємо перший

        if next_node:
            next_node.prev = prev_node
        else:
            self.first = prev_node  # видаляємо останній

        # Після видалення поточним стає наступний (або попередній, якщо next = None)
        self.current = next_node if next_node else prev_node

        self.size -= 1
        return removed_data

# ###################################################################

    def Print(self) -> None:
        """Вивести елементи Зв'язного Списку"""
        if self.is_empty():
            return
        self.move_to_first()  # Ставимо курсор на початок
        while True:
            # Використовуємо твій метод get_current
            data = self.get_current()

            # Перевіряємо, чи є куди йти далі (щоб красиво розставити пробіли)
            if self.current.next:
                print(data, end=" ")
                self.move_to_next()
            else:
                print(data)  # Останній елемент
                break
        """el = self.first
        while el:
            if el.next:
                print(el.data, end=" ")
            else:
                print(el.data)
            el = el.next"""

    def PrintReverse(self) -> None:
        """Вивести елементи Зв'язного Списку в зворотному порядку"""
        if self.is_empty():
            return

        self.move_to_last()  # Ставимо курсор у кінець
        while True:
            data = self.get_current()  # Отримуємо дані через твій метод

            if self.current.prev:
                print(data, end=" ")
                self.move_to_prev()
            else:
                print(data)
                break
        """el = self.last
        while el:
            if el.prev:
                print(el.data, end=" ")
            else:
                print(el.data)
            el = el.prev"""

if __name__ == "__main__":
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    dll = DoublyLinkedList()

    # Створення зв'язного списку
    for i in range(1, n + 1):
        value = int(input_data[i])
        if dll.is_empty():
            dll.insert_after_current(value)
        else:
            # Для послідовного додавання в кінець переміщуємося до останнього
            dll.move_to_last()
            dll.insert_after_current(value)

    dll.Print()
    dll.PrintReverse()
