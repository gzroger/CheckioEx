adfgvx = "ADFGVX"


def createMpkey(keyword):
    nodup = []
    for ch in keyword:
        if ch not in nodup:
            nodup.append(ch)

    return {ch: nodup.index(ch) for ch in set(keyword)}


def encode(message, secret_alphabet, keyword):
    mpCode = mpCodeCreate(secret_alphabet)
    factionated = ''.join([mpCode[ch.lower()] for ch in message if ch.isalnum()])
    mpkey = createMpkey(keyword)
    splitted = [factionated[i * len(mpkey):(i + 1) * len(mpkey)] for i in range(len(factionated) // len(mpkey) + 1)]
    res = ''.join([splitted[col][mpkey[ch]] for ch in sorted(mpkey.keys()) for col in range(len(splitted)) if
                    mpkey[ch] < len(splitted[col])])
    return res


def mpCodeCreate(secret_alphabet):
    mpCode = {secret_alphabet[i * len(adfgvx) + j]: adfgvx[i] + adfgvx[j] for i in range(len(adfgvx)) for j in
              range(len(adfgvx))}
    return mpCode


def decode(message, secret_alphabet, keyword):
    mpkey = createMpkey(keyword)
    msgsplitted = [[] for _ in range(len(mpkey))]
    msg = message
    cX = len(message) // len(mpkey)
    for ch in sorted(mpkey):
        c = cX + 1 if mpkey[ch] < (len(message) % len(mpkey)) else cX
        msgsplitted[mpkey[ch]] = msg[0:c]
        msg = msg[c:]
    assert not msg
    factionated = ''.join(
        [msgsplitted[j][i] for i in range(len(msgsplitted[0])) for j in range(len(mpkey)) if i < len(msgsplitted[j])])
    pairs = [factionated[i * 2:(i + 1) * 2] for i in range(len(factionated) // 2)]
    message = ''.join([secret_alphabet[adfgvx.index(pair[0]) * len(adfgvx) + adfgvx.index(pair[1])] for pair in pairs])
    return message


if __name__ == '__main__':
    decode("DXDXDGVXFXDVVDXXXFAXXGDDGGDDGDAVDGFGGVVVFAVGGXFXADFAFXGXFAVGFXVXGVXGGVXFAGXFXAFVGFAFDXGFFFDVDGGFAFXX", "zm3ahs68ig9bc7xy4pu1jntvld2rk05oewfq", "yep")
    # assert encode("I am going",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    # assert decode("FXGAFVXXAXDDDXGA",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "cipher") == 'iamgoing', "decode I am going"
    # assert encode("attack at 12:00 am",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    # assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'attackat1200am', "decode attack"
    # assert encode("ditiszeergeheim",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    # assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    # assert encode("I am going",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    # assert decode("DXGAXAAXXVDDFGFX",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'iamgoing', "decode weasel == weasl"
