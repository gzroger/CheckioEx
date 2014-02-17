def flatten_r(data, inlist):
    if not isinstance(data, list):
        inlist.append(data);
        return;
        
    for d in data:
        flatten_r(d, inlist);
        

def checkio(data):
    lst = []
    flatten_r(data, lst);
    return lst;


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3]) == [1, 2, 3], 'First example'
    assert checkio([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], 'Second example'
    assert checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) ==\
        [2, 4, 5, 6, 6, 6, 6, 6, 7], 'Third example'
