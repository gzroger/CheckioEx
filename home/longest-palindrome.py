def palstart(text, minlen):
    for icTo in range(len(text) - 1, minlen-1, -1):
        for x in range((icTo+1) // 2):
            if text[x] != text[icTo - x]:
                break
        else:
            return text[0:icTo + 1]


def longest_palindromic(text):
    longest = ""
    for ic in range(len(text)):
        palfromhere = palstart(text[ic:], minlen=len(longest))
        if palfromhere and len(longest) < len(palfromhere):
            longest = palfromhere
        if len(text) - ic - 1 < len(longest):
            break
    return longest


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abc") == "a", "abc"
