#code
def maxLeftSubArray(arr):
    maxVal,currSum = arr[0], arr[0]
    leftArr = [arr[0]]
    for n in arr[1:]:
        currSum = max(n, currSum + n)
        maxVal = max(currSum, maxVal)
        leftArr.append(maxVal)
    return leftArr
    
def maxRightSubArray(arr):
    maxVal,currSum = arr[-1], arr[-1]
    rightArr = [arr[-1]]
    for n in reversed(arr[:-1]):
        currSum = max(n, currSum + n)
        maxVal = max(currSum, maxVal)
        rightArr.insert(0, maxVal)
    return rightArr
    
def maxAbsDiff(arr):
    aLMax = maxLeftSubArray(arr)
    aRMax = maxRightSubArray(arr)
    aLMin = maxLeftSubArray(list(map(lambda x: -1*x, arr)))
    aRMin = maxRightSubArray(list(map(lambda x: -1*x, arr)))
    maxDiff = float("-inf")
    for i in range(len(arr)):
        if i == 0:
            val1 = abs(aRMax[i+1] - aLMin[i])
            val2 = abs(aRMax[i] - 0)
        elif i == len(arr):
            val1 = abs(0 - aLMin[i])
            val2 = abs(aRMax[i+1] - aLMin[i])
        else:
            val1 = abs(aRMax[i+1] - aLMin[i])
            val2 = abs(aRMax[i+1] - aLMin[i])
        maxDiff = max(maxDiff, val1, val2)
    return maxDiff



print maxAbsDiff([-2, -3, 4, -1, -2, 1, 5, -3])
