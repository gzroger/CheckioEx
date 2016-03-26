def edges(polygon):
    for i in range(len(polygon)):
        yield (polygon[i], polygon[(i+1)%len(polygon)])


def crosses(edge, y):
    x0, y0 = edge[0]
    x1, y1 = edge[1]
    if y0>y1:
        xT, yT = x0, y0
        x0, y0 = x1, y1
        x1, y1 = xT, yT

    if y0<=y<=y1:
        if y0 == y1:
            if y == y0:
                return x0 # to x1
            else:
                return
        else:
            xD = x1 - x0
            yD = y1 - y0
            yZ = y - y0
            xZ = xD*yZ/yD

            return x0+xZ
    else:
        return

def crossingY(polygon, y: int):
    fInside = polygon[0][1] == y
    rgcrosses=[]
    if fInside:
        rgcrosses.append(polygon[0])
    for edge in edges(polygon):
        cross = crosses(edge, y)
        if cross:
            fInside = not fInside
            rgcrosses.append(cross)

    return rgcrosses



def is_inside(polygon, point):
    rgcross = crossingY(polygon, point[1])
    x = point[0]
    for i in range(0, len(rgcross), 2):
        x0 = rgcross[i]
        x1 = rgcross[i+1]
        if x0<=x<=x1 or x1<=x<=x0:
            return True
    return False


if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"
