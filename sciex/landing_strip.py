def fOk(landing_map, row, col):
    return landing_map[row][col] in ['G', 'S'];

def fOkRowsInCol(landing_map, rowFrom, rowTo, col):
    for row in range(rowFrom, rowTo+1):
        if not fOk(landing_map, row, col):
            return False;
    return True;

def get_max_size_vert(landing_map, rowFrom, rowTo, col):
    colT = col;
    size = 0;
    while (colT < len(landing_map[rowFrom])):
        if not fOkRowsInCol(landing_map, rowFrom, rowTo, colT):
            break;
        size = (rowTo-rowFrom+1)*(colT-col+1);
        colT = colT+1;
    return size;
        

def get_max_size_from(landing_map, row, col):
    rowT = row;
    max_size = 0;
    while (rowT < len(landing_map)):
        if not fOk(landing_map, rowT, col):
            break;
        size_here = get_max_size_vert(landing_map, row, rowT, col);
        if (size_here>max_size):
            max_size = size_here;
        rowT=rowT+1;
    return max_size;

def checkio(landing_map):
    max_size = 0;
    for row in range(0, len(landing_map)):
        for col in range(0, len(landing_map[row])):
            size_here = get_max_size_from(landing_map, row, col);
            if (size_here>max_size):
                max_size = size_here;
    print(landing_map);
    print("max_size: ", max_size);
    return max_size;

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(['G']) == 1, 'One cell - one variant'
    assert checkio(['GS',
                    'GS']) == 4, 'Four good cells'
    assert checkio(['GT',
                    'GG']) == 2, 'Four cells, but with a tree'
    assert checkio(['GGTGG',
                    'TGGGG',
                    'GSSGT',
                    'GGGGT',
                    'GWGGG',
                    'RGTRT',
                    'RTGWT',
                    'WTWGR']) == 9, 'Classic'