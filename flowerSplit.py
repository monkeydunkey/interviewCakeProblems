def solution(P, K):
    if K == len(P):
        return len(P)
    # write your code in Python 3.6
    bloomMap = {}
    for i, r in enumerate(P):
        bloomMap[i + 1] = r
    splits = [0, len(P) + 1]
    regions = [range(1,len(P)+1)]
    for i in range(len(P) - 1, 0, -1):
        newSplit = bloomMap[i+1]
        for j, region in enumerate(regions):
            if newSplit in region:
                for ele, jj in enumerate(region):
                    if ele == newSplit:
                        r1 = region[:jj]
                        r2 = region[jj+1:]
                        if len(r1)== K or len(r2)==K:
                            return i
                        regions.pop(j)
                        regions.extend([r1, r2])
        
    return -1


print 
