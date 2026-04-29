def find_first(array, x):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def find_last(array, x):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == '__main__':
    n = int(input())
    lst = [int(x) for x in input().split()]
    m = int(input())
    q = [int(x) for x in input().split()]

    for x in q:
        first = find_first(lst, x)
        last = find_last(lst, x)
        print(last - first)