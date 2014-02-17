import math
def checkio(a, b, c):
    l = [a, b, c];
    l.sort();
    a = l[0];
    b = l[1];
    c = l[2];
    
    if (c>=a+b):
        return [0,0,0];
    
    x = (a*a-b*b+c*c)/2/c;
    alpha = math.acos(x/a) / math.pi * 180;
    beta = math.acos((c-x)/b) / math.pi * 180;
    al = [round(alpha), round(beta), round(180-alpha-beta)];
    al.sort();
    return al;

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
