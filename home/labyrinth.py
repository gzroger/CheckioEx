#Your code here
#You can import some modules or create additional functions

dirs = [(-1, 0, 'N'), (1, 0, 'S'), (0, -1, 'W'), (0, 1, 'E')];

def isValid(data, pos):
    return data[pos[0]][pos[1]]==0;
    
def untouched(path, pos):
    for p in path:
        if p[0]==pos[0] and p[1]==pos[1]:
            return False;
    return True;

def route(data, path, pos):
    print( "pos: ", pos )

    if pos[0]==10 and pos[1]==10:
        return path;
        
    for d in dirs:
        new_pos = (pos[0]+d[0], pos[1]+d[1], d[2]);
        print ("goint to: ", new_pos)
        if isValid(data, new_pos):
            print("valid") 
            if untouched(path, new_pos):
                print ("untouched")
                newPath = path[:];
                newPath.append(new_pos);
                resultPath = route(data, newPath, new_pos);
                if not resultPath is None:
                    return resultPath;
            
    return None;        

def checkio(data):
    path = route(data, [(1, 1, None)], (1, 1));
    if path is None:
        return '';
    else:
        return ''.join([r[2] for r in path if not r[2] is None]);

#Some hints
#Look to graph search algorithms
#Don't confuse these with tree search algorithms


#This code using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
