__author__ = 'Xidai'


def has_two_three_digit_factors(n):
    for i in xrange(100, 1000):
        if n % i == 0 and (100 <= n / i <= 999):
            return True
    return False


def largest_palindrome_product():
    for x in xrange(999*999, 100 * 100 + 1, -1):
        string_x = str(x)
        if string_x == string_x[::-1] and has_two_three_digit_factors(x):
            print int(string_x)
            break
    else:
        print "Not found"


if __name__ == "__main__":
    largest_palindrome_product()