def kDistinctSubString(st, k):
    #import pdb; pdb.set_trace()
    charMap = {}
    currCount = 0
    stInd = 0
    endInd = -1
    for i, a in enumerate(st):
        if charMap.get(a, -1) == -1:
            #New Character
            currCount += 1
            charMap[a] = i
        else:
            #we have already seen this guy before
            lastInd = charMap[a]
            diff = lastInd - stInd
            currCount -= (charMap[a] - stInd)
            for jj in charMap.keys():
                if charMap[jj] < charMap[a]:
                    charMap[jj] = -1
            charMap[a] = i
            stInd = lastInd + 1
        if currCount >= k:
            endInd = i
            break
    if currCount >= k:
        return st[stInd: endInd+1]
    else:
        return -1


print kDistinctSubString('abbcdba', 4)
print kDistinctSubString('abbcdbb', 4)

