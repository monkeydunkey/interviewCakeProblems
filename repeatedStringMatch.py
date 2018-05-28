def repeatedStringMatch(A, B):
    count = 1
    checkString = A
    while len(checkString) <= 2 * len(B):
        print checkString, len(checkString), 2 * len(B)
        if B in checkString:
            return count
        count += 1
        checkString += A
    return -1

print repeatedStringMatch("abcd", "cdabcdab")
