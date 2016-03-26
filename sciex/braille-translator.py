def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36)}
WHITESPACE = convert(0)


def apdch(res, dch):
    if res and len(res[-1]) < 10:
        res[-1].append(dch)
    else:
        res.append([dch])


def braille_page(text: str):
    rgrgdch = []
    for ch in text:
        if '0' <= ch <= '9':
            apdch(rgrgdch, NUMBER_FORMAT)
            apdch(rgrgdch, LETTERS_NUMBERS[9] if ch == '0' else LETTERS_NUMBERS[int(ch) - 1])
        elif 'A' <= ch <= 'Z':
            apdch(rgrgdch, CAPITAL_FORMAT)
            apdch(rgrgdch, LETTERS_NUMBERS[ord(ch) - ord('A')])
        elif 'a' <= ch <= 'z':
            apdch(rgrgdch, LETTERS_NUMBERS[ord(ch) - ord('a')])
        elif ch == ' ':
            apdch(rgrgdch, WHITESPACE)
        elif ch in PUNCTUATION:
            apdch(rgrgdch, PUNCTUATION.get(ch))
        else:
            raise 'NoWay'

    rgblr = []
    maxlen = 0
    for rgdch in rgrgdch:
        blr1 = []
        blr2 = []
        blr3 = []
        blrsep = []

        for dch in rgdch:
            blr1 += dch[0] + [0]
            blr2 += dch[1] + [0]
            blr3 += dch[2] + [0]
            blrsep += [0, 0, 0]
        maxlen = max(maxlen, len(blr1))
        for x in range(maxlen - len(blr1)):
            blr1 += [0]
            blr2 += [0]
            blr3 += [0]
            blrsep += [0]

        rgblr.append(tuple(blr1[0:-1]))
        rgblr.append(tuple(blr2[0:-1]))
        rgblr.append(tuple(blr3[0:-1]))
        rgblr.append(tuple(blrsep[0:-1]))

    rgblr = tuple(rgblr[0:-1])
    return rgblr


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, text, answer):
        result = func(text)
        return answer == tuple(tuple(row) for row in result)


    assert checker(braille_page, "hello 1st World!", (
        (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
        (1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0))
                   ), "Example"
    assert checker(braille_page, "42", (
        (0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0),
        (0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0),
        (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0))), "42"
    assert checker(braille_page, "CODE", (
        (0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0))
                   ), "CODE"
