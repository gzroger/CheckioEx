def minmax(*args, **kwargs):
    try:
        if len(args) == 1:
            args = iter(args[0])
    except TypeError as te:
        pass

    key = kwargs.get("key", None)
    ord = kwargs.get("ord")
    maxA, vmax = None, None
    for arg in args:
        v = key(arg) if key else arg
        if vmax is None or ord(v, vmax):
            vmax = v
            maxA = arg
    return maxA


def min(*args, **kwargs):
    return minmax(*args, ord=lambda v, w: v < w, **kwargs)


def max(*args, **kwargs):
    return minmax(*args, ord=lambda v, w: v > w, **kwargs)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert max(3, 2) == 3, "Simple case max"
#    assert min(3, 2) == 2, "Simple case min"
#    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
#    assert min("hello") == "e", "From string"
#    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
#    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min(abs(i) for i in range(-10, 10)) == 0, "0 is min"
