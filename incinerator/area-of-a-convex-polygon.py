import math


def length(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


def tarea(p0, p1, p2):
    a = length(p0, p1)
    b = length(p1, p2)
    c = length(p2, p0)
    x = (a ** 2 + b ** 2 - c ** 2) / 2 / b * (1 if c ** 2 <= (a ** 2 + b ** 2) else -1)
    m = math.sqrt(a ** 2 - x ** 2)
    return b * m / 2


def checkio(p):
    return sum([tarea(p[0], p[i], p[i + 1]) for i in range(1, len(p) - 1)])


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
