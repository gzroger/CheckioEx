class Cypher:
    keyleft = "abcdefghijklmnopqrstuvwxyz0123456789"

    def __init__(self, key: str):
        self.key = key + Cypher.keyleft
        self.tbl = self.tblCreate()
        self.mpPosByChTbl = {ch: (i, j) for i, row in enumerate(self.tbl) for j, ch in enumerate(row)}
        print("tbl", self.tbl)

    def tblCreate(self) -> [str]:
        keyUni = ""
        for ch in self.key:
            if ch not in keyUni:
                keyUni += ch
        return [keyUni[x * 6:(x + 1) * 6] for x in range(6)]

    def encode(self, msg: str) -> str:
        msgPrep = self.prep(msg)
        res = "".join([self.crp(a, b) for a, b in msgPrep])
        print(res)
        return res

    def decode(self, cms: str) -> str:
        msgPrep = [cms[i*2:i*2 + 2] for i in range(len(cms) // 2)]
        print(msgPrep)
        res = "".join([self.decrp(a, b) for a, b in msgPrep])
        print(res)
        return res

    def prep(self, msg: str):
        msgPrep = [ch.lower() for ch in msg if ch.isalnum()]
        i = 0
        res = []
        while True:
            if i == len(msgPrep):
                break
            a = msgPrep[i]
            i += 1
            if i < len(msgPrep):
                b = msgPrep[i]
                if a == b:
                    b = "x" if a != "x" else "z"
                else:
                    i += 1
            else:
                b = "z" if a != "z" else "x"
            res += [(a, b)]

        print(res)
        return res

    def crp(self, a, b):
        aRow, aCol = self.mpPosByChTbl[a]
        bRow, bCol = self.mpPosByChTbl[b]
        if aRow == bRow:
            aCrp = self.tbl[aRow][(aCol + 1) % 6]
            bCrp = self.tbl[bRow][(bCol + 1) % 6]
        elif aCol == bCol:
            aCrp = self.tbl[(aRow + 1) % 6][aCol]
            bCrp = self.tbl[(bRow + 1) % 6][bCol]
        else:
            aCrp = self.tbl[aRow][bCol]
            bCrp = self.tbl[bRow][aCol]
        return aCrp + bCrp

    def decrp(self, a, b):
        aRow, aCol = self.mpPosByChTbl[a]
        bRow, bCol = self.mpPosByChTbl[b]
        if aRow == bRow:
            aCrp = self.tbl[aRow][(aCol - 1) % 6]
            bCrp = self.tbl[bRow][(bCol - 1) % 6]
        elif aCol == bCol:
            aCrp = self.tbl[(aRow - 1) % 6][aCol]
            bCrp = self.tbl[(bRow - 1) % 6][bCol]
        else:
            aCrp = self.tbl[aRow][bCol]
            bCrp = self.tbl[bRow][aCol]
        return aCrp + bCrp


def encode(message, key):
    cypher = Cypher(key)
    return cypher.encode(message)


def decode(secret_message, key):
    cypher = Cypher(key)
    return cypher.decode(secret_message)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
