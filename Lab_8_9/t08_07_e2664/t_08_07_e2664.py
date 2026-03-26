def insertion_sort(array):
    n = len(array)
    for index in range(1, n):
        currentValue = array[index]
        position = index
        was_moved = False
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
                was_moved = True
            else:
                break
            position -= 1
        array[position] = currentValue
        if was_moved:
            print(*array)

if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]

    is_sorted = True
    for i in range(n-1):
        if array[i] > array[i+1]:
            is_sorted = False
            break

    if not is_sorted:
        insertion_sort(array)
