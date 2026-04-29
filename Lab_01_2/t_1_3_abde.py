# 1.3. Визначте час виконання фрагментів програм заданих нижче

# a)
def a(n, k):
    k += 1         # 4
    i = n          # 2
    while i > 0:   # 3 * (n + 1)
        i -= 1     # 4 * n

# n = 0 : loop block: 0, while condition: 1
# n = 1 : loop block: 1, while condition: 2
# n     : loop block: n, while condition: n + 1

# sum: 7n + 9

# b)
def b(n, k):
    i = n              # 2
    while i > 1:       # 3 * (m + 1)
        k += 1         # 4 * m
        i //= 2        # 4 * m

# n = 2^m => m = log2(n)

# m = 0, n = 1 : loop block: 0, while condition: 1
# m = 1, n = 2 : loop block: 1, while condition: 2
# m = 2, n = 4 : loop block: 2, while condition: 3
# m   ,  n     : loop block: m, while condition: m+1

# sum: 11m + 5 = 11log2(n) + 5

# d)
def d(n, k):

    i = 0                 # 2
    while i < n:          # 3 * (n+1)
        j = 0             # 2 * n
        while j < i * i:  # 4 * [(0+1) + (1+1) + ... + ((n-1)**2+1)]
            k += 1        # 4 * [0 + 1 + 2**2 + ... + (n-1)**2]
            j += 1        # 4 * [0 + 1 + 2**2 + ... + (n-1)**2]
        i += 1            # 4 * n


# n = 0 : loop block_i: 0, while condition_i: 1
#         loop block_j: 0, while condition_j: 0

# n = 1 : loop block_i: 1, while condition_i: 2
# i = 0 : loop block_j: 0, while condition_j: 1
#                       0                     1

# n = 2 : loop block_i: 2, while condition_i: 3
# i = 0 : loop block_j: 0, while condition_j: 1
# i = 1 : loop block_j: 1, while condition_j: 2
#                       1                     3

# n = 3 : loop block_i: 3, while condition_i: 4
# i = 0 : loop block_j: 0, while condition_j: 1
# i = 1 : loop block_j: 1, while condition_j: 2
# i = 2 : loop block_j: 4, while condition_j: 5
#                       5                     8

# n     : loop block_i: n, while condition_i: n+1,
#         loop block_j:      0 + 1 + 2**2 + ... + (n-1)**2,
#         while condition_j: (0+1) + (1+1) + ... + ((n-1)**2+1),

# sum: 2 + 3n+3 + 2n + 4[(0+1) + (1+1) + ... + ((n-1)**2+1)] + 2*4*[0 + 1 + 2**2 + ... + (n-1)**2] + 4n
# sum: 9n + 5 + 4*n + 12*(n-1)(n-1+1)(2n-2+1)/6 = 13n + 5 + 2*(n-1)n(2n-1)
# sum: 4n**3 - 6n**2 + 15n + 5



# e)
def e(n, k):
    i = 1                 # 2
    while i < n:          # 3 * (m+1)
        j = 1             # 2 * m
        while j < n:      # 3 * m * (m+1)
            k += 1        # 4 * m * m
            j *= 2        # 4 * m * m
        i *= 2            # 4 * m

# n = 2^m => m = log2(n)

# m = 0, n = 1: loop block_i: 0, while condition_i: 1
#               loop block_j: 0, while condition_j: 0
# m = 1, n = 2: loop block_i: 1, while condition_i: 2
#               loop block_j: 1, while condition_j: 2 (* 1)
# m,     n    : loop block_i: m, while condition_i: m+1
#               loop block_j: m*m, while condition_j: m*(m+1)

# sum: 11m**2 + 12m + 5 = 11(log2(n))**2 + 12log2n + 5
