def checkio(data):
    dn = [[int(ipd) for ipd in ip.split(".")] for ip in data]
    res = []
    eq = True
    for d in range(32):
        if eq:
            x = 7 - d % 8
            y = d // 8
            b = [d[y] & (2 ** x) for d in dn]
            print(d, ": ", b)
            if not all([bd == b[0] for bd in b]):
                per = d
                eq = False
            else:
                res.append(b[0])
        else:
            res.append(0)
    res = '.'.join([str(sum(res[x*8 : (x+1)*8])) for x in range(4)])
    return res + "/" + str(per)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
