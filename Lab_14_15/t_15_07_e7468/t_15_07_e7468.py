import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.next: 'Node | None' = None

class LinkedList:
    def __init__(self):
        """ Конструктор ініціалізує порожній список. """
        self.head: Node | None = None
        self.curr: Node | None = None

    def empty(self) -> bool:
        """ Перевіряє чи список порожній. """
        return self.head is None

    def reset(self):
        """ Робить перший елемент списку поточним. """
        if self.empty():
            return
        self.curr = self.head

    def next(self):
        """ Перейти до наступного елемента. """
        if self.empty() or self.curr.next is None:
            raise StopIteration
        self.curr = self.curr.next

    def current(self):
        """ Повертає значення поточного елементу. """
        if self.empty():
            raise ValueError("Список порожній")
        return self.curr.item

    def insert_after(self, item):
        """ Вставляє новий елемент у список після поточного. """
        new_node = Node(item)

        if self.empty():
            self.head = self.curr = new_node
            return

        # Вставка після поточного (curr)
        new_node.next = self.curr.next
        self.curr.next = new_node

    # #################################################################
    def addToTail(self, val):
        """Додавання в кінець"""
        if self.empty():
            self.insert_after(val)
        else:
            while self.curr.next:
                self.next()
            self.insert_after(val)

    def ReorderList(self):
        if self.empty() or self.head.next is None:
            return

        # Знаходимо середину
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Реверс другої половини
        second_half = slow.next
        slow.next = None
        prev = None
        curr_rev = second_half
        while curr_rev:
            nxt = curr_rev.next
            curr_rev.next = prev
            prev = curr_rev
            curr_rev = nxt

        # Злиття через insert_after
        self.reset()
        head_second = prev
        while head_second:
            next_to_ins = head_second.next
            self.insert_after(head_second.item)

            self.next()
            if self.curr.next:
                self.next()
            head_second = next_to_ins

    def Print(self):
        if self.empty():
            return
        self.reset()
        while True:

            if self.curr.next:
                print(self.curr.item, end=" ")
            else:
                print(self.curr.item)

            try:
                self.next()
            except StopIteration:
                break

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        ll = LinkedList()

        for i in range(1, n + 1):
            ll.addToTail(int(data[i]))

        ll.ReorderList()
        ll.Print()
