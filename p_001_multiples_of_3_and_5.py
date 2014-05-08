__author__ = 'Xidai'


def multiples():
    multiples_list = [x for x in range(1, 100000000) if x % 3 == 0 or x % 5 == 0]
    print sum(multiples_list)

if __name__ == "__main__":
    multiples()