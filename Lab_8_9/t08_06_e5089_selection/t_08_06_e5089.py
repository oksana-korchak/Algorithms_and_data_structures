def selection_sort(array):
    lst = array.copy()
    n = len(array)
    for i in range(n - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if lst[maxpos] < lst[j]:
                maxpos = j
        lst[i], lst[maxpos] = lst[maxpos], lst[i]
    return lst

if __name__ == '__main__':
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())

    lst = selection_sort(words)

    for word in lst:
        print(word)

