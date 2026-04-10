import sys
sys.set_int_max_str_digits(0)

def mult(a, b):
    """
    Множення в стопчик(перебір всіх пар чисел)
    """
    n, m = len(a), len(b)
    res = [0] * (n + m)

    num1 = [int(d) for d in a[::-1]]
    num2 = [int(d) for d in b[::-1]]

    for i in range(n):
        for j in range(m):
            res[i + j] += num1[i] * num2[j]
            res[i + j + 1] += res[i + j] // 10
            res[i + j] %= 10

    answ = int("".join(map(str, res[::-1])))
    return answ

def karatsuba(a, b):
    n = max(len(str(a)), len(str(b)))

    if n <= 64:
        return mult(str(a), str(b))

    m = n // 2
    p = 10**m

    # a_high = a // 10^m, a_low = a % 10^m
    a_high, a_low = divmod(a, p)
    b_high, b_low = divmod(b, p)

    x1 = karatsuba(a_high, b_high)
    x2 = karatsuba(a_low, b_low)
    x3 = karatsuba(a_high + a_low, b_high + b_low)

    return (x1 * 10 ** (2 * m)) + ((x3 - x1 - x2) * p) + x2

if __name__ == '__main__':

    input_data = sys.stdin.read().split()
    A, B = input_data[0], input_data[1]

    print(karatsuba(int(A), int(B))) # дає 30%
    #print(mult(A, B)) # дає 20%
