OP = {"conjunction": lambda a, b: a and b,
      "disjunction": lambda a, b: a or b,
      "implication": lambda a, b: not a or b,
      "exclusive": lambda a, b: a != b,
      "equivalence": lambda a, b: a == b}


def boolean(x, y, operation):
    return OP[operation](x, y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
