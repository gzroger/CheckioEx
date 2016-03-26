def capture(matrix):
        openQ = [(0, 0)]
        closed = set()
        t = 0
        while openQ:
            t, node = openQ[0]
            del openQ[0]
            for nodeNext in [n for n, x in enumerate(matrix[node]) if n != node and x]:
                if nodeNext not in closed:
                    tNext = t + matrix[nodeNext][nodeNext]
                    iInsert = len(openQ)
                    for ii in (i for i, (t, n) in enumerate(openQ) if t > tNext):
                        iInsert = ii
                        break
                    openQ.insert(iInsert, (tNext, nodeNext))
                    closed |= {nodeNext}
        return t


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
