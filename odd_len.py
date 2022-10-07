def odd_len(word1, word2):
    w1 = 0
    w2 = 0
    new_word = ""

    while w1 < len(word1) and w2 < len(word2):
        new_word += word1[w1]
        new_word += word2[w2]
        w1 += 1
        w2 +=1

    if len(word1) < len(word2):
        new_word += word2[len(word1):]
    else:
        new_word += word1[len(word2):]

    return new_word

word1 = "abcd"
word2 = "pqrdef"
print(odd_len(word1, word2))
