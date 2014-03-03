__author__ = 'zgaspar'


def checkio(stExpr):
    stackP = []
    mpOpeningByClosing = {')': '(', ']': '[', '}': '{'}
    for char in stExpr:
        if char in mpOpeningByClosing.values():
            stackP.append(char)
        elif char in mpOpeningByClosing.keys():
            if not stackP or stackP.pop() != mpOpeningByClosing[char]:
                return False
    return not stackP

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("(((1+(1+1))))]") == False, "f"
