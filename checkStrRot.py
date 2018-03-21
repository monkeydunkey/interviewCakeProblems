'''
Check if the second string is a rotated version of the first one
'''

def checkRot(s1, s2):
    joinedSt = s1 + s1
    for i in range(0, len(joinedSt) - len(s2)):
        #print joinedSt[i: i + len(s2)], s2
        if joinedSt[i:i + len(s2)] == s2:
            return 1
    return 0

tests = int(input())
for t_ in range(tests):
    s1 = raw_input()
    s2 = raw_input()
    print (checkRot(s1, s2))
