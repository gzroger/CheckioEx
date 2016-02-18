mp = dict()

def countWays(dice_number, sides, target):
    if dice_number == 0:
        return 1 if target == 0 else 0

    if not 1 * dice_number <= target <= sides * dice_number:
        return 0

    k = (dice_number, sides, target)
    if not k in mp:
        cAll = 0
        for c in range(1, sides + 1):
            cAll += countWays(dice_number - 1, sides, target - c)
        mp[k] = cAll
    return mp[k]


def probability(dice_number, sides, target):
    c = countWays(dice_number, sides, target)
    print(c)
    return c / (sides ** dice_number)


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
