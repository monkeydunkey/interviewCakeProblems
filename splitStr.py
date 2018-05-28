def solution(S, K):
    # write your code in Python 3.6
    #import pdb; pdb.set_trace()
    S = ''.join(S.upper().split('-'))
    finalSt, i = '', len(S) - 1
    while i >=0 :
        stInd = max(i-K + 1 , 0)
        finalSt = S[stInd: i+1] + '-' + finalSt
        i -= (K-1)
    return finalSt.strip('-')


print solution('2-4A0r7-4k', 4)
