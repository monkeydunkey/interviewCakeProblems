def reverseWord(st, stInd, stpInd):
    for i in range(0, (stpInd - stInd)//2 + 1):
        st[stInd + i], st[stpInd - i] =  st[stpInd - i], st[stInd + i]
    
def reverseStrWords(st):
    stli = list(st)
    stInd = 0
    for i, c_ in enumerate(stli):
        if c_ == '.':
            #we found a word end
            reverseWord(stli, stInd, i-1)
            stInd = i + 1
    reverseWord(stli, stInd, len(stli) - 1)
    return ''.join(stli)

test = input()
for i in range(test):
    st = raw_input()
    print(reverseStrWords(st))
