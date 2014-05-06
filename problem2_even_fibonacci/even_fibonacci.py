__author__ = 'Xidai'


def sum_of_even_fibo():
    a, b, result = 0, 1, 0
    while b < 4000000:
        if b % 2 == 0:
            result += b
        a, b = b, a+b

    return result

if __name__ == "__main__":
    print sum_of_even_fibo()