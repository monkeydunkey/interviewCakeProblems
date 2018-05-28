def compareStr(s1, s2):
    print s1, s2
    charMap = {}
    for s in s1:
        charMap[s] = charMap.get(s, 0) + 1
    for s in s2:
        if charMap.get(s, None) is None:
            return False
        else:
            charMap[s] -= 1
    for k in charMap.keys():
        if charMap[k] != 0: return False
    return True

def solution(S):
    # write your code in Python 3.6
    h, m = list(map(lambda x: int(x), S.split(":")))
    #import pdb; pdb.set_trace()
    #converting to minutes
    t = h * 60 + m
    for i in range(t+1, t + 1440):
        h1, m1 = i / 60, i % 60
        #newTime = str(h1)+":"+str(m1)
        newTime = "%02d:%02d" % (h1, m1)
        if compareStr(newTime, S):
            return newTime
    #Sort of a fallback
    return S

print solution('11:00')
