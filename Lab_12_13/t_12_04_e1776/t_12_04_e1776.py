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

    def back(self):
        if self.empty():
            raise Exception("Stack: 'back' applied to empty container")
        return self.items[-1]


if __name__ == "__main__":
    while True:
        try:
            line = input().split()
            if not line:
                continue

            n = int(line[0])
            if n == 0:
                break

            while True:
                line = input().split()
                if line[0] == "0":
                    print()
                    break

                target = [int(x) for x in line]

                # СТАНЦІЯ
                station = Stack()
                current_wagon = 1  # Вагони в напрямку А: 1, 2, 3...
                possible = True

                for wagon in target:
                    # Поки потрібного вагона немає на станції — завозимо нові з А
                    while (station.empty() or station.back() != wagon) and current_wagon <= n:
                        station.push(current_wagon)
                        current_wagon += 1

                    # Якщо зверху на станції потрібний вагон — вивозимо його в Б
                    if station.back() == wagon:
                        station.pop()
                    else:
                        # Якщо потрібного вагона немає і взяти ніде
                        possible = False
                        break

                if possible:
                    print("Yes")
                else:
                    print("No")

        except EOFError:
            break
