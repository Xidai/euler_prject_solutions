_author__ = 'Xidai'
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from p_003_largest_prime_factor import is_prime


def summation_of_primes(n):
    summation = 0
    for i in xrange(2, n):
        if is_prime(i):
            summation += i
    return summation


if __name__ == "__main__":
    print summation_of_primes(2000000)