def selection_sort(array):
    n = len(array)

    first_el = array[0]
    moves = 0

    for i in range(n - 1):
        minpos = i
        for j in range(i+1, n):
            if array[j] < array[minpos]:
                minpos = j

        if i != minpos:
            if array[i] == first_el or array[minpos] == first_el:
                moves += 1

            array[i], array[minpos] = array[minpos], array[i]

    return moves


if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]
    print(selection_sort(array))