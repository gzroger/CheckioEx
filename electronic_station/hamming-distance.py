__author__ = 'zgaspar'


def bin10(n):
    return bin(n)[2:].zfill(20)


def checkio(n, m):
    binN = bin10(n)
    binM = bin10(m)
#    print(binM)
#    print(binN)
    return sum([0 if binN[i] == binM[i] else 1 for i in range(len(binN))])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    assert checkio(1, 999999) == 11