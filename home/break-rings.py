import functools


def removeFromX(x, cut, node):
    return frozenset(s for s in x if node not in s), frozenset(cut | {node})


def countFree(x, cut, hlmnodeAll):
    return len(functools.reduce(lambda w, u: w - u, x, hlmnodeAll - cut))


def break_rings(rings):
    x0 = frozenset(frozenset(s) for s in rings)
    hlmnodeAll = frozenset(functools.reduce(lambda u, v: u | v, rings, set()))
    # print(hlmnodeAll)
    openX = [(x0, frozenset())]
    closed = set()
    maxFree, maxFreeState = 0, None
    while openX:
        x, cut = openX.pop()
        closed.add((x, cut))
        free = countFree(x, cut, hlmnodeAll)
        # print("opened state free", free, x, cut)
        if free > maxFree:
            maxFree = free
            maxFreeState = x, cut

        hlmnode = functools.reduce(lambda u, v: u | v, x, set())
        for node in hlmnode:
            xNew, cutNew = removeFromX(x, cut, node)
            if (xNew, cutNew) not in closed:
                openX.append((xNew, cutNew))

    # print(maxFreeState)
    return len(maxFreeState[1])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
