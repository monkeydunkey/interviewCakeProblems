'''
Recursive solution for finding all the permutations of a string
'''

def recurse(crtStr, availableSet):
    if len(availableSet):
        retLi = []
        for i, a in enumerate(availableSet):
            temp = crtStr + a
            retLi.extend(recurse(temp, availableSet[:i] + availableSet[i+1:]))
        return retLi
    else:
        return [crtStr]

def createPermutations(st):
    return recurse('', st)

if __name__ == '__main__':
    print createPermutations('abcd')

