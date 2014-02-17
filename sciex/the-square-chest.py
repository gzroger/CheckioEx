__author__ = 'zoli'

class Grid:
    rgrows = None;

    def coord(self, line_point):
        return line_point // 4, line_point % 4

    def __init__(self, rgline):
        self.rgrows = []
        for r in range(4):
            self.rgrows.append([])
            for c in range(4):
                self.rgrows[r].append(dict(horiz=False, vert=False))

        for line in rgline:
            r0, c0 = self.coord(line[0]-1)
            r1, c1 = self.coord(line[1]-1)
            assert ((r0 == r1 and abs(c1-c0)==1 or c0 == c1 and abs(r1-r0)==1)), "should be same row ({0}, {1}) or same column {2}, {3} (from points: {4}, {5})".format(r0, r1, c0, c1, line[0], line[1])
            if r0 == r1:
                for c in range(min(c0, c1), max(c0, c1)):
                    self.rgrows[r0][c]['horiz']=True
            else:
                for r in range(min(r0, r1), max(r0, r1)):
                    self.rgrows[r][c0]['vert']=True

    def countSquares(self):
        result = 0
        for r in range(3):
            for c in range(3):
                for s in range(1,4-max(r, c)):
                    for i in range(s):
                        if not self.rgrows[r+i][c]['vert'] \
                                or not self.rgrows[r][c+i]['horiz']\
                                or not self.rgrows[r+i][c+s]['vert']\
                                or not self.rgrows[r+s][c+i]['horiz']\
                                :
                            break;
                    else:
                        result=result+1
        return result


def checkio(lines_list):
    grd = Grid(lines_list)
    return grd.countSquares()


if __name__ == '__main__':
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"