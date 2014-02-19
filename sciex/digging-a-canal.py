__author__ = 'zgaspar'

rgdirection = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def hlmposOneStepDist(rgrgfland, hlmposWeWere, pos):
    hlmRes = set()
    for posNeighbour in [(pos[0] + direction[0], pos[1] + direction[1]) for direction in rgdirection]:
        if posNeighbour[0] < 0 or posNeighbour[1] < 0 or posNeighbour[1] >= len(rgrgfland[0])\
                or posNeighbour in hlmposWeWere:
            continue
        elif posNeighbour[0] == len(rgrgfland) or rgrgfland[posNeighbour[0]][posNeighbour[1]] == 1:
            hlmRes.add(posNeighbour)
        else:
            hlmposWeWere.add(posNeighbour)
            hlmRes.update(hlmposOneStepDist(rgrgfland, hlmposWeWere, posNeighbour))
    return hlmRes


def checkio(rgrgfland):
    hlmposOneStep = set((-1, x) for x in range(len(rgrgfland[0])))
    hlmposWeWere = set()
    for dist in range(len(rgrgfland) + 2):
        hlmposNextOneStep = set()
        hlmposWeWere.update(hlmposOneStep)
        for pos in hlmposOneStep:
            if pos[0] == len(rgrgfland):
                #print("dist: ", dist-1)
                return dist - 1
            hlmposNextOneStep.update(hlmposOneStepDist(rgrgfland, hlmposWeWere, pos))
        hlmposOneStep = hlmposNextOneStep
    #print("c")

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 1, 1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1]]) == 2, "1st example"
    assert checkio([[0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0]]) == 3, "2nd example"
    assert checkio([[1, 1, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1]]) == 2, "3rd example"

    assert checkio([[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]) == 8, "blabla"