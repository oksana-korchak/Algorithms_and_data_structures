def sequences(lst, n, k):
    if len(lst) == k:
        print(*lst)
        return

    for i in range(1, n+1):
        if i not in lst:
            lst_next = lst[:]
            lst_next.append(i)
            sequences(lst_next, n, k)

if __name__ == '__main__':
    n, k = [int(x) for x in input().split()]
    lst = []
    sequences(lst, n, k)

