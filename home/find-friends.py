def putEdge(mpNodeByNode, n0, n1):
    if n0 not in mpNodeByNode:
        mpNodeByNode[n0] = set()
    mpNodeByNode[n0].add(n1)


def check_connection(network, n1, n2):
    mpNodeByNode = dict()
    for edge in network:
        a, b = edge.split("-")
        putEdge(mpNodeByNode, a, b)
        putEdge(mpNodeByNode, b, a)

    opened = [n1]
    closed = set()
    while opened:
        n = opened.pop()
        closed.add(n)
        if n == n2:
            return True
        for nNeigh in mpNodeByNode[n]:
            if nNeigh not in closed:
                opened.append(nNeigh)

    return False



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
