def maxSpan(arr):
    occList = {}
    maxspan = 0
    for i, a in enumerate(arr):
        if a in occList:
            occList[a][1] = i
            maxspan = max(maxspan, i - occList[a][0] + 1)
        else:
            occList[a] = [i, i]
    return maxspan


if __name__ == '__main__':
    print maxSpan([1, 2, 1, 1, 3])
    print maxSpan([1, 4, 2, 1, 4, 1, 4])
    print maxSpan([1, 4, 2, 1, 4, 4, 4])
