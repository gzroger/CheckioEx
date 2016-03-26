def rc(p):
    return int(p[1]) - 1, ord(p[0]) - ord('a')


def safe_pawns(pawns):
    t = dict()
    rcp = [rc(p) for p in pawns]
    for (r, c) in rcp:
        t[(r + 1, c - 1)] = True
        t[(r + 1, c + 1)] = True

    for r in range(8):
        for c in range(8):
            print(("P" if (r, c) in rcp else "x") if t.get((r, c), False) else ("q" if (r, c) in rcp else "-"), end="")
        print()
    x = [(r, c) for (r, c) in rcp if t.get((r, c), False)]
    print(x)
    return len(x)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
