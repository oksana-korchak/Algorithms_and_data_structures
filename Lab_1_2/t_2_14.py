# 2.14. Доведіть співвідношення
# Зауваження. Для доведення співвідношення треба запропонувати алгоритм
# обчислення виразу зазначеного у лівій частині рівності, що має вказану у
# правій частині рівності асимптотичну оцінку часу виконання програми.
from math import factorial


# ----------------- a ---------------------

# sum{i=0}^{n} (i) = O(n)
def a(n):
    sum = 0                       # O(1)
    for i in range(1, n + 1):     # O(n)
        sum = sum + i             # O(n)
    return sum                    # O(1)

# ----------------- b ---------------------

# sum{i=0}^{n} (i*i) = O(n)
def b(n):
    s = 0                         # O(1)
    for i in range(1, n + 1):     # O(n)
        s += i * i                # O(n)
    return s                      # O(1)

# ------------------ c --------------------

# sum{i=0}^{n} (a^i) = O(n)
def c(n, a):
    s = 0                         # O(1)
    a_i = 1                       # O(1)
    for i in range(0, n + 1):     # O(n)
        s = s + a_i               # O(n)
        a_i *= a                  # O(n)
    return s                      # O(1)

# ------------------- d -------------------

# sum{i=0}^{n} (i^i) = O(n^2)
def d(n):
    s = 0
    for i in range(1, n + 1):     # O(n)
        a_i = 1                   # O(n)
        for j in range(i):        # O(n*n)
            a_i *= i              # O(n*n)
        s += a_i                  # O(n)
    return s                      # O(1)

# row 34-35:
# n = 2: i=1 -> j=0
#        i=2 -> j=01            1+2
# n = 3: i=1 -> j=0
#        i=2 -> j=01
#        i=3 -> j=012           1+2+3
# n   : 1 + 2 + ... + n = n^2/2 + n/2 = O(n^2)

# ------------------- e -------------------

# prod{i=1}^{n} (1/(1+i)) = O(n)
def e(n):
    res = 1                        # O(1)
    for i in range(1, n+1):        # O(n)
        res *= 1 / (1+i)           # O(n)
    return res                     # O(1)

# ------------------- f -------------------

# prod{i=1}^{n} (1/(1+i!)) = O(n)
def f(n):
    res = 1                        # O(1)
    factorial = 1                  # O(1)
    for i in range(1, n+1):        # O(n)
        factorial *= i             # O(n)
        res *= 1 / (1 + factorial) # O(n)
    return res                     # O(1)

# ------------------- g -------------------

# prod{i=1}^{n} (a^i/(1+i!)) = O(n)
def g(n, a):
    res = 1                        # O(1)
    fact = 1                       # O(1)
    a_p = 1                        # O(1)
    for i in range(1, n+1):        # O(n)
        a_p *= a                   # O(n)
        fact *= i                  # O(n)
        res *= a_p / (1 + fact)    # O(n)
    return res                     # O(1)

# ------------------- h -------------------

# prod{i=1}^{n} (1/(1+i^m)) = O(nm)
def h(n, m):
    res = 1                        # O(1)
    for i in range(1, n+1):        # O(n)
        val = 1                    # O(n)
        for j in range(m):         # O(n*m)
            val *= i               # O(n*m)
        res *= 1 / (1 + val)       # O(n)
    return res                     # O(1)

# ------------------- i -------------------

# prod{i=1}^{n} (1/(1+i^i)) = O(n^2)
def i(n):
    res = 1                        # O(1)
    for i in range(1, n+1):        # O(n)
        val = 1                    # O(n)
        for j in range(i):         # O(n*n) <- з пункту d)
            val *= i               # O(n*n)
        res *= 1 / (1 + val)       # O(n)
    return res                     # O(1)

# -----------------------------------------

