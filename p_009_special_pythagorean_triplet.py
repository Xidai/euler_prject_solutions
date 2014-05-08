__author__ = 'Xidai'
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def special_pythagorean_triplet():
    for a in xrange(1, 1000):
        b = (500000 - 1000 * a) / (1000 - a)
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print a, ", ", b, ", ", c
            print "product of three: ", a * b * c
            break


if __name__ == "__main__":
    special_pythagorean_triplet()
