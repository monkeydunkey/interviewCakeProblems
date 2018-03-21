def removeInstances(base, rem):
    base, rem = list(base), rem.lower()
    stInd = 0
    remInd = 0
    for i, b in enumerate(base):
        if remInd == len(rem):
            base[stInd: i] = [''] * (i - stInd)
            remInd = 0

        if rem[remInd] == b.lower():
            stInd = i if remInd == 0 else stInd
            remInd += 1
            #print remInd, b, rem
    #print rem, base, remInd
    if remInd == len(rem):
        base[stInd:] = ''
    return ''.join(base)

if __name__ == '__main__':
    print removeInstances('Hello there', 'llo')
    print removeInstances('Hello there', 'e')
    print removeInstances('Hello there', 'x')
