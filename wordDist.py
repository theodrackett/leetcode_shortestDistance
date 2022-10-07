def shortestDistance(wordsDict, word1: str, word2: str):
    # go thru the dict looking for the words
    # create a hash map of each word and their indices
    wordMap = {}
    for i, word in enumerate(wordsDict):

        if word in wordMap:
            my_list = wordMap[word]
            my_list.append(i)
            wordMap[word] = my_list
        else:
            my_list = [i]
            wordMap[word] = my_list

    # find the words of interest and find their closest indices
    closest = abs(wordMap[word1][0] - wordMap[word2][0])
    print(f"word1 contains {wordMap[word1]}")
    for i in range(len(wordMap[word1])):
        for j in range(len(wordMap[word2])):
            if abs(wordMap[word1][i] - wordMap[word2][j]) < closest:
                closest = abs(wordMap[word1][i] - wordMap[word2][j])

    return closest


wordsDict = ["a","a","b","b"]
word1 = "a"
word2 = "b"

print(shortestDistance(wordsDict,word1,word2))
