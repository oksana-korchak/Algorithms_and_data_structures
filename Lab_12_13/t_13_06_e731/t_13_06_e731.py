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

def priority(op):
    if op in '+-':
        return 1
    if op in '*/':
        return 2
    return 3  # для операндів(літер)

if __name__ == "__main__":
    prefix = input().strip()
    stack = Stack()

    for char in reversed(prefix):
        if char not in "+-*/":
            # Літера
            stack.push((char, 3))
        else:
            # Якщо це оператор, дістаємо два операнди
            op1_val, op1_pr = stack.pop()
            op2_val, op2_pr = stack.pop()

            curr_pr = priority(char)

            # Дужки для лівого операнда
            left = op1_val
            if op1_pr < curr_pr:
                left = f"({op1_val})"

            # Дужки для правого операнда
            right = op2_val
            # Якщо пріоритет нижчий, то дужки потрібні
            if op2_pr < curr_pr or (op2_pr == curr_pr and char in ('-', '/')):
                right = f"({op2_val})"

            # '+' та '*', де порядок не має значення
            new_expr = f"{left}{char}{right}"
            stack.push((new_expr, curr_pr))

    print(stack.pop()[0])