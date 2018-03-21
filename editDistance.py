def editDistance(st1, st2):
    arr = [[0 for x in range(len(st1) + 1)] for y in range(len(st2) + 1)]
    for i in range(len(st1) + 1):
        for j in range(len(st2) + 1):
            if i == 0:
                arr[j][i] = j
                continue
            if j == 0:
                arr[j][i] = i
                continue
            if st1[i-1] == st2[j-1]:
                arr[j][i] = arr[j-1][i-1]
            else:
                arr[j][i] = 1 + min(arr[j-1][i-1], arr[j][i-1], arr[j-1][i])
    return arr[-1][-1]


if __name__ == '__main__':
    print editDistance('geeks', 'gee')
    print editDistance('abc', 'aebdce')
    print editDistance('abc', 'def')
