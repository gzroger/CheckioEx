def rotate(state, pipe_numbers):
    res = []
    for r in range(len(state)):
        rotstate = (state + state)[len(state)-r : 2*len(state)-r]
        if all([rotstate[n]==1 for n in pipe_numbers]):
            res.append(r)
    return res



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
    assert rotate([1,1,1],[0,1,2]) == [0, 1, 2]