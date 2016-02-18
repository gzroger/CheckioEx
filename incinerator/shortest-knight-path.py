alpha = 'abcdefgh'

steps = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]


def stepWithKnight(p):
    return [(p[0] + step[0], p[1] + step[1]) for step in steps if 0 < p[0] + step[0] < 9 and 0 < p[1] + step[1] < 9]


def path(p, mpParentByP):
    while p:
        yield p
        p = mpParentByP[p]


def findShortestPath(p0, p1):
#    print(p0, '->', p1)
    openQ = [p0]
    mpParentbyP = {p0: None}
    while openQ:
        p = openQ.pop(0)

        if p == p1:
            return list(path(p, mpParentbyP))
        for pNext in stepWithKnight(p):
            if not pNext in mpParentbyP:
                openQ.append(pNext)
                mpParentbyP[pNext] = p

    return []


def checkio(cells):
    xcells = cells.split("-")
    r0 = alpha.index(xcells[0][0]) + 1
    c0 = int(xcells[0][1])
    r1 = alpha.index(xcells[1][0]) + 1
    c1 = int(xcells[1][1])
    path = findShortestPath((r0, c0), (r1, c1))
#    print(path)
    return len(path)-1


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
