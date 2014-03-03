__author__ = 'zgaspar'


def checkio(num):
    rgprime = [2, 3, 5, 7]
    mpFactorByDigit = {}
    for numT in range(2, 10):
        if numT in rgprime:
            i = 0
            while num % numT == 0:
                num //= numT
                i += 1
            mpFactorByDigit[numT] = i
        else:
            mpFactorByDigit[numT] = 0
    if num > 1:
        return 0

    rgrules = [([(2, 3)], 8), ([(2, 2)], 4), ([(2, 1), (3, 1)], 6), ([(3, 2)], 9)]
    while True:
        for rule in rgrules:
            rgInRule = rule[0]
            outRule = rule[1]
            if all([mpFactorByDigit[inrule[0]] >= inrule[1] for inrule in rgInRule]):
                for inrule in rgInRule:
                    mpFactorByDigit[inrule[0]] -= inrule[1]
                mpFactorByDigit[outRule] += 1
                break
        else:
            break

    res = ''.join([str(i) * mpFactorByDigit[i] for i in range(2, 10)])
#    print(res)
    return int(res) if res else 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"
    assert checkio(3645) ==  5999, "xxx"