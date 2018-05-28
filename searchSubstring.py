def getStartAndEnd(sMap, word):
    print sMap, word
    if not (set(word) <= set(sMap.keys())):
        return [[-1, -1]]
    lastInd, stInd, i, topPos = list(sMap[word[0]]), list(sMap[word[0]]), 1,list( sMap[word[0]])
    while i < len(word):
        topPos = filter(lambda x: x - 1 in lastInd, sMap[word[i]])
        print topPos, lastInd, sMap[word[i]]
        toDelete = filter(lambda x: lastInd[x] + 1 not in topPos, range(len(lastInd)))
        print toDelete, stInd
        for ind in reversed(toDelete):
            stInd.pop(ind)
        if len(topPos) > 0:
            lastInd = topPos
        else: return [[-1, -1]]
        i += 1
    return map(lambda x: [x[1],topPos[x[0]]], enumerate(stInd) )


st = 'aaabbcc'
sMap = {}
for i, s in enumerate(st):
    sMap[s] = sMap.get(s, []) + [i]
print getStartAndEnd(sMap, 'aaa')
