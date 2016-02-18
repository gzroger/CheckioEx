def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

RADIXES=list(char_range('0','9'))+list(char_range('A','Z'))

def checkio(number):
    maxchar = max(list(number))
    for radix in range(RADIXES.index(maxchar)+1, len(RADIXES)+1):
        num = int(number, radix)
        if num%(radix-1) == 0:
            return radix
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k is not exist"
    assert checkio("ZZZ") == 36, "36"
    print('Local tests done')
