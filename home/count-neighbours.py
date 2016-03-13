neigh = [(r, c) for r in range(-1, 2) for c in range(-1, 2) if not (r == 0 and c == 0)]


def neighbours(grid, r0, c0):
    rc = [(r, c) for (r, c) in ((r0 + rD, c0 + cD) for (rD, cD) in neigh) if
          0 <= r < len(grid) and 0 <= c < len(grid[0])]
    return [grid[r][c] for (r, c) in rc]


def count_neighbours(grid, row, col):
    return sum(neighbours(grid, row, col))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
