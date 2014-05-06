__author__ = 'Xidai'
from problem_003_largest_prime_factor.largest_prime_factor import is_prime


def the_10001th_prime():
    count, i = 0, 1
    while count != 100000:
        i += 1
        if is_prime(i):
            count += 1
    print i



if __name__ == "__main__":
    the_10001th_prime()