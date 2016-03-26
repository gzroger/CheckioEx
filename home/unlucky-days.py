import datetime


def checkio(year):
    return len([d for d in [datetime.date(year, m, 13) for m in range(1, 13)] if d.weekday() == 4])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
