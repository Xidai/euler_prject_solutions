__author__ = 'Xidai'


def sum_of_squares(n):
    return sum([x * x for x in range(1, n + 1)])


def square_of_sum(n):
    return sum(range(1, n + 1))**2


def sum_square_difference(n):
    print square_of_sum(n) - sum_of_squares(n)


if __name__ == "__main__":
    sum_square_difference(100)