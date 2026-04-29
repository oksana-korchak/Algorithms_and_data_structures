# На відрізку [0, 2] знайдіть корінь рівняння
# 𝑥³ + 4𝑥² + 𝑥 − 6 = 0.

# f = 𝑥³ + 4𝑥² + 𝑥 − 6
# a = 0, b = 2, c = 0
# RESULT: x = 1.000000

import sympy as sp

def check_monotonicity(func, a, b):
    x = sp.Symbol('x')
    f = func(x)

    interval = sp.Interval(a, b)

    if sp.is_increasing(f, interval):  # Зростання
        return "increasing"
    elif sp.is_decreasing(f, interval):  # Спадання
        return "decreasing"
    else:
        return False


def binary_continuous(f, c, a, b, condition):
    l = a  # лівий кінець відрізка
    r = b  # правий кінець відрізка

    m = (l + r) / 2.0  # середина відрізка [l,r]
    while l != m and m != r:

        # Зростання
        if condition == "increasing":
            if f(m) < c:
                l = m  # [l,r] = [x,r]
            else:
                r = m  # [l,r] = [l,x]

        # Спадання
        if condition == "decreasing":
            if f(m) > c:
                l = m  # [l,r] = [x,r]
            else:
                r = m  # [l,r] = [l,x]

        m = (l + r) / 2.0  # середина відрізка [l,r]

    return l


if __name__ == '__main__':

    # A = float(input())
    # B = float(input())
    # C = float(input())

    A = 0.
    B = 2.
    C = 0.

    def F(x):
        return x**3 + 4 * x**2 + x - 6

    condition = check_monotonicity(F, A, B)
    if condition:
        res = binary_continuous(F, C, A, B, condition)
        print(f"{res:.6f}")
    else:
        print("Функція не є монотонною на відрізку, тому розв'язок через бінарний пошук неможливий")

    # RESULT: x = 1.000000

