def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right :
        m = (left + right) // 2

        if array[m] < x:
            left = m + 1
        elif array[m] > x:
            right = m - 1
        else:
            return m
    return None

if __name__ == '__main__':
    n = int(input())
    lst = [int(x) for x in input().split()]
    m = int(input())
    q = [int(x) for x in input().split()]

    for x in q:
        res = binary_search(lst, x)
        if res is not None:
            print("YES")
        else:
            print("NO")

