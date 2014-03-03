__author__ = 'zgaspar'


def checkio(data):
    return 0 if not data else data[0] + checkio(data[1:])


if __name__ == "__main__":
    assert checkio([1, 2, 3]) == 6, "alma"