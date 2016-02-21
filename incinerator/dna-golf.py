def golf(s,p):
    return ''.join(sorted([s[p*x:p*(x+1)]for x in range(len(s)//p)],key=lambda z:([1 for i in range(p) for j in range(i) if z[i]<z[j]])))

if __name__ == '__main__':
    assert golf("ACGGCATAACCCTCGA", 3) == "ACGCCCTAATCGGCA"
