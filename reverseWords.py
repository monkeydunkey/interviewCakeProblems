'''
Reverse words in an array the words will be written straight but their order will be reversed

There can be an inplace approach for this problem but doing so will lead to a bit complex and messy code so to avoid that leaving the code at the current state where the implementation is not inplace
'''

def swapWords(wordList, w1_st, w1_end, w2_st, w2_end):
    w1_le, w2_le = w1_end - w1_st, w2_end - w2_st
    return wordList[w2_st: w2_end + 1] + wordList[w1_end + 1 : w2_st] + wordList[w1_st: w1_end + 1]

def reverse_words(wordList):
    i, j = 0, len(wordList) - 1
    while i <= j:
        last_i, last_j = i, j
        while wordList[i] != ' ' and i < len(wordList):
            i += 1
        while wordList[j] != ' ' and j >= 0:
            j -= 1
        if i > j:
            break
        wordList = swapWords(wordList, last_i, i, last_j, j)
    return wordList
        
