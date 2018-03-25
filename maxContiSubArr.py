def maxContigousSubArr(arr):
    maxVal = float("-inf")
    currSum = arr[0]
    #print arr[1:]
    for a in arr[1:]:
        maxVal = max(maxVal, currSum)
        currSum += a
        if currSum < 0:
            currSum = a
    maxVal = max(maxVal, currSum)
    return maxVal

print maxContigousSubArr([-1, -2, -3, -4])
print maxContigousSubArr([1, 2, 3])
