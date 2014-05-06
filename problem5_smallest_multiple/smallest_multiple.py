__author__ = 'Xidai'


def smallest_multiple():
    n = 20
    while True:
        for i in range(11, 21):
            if n % i != 0:
                break
        else:
            print n
            break
        n += 20


if __name__ == "__main__":
    smallest_multiple()