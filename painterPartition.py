def dividePartition(logs, k):
    arr = [[0 for x in xrange(len(logs) + 1)] for y in xrange(k + 1)]
    sumTillNow = 0
    for i in range(1, len(logs) + 1):
        sumTillNow += logs[i- 1]
        arr[1][i] = sumTillNow

    for i in range(1, k + 1):
        arr[i][1] = logs[0]

    for i in xrange(2, k + 1):
        for j in xrange(2, len(logs) + 1):
            be = float('inf')
            for p in xrange(1, j + 1):
                #print (logs[p-1:j], p, j)
                be = min(be, max(arr[i-1][p - 1], sum(logs[p-1:j])))
            arr[i][j] = be
            #print arr
    return arr[-1][-1]


print dividePartition([10, 20, 30], 2)
print dividePartition([10, 10, 10], 3)
print dividePartition([40, 20, 60], 2)
print dividePartition([10, 10, 10, 10], 2)
print dividePartition([10, 20, 30, 40], 2)
