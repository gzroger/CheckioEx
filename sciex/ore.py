__author__ = 'zgaspar'
import math
def checkio(rgprobe):
    rgyxcouldbe = set()
    rgxywewere = [(x, y) for [y, x, r] in rgprobe]
    for y in range(10):
        for x in range(10):
            if (x, y) in rgxywewere:
                continue
            all_ok = True
            for probe in rgprobe:
                y0, x0, r = probe[0], probe[1], probe[2]
                all_ok = all_ok and round( math.sqrt( abs((x-x0)*(x-x0) + (y-y0)*(y-y0)) ) ) == r
            if all_ok:
                rgyxcouldbe.add((y, x))

    print(rgyxcouldbe)
    return list(rgyxcouldbe.pop())

if __name__ == '__main__':
    assert checkio([[7,3,6],[1,2,1]]) == [1,3]
    assert checkio([[7,3,6],[1,2,11]]) == [9, 9]
