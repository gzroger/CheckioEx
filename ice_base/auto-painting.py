__author__ = 'zoli'


def checkio(capacity, number):
    res = ""
    stage = [0] * number
    while True:
        if all([c == 2 for c in stage]):
            return stage
        stageNext = stage[:]
        p = 0
        for i, c in enumerate(stage):
            if c < 2:
                stageNext[i] += 1
                p += 1
                res += str(i)
            if p >= capacity:
                break
        res += ","
        stage = stageNext
        print(res[:-1])
    return res[:-1]



                #These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    print(checkio(2, 3))  # "01,12,02"
    print(checkio(6, 3))  # "012,012"
    print(checkio(3, 6))  # "012,012,345,345"
    print(checkio(1, 4))  # "0,0,1,1,2,2,3,3"
    print(checkio(2, 5))  # "01,01,23,42,34"