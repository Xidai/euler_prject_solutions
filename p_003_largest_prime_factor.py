__author__ = 'Xidai'

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt


def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    if not num % 2 or not num % 3:
        return False
    for i in range(5, int(num**0.5) + 1, 6):
        if not num % i or not num % (i + 2):
            return False
    return True


def largest_prime_factor(n):
    divisor = 2
    while n > 1:
        if n % divisor == 0 and is_prime(divisor):
            n /= divisor
            divisor -= 1
        divisor += 1
    return divisor


def cheat(n):
    i = 2
    test = 0
    while n > i:
        while n % i == 0:
            n /= i
        i += 1
        if i * i > n > 1:
            print n
            test = 1
            break
    if test == 0:
        print i - 1


def cheat2():
    n = 600851475143
    divisor = 2
    count = 0
    while n > 1:
        count += 1
        print "n=", n, "divisor=", divisor
        if n % divisor == 0:
            n /= divisor
            divisor -= 1
        divisor += 1
    print "count=", count
    return divisor


def cheat3():
    roots = []
    product = 1
    x = 2
    number = input("number?: ")
    y = number
    while product != number:
        while y % x == 0:
            roots.append(x)
            y /= x
            product *= roots[-1]
        x += 1
    print roots


if __name__ == "__main__":
    print largest_prime_factor(600851475143)