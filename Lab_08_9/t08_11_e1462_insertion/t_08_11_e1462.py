def insertion_sort(array):
    n = len(array)
    for index in range(1, n):
        currentValue = array[index]
        position = index
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue

if __name__ == '__main__':
    n = int(input())
    array = []

    for i in range(n):
        num = input()
        last_num = int(num[-1])
        num = int(num)
        array.append([last_num, num])

    insertion_sort(array)
    print(*[el[1] for el in array])

