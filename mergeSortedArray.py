def mergeSortedArray(l1, l2):
    i, j = 0, 0
    combinedArr = []
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            combinedArr.append(l2[j])
            j += 1
        else:
            combinedArr.append(l1[i])
            i += 1
    if i == len(l1):
        combinedArr.extend(l2[j:])
    else:
        combinedArr.extend(l1[i:])

    return combinedArr


def mergeSortedArrays(arrLi):
    i = [0 for x in arrLi]
    combinedArr = []
    totalLength = reduce(lambda x, y: (x if type(x) == type(1) else len(x)) + len(y), arrLi)
    while sum(i) < totalLength:
        currMin = float("inf")
        incrementInd = -1
        for k, j in enumerate(i):
            if j < len(arrLi[k]):
                if currMin > arrLi[k][j]:
                    currMin = arrLi[k][j]
                    incrementInd = k
        combinedArr.append(currMin)
        i[incrementInd] += 1
    return combinedArr



if __name__ == '__main__':
    arr1 = map(lambda x: int(x), raw_input().split())
    arr2 = map(lambda x: int(x), raw_input().split())
    print(mergeSortedArray(arr1, arr2))
    print(mergeSortedArrays( [arr1, arr2, [3, 5, 78] ] ))
