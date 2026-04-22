class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            raise Exception("Stack: 'pop' applied to empty container")
        return self.items.pop()


if __name__ == "__main__":
    s = input().strip()
    stack = Stack()
    is_correct = True

    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.push(char)

        elif char in ")]}":
            if stack.empty():
                is_correct = False
                break

            last_opened = stack.pop()

            if last_opened != pairs[char]:
                is_correct = False
                break

    if is_correct and stack.empty():
        print("yes")
    else:
        print("no")