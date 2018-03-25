def stringDecompression(st):
    #import pdb; pdb.set_trace()
    stack = []
    tempSt = ''
    finalSt = ''
    i = 0
    while i < len(st):
        if st[i] == '[':
            #start string
            stack.append(int(tempSt))
            tempSt = ''
        elif st[i] == ']':
            stackSt = ''
            stackTop = stack.pop()
            while type(stackTop) == type(''):
                stackSt = stackTop + stackSt
                stackTop = stack.pop()
            tempSt = (stackSt + tempSt) * stackTop
            stack.append(tempSt)
            tempSt = ''
        else:
            tempSt += st[i]
        i += 1
    for s in stack:
        finalSt += s
    return finalSt + tempSt

print stringDecompression('3[abc]4[ab]c')
print stringDecompression('10[a]')
print stringDecompression('2[3[a]b]')
print stringDecompression('1[2[ab]2[bc]3[cd]e]')
        
