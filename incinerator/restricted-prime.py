def checkio(number):
    base = ord('X')
    basepertwo = ord(',')

    x = base+base
    while x <= number * basepertwo:
        y = base+base
        while y <= number * basepertwo:
            if x*y == number*base*base:
                return False
            y += base
        x += base
    return True


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(5), "1st example"
    assert not checkio(6), "2nd example"
    assert not checkio(144)
    assert checkio(28723)
    assert not checkio(28725)

