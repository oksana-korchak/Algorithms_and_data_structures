class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
        self._size = 0

    def empty(self):
        return self.top_node is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"

        current_top = self.top_node
        item = current_top.item
        self.top_node = self.top_node.next
        self._size -= 1
        del current_top
        return item

    def back(self):
        if self.empty():
            return "error"
        return self.top_node.item

    def size(self):
        return self._size

    def clear(self):
        self.top_node = None
        self._size = 0
        return "ok"


if __name__ == "__main__":
    stack = Stack()

    while True:
        try:
            line = input().strip()
            if not line:
                continue

            parts = line.split()
            command = parts[0]

            if command == "push":
                print(stack.push(parts[1]))

            elif command == "pop":
                print(stack.pop())

            elif command == "back":
                print(stack.back())

            elif command == "size":
                print(stack.size())

            elif command == "clear":
                print(stack.clear())

            elif command == "exit":
                print("bye")
                break

        except EOFError:
            break


