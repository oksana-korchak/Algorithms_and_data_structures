def qsort(array, a, b):
    if a >= b: return
    pivot = array[a + (b - a) // 2]
    left = a
    right = b
    while True:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1
        if left >= right:
            break
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    qsort(array, a, right)
    qsort(array, right + 1, b)


if __name__ == '__main__':
    n = int(input()) # кількість особових справ
    array = []
    for i in range(n):
        surname = input()
        name = input()
        class_ = input()
        birth = input()
        array.append([int(class_[:-1]), class_[-1], surname, name, birth])

    qsort(array, 0, n-1)
    for s in array:
        print(str(s[0])+s[1], *s[2:])