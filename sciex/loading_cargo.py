def diff(perm, data):
    diff = 0;
    for i in range(0, len(data)):
        if (perm & 1)==1:
            diff += data[i];
        else:
            diff -= data[i];
        perm = perm//2;
    return abs(diff);

def checkio(data):
    min_diff = -1;
    for perm in range (0, 1<<len(data)):
        d = diff(perm, data);
#        print ("diff ", perm, ": ", d);
        if min_diff == -1 or d<min_diff:
            min_diff = d;
#    print ("min_diff: ", min_diff);
    return min_diff;


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
