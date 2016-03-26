M,a,b=1003010,set(),[]
for p in range(2,M):
    if p not in a:
        z=str(p)
        if z==z[::-1]:
            b+=[p]
        a|=set(range(p*2,M,p))
def golf(n):
    for i in range(n+1,M):
        if i in b:
            return i


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert golf(2) == 3, "example"
    assert golf(13) == 101, "13"
