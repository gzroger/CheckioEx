__author__ = 'zoli'

rgdirNeighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_island(rgrgfland, rgrgfchecked, r, c):
    if 0 > r or r >= len(rgrgfland) or 0 > c or c >= len(rgrgfland[0]) or  rgrgfland[r][c] == 0 or rgrgfchecked[r][c]:
        return 0

    res, rgrgfchecked[r][c] = 1, True
    for direction in rgdirNeighbours:
        r1, c1 = r + direction[0], c + direction[1]
        res += count_island(rgrgfland, rgrgfchecked, r1, c1)
    return res

def checkio(rgrgfland):
    rgrgfchecked = [[False for c in row] for row in rgrgfland]
    rgislands = []
    for r in range(len(rgrgfland)):
        for c in range(len(rgrgfland[r])):
            cisland = count_island(rgrgfland, rgrgfchecked, r, c)
            if 0 != cisland:
                rgislands.append(cisland)

    rgislands.sort()
    return rgislands

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
