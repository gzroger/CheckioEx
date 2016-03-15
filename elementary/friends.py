import functools


class Friends:
    def __init__(self, connections):
        self.s = {frozenset(c) for c in connections}

    def add(self, connection):
        c = frozenset(connection)
        res = c not in self.s
        self.s |= {c}
        return res

    def remove(self, connection):
        c = frozenset(connection)
        res = c in self.s
        self.s -= {c}
        return res

    def names(self):
        return functools.reduce(lambda u, v: u | v, self.s, set())

    def connected(self, name):
        return functools.reduce(lambda u, v: u | v, {c - {name} for c in self.s if name in c}, set())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
