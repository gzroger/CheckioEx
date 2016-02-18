VOWELS = "aeiouy"

def tryieldGen(phrase):
    ich = 0
    while ich < len(phrase):
        yield phrase[ich]
        ch = phrase[ich]
        if ch == " ":
            ich+=1
        elif ch in VOWELS:
            ich+=3
        else:
            ich+=2

def trR(phrase):
    if len(phrase) == 0:
        return ''

    ch = phrase[0]
    if ch == ' ':
        return phrase[0] + trR(phrase[1:])
    elif ch in VOWELS:
        return phrase[0] + trR(phrase[3:])
    else:
        return phrase[0] + trR(phrase[2:])

def translate(phrase):
    return trR(phrase)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
