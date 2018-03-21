def countSpecialPalindrome(st):
    similarityCount = [1]
    stInd = 0
    for i, s in enumerate(st[1:]):
        if s == st[i]:
            maxSimilarity = similarityCount[-1] + 1
            similarityCount[stInd:] = [maxSimilarity] * ((i - stInd) + 1)
            similarityCount.append(maxSimilarity)
            #print st, i, s, maxSimilarity
        else:
            stInd = i + 1
            similarityCount.append(1)

    #print similarityCount
    i = 0
    anagramCount = 0
    while i < len(st):
        anagramCount += (similarityCount[i] * (similarityCount[i] + 1)) // 2
        if similarityCount[i] == 1 and i !=0 and i != len(st) - 1 and st[i - 1] == st[i + 1]:
            anagramCount += min(similarityCount[i-1], similarityCount[i+1])
        i += similarityCount[i]
    return anagramCount - len(st)

if __name__ == '__main__':
    print countSpecialPalindrome('abab')
    print countSpecialPalindrome('aabbb')
