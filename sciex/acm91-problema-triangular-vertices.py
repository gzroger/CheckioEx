__author__ = 'zgaspar'
def checkio(inset):
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