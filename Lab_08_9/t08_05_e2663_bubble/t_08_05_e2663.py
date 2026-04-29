def bubble_sort(array):
    k = 0
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                k += 1
                array[i], array[i + 1] = array[i + 1], array[i]
    return k

if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]
    k = bubble_sort(array)
    print(k)
