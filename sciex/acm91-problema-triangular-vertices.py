__author__ = 'zoli'

"""
1: 1-1 1
2: 2-3 1+1 - 1+2
3: 4-6 (1+2)+1 - 1+2+3

Sum(1..n) = 1+n + 2+n-1 ... n/2-1+n/2+1 = (n+1)*n/2 = n*n/2+n/2

X = (n+1)*n/2
0 = n*n+n-2X

x =

"""

import math


class Tripnt(object):
    def __init__(self, numtripnt):
        self.numtripnt = numtripnt
        self.zdim = math.ceil((math.sqrt(1+4*2*numtripnt)-1)/2)
        self.xdim = numtripnt - (self.zdim - 1)*self.zdim//2
        assert (0 < self.zdim), "zdim assert"
        assert (0 < self.xdim <= self.zdim), "xdim assert"

    def x(self):
        return self.xdim

    def y(self):
        return self.zdim-self.xdim+1

    def z(self):
        return self.zdim

    def __repr__(self):
        return str((self.x(), self.y(), self.z()))

    def __eq__(self, other):
        return self.numtripnt == other.numtripnt

    def dist(self, other):
        return max(abs(self.x() - other.x()), abs(self.y() - other.y()), abs(self.z() - other.z()))


def reachFromToWith(tripntFrom, tripntTo, rgtripnt):
    for i, tripnt in enumerate(rgtripnt):
        if tripnt.x() == tripntFrom.x() or tripnt.y() == tripntFrom.y() or tripnt.z() == tripntFrom.z():
            if tripnt == tripntTo and len(rgtripnt) == 1:
                return [tripnt]
            res = reachFromToWith(tripnt, tripntTo, rgtripnt[:i] + rgtripnt[i + 1:])
            if res is not None:
                return [tripnt] + res
    return None


def checkio(rgnumtripnt):
    if len(rgnumtripnt) in (3, 4, 6):
        rgtripnt = [Tripnt(numtripnt) for numtripnt in rgnumtripnt]
        rgtripntCircle = reachFromToWith(rgtripnt[0], rgtripnt[0], rgtripnt[:])

        if not rgtripntCircle:
            return 0

        for i in range(len(rgtripntCircle)-2):
            if not rgtripntCircle[i].dist(rgtripntCircle[i+1]) == rgtripntCircle[i+1].dist(rgtripntCircle[i+2]):
                return 0

        return len(rgnumtripnt)
    else:
        return 0

if __name__ == "__main__":
    assert checkio([1, 2, 3]) == 3, 'Triangle'
    assert checkio([11, 13, 29, 31]) == 0, 'It is not parallelogram'
    assert checkio([26, 11, 13, 24]) == 4, 'It is parallelogram'
    assert checkio([4, 5, 9, 13, 12, 7]) == 6, 'Hexagon'
    assert checkio([1, 2, 3, 4, 5]) == 0, 'It is weird triangle'
    assert checkio([47]) == 0, 'Point'
    assert checkio([11, 13, 23, 25]) == 0, 'It is not parallelogram, again'
    assert checkio([2,6,8]) == 0, 'triangle but not aligned!'