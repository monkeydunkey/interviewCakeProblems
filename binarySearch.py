def template1(arr, left, right, target):
    if left > right:
        return -1
    mid = left + (right - left)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return template1(arr, left, mid -1, target)
    else:
        return template1(arr, mid + 1, right, target)

def binaryInsert(arr, left, right, target):
    if left >= right:
        return left if arr[left] > target else left + 1
    mid = left + (right - left) /2 
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binaryInsert(arr, left, mid - 1, target)
    else:
        return binaryInsert(arr, mid + 1, right, target)

def rangeSearch(arr, left, right, target, first):
    if left + 1 >= right:
        if first:
            return left if arr[left] == target else right if arr[right] == target else -1
        return right if arr[right] == target else left if arr[left] == target else -1
    mid = (left + right)/2
    if first:
        if arr[mid] >= target:
            return rangeSearch(arr, left, mid, target, first)
        return rangeSearch(arr, mid + 1, right, target, first)
    else:
        if arr[mid] > target:
            return rangeSearch(arr, left, mid - 1, target, first)
        return rangeSearch(arr, mid, right, target, first)



if __name__ == '__main__':
    print template1([1,2,3,4,5,6], 0, 5, 1)
    print binaryInsert([3, 5, 7], 0, 2, 0)
    print binaryInsert([3, 5, 7], 0, 2, 8)
    arr = [1,1,1,1,1,1,1,1]
    print 'Start position: ', rangeSearch(arr, 0, len(arr) - 1, 1, True)
    print 'End position: ', rangeSearch(arr, 0, len(arr) - 1, 1, False)
    arr = [1,1, 2, 2, 2, 4, 5, 6, 7, 8, 8, 9, 9]
    print 'Start position: ', rangeSearch(arr, 0, len(arr) - 1, 2, True)
    print 'End position: ', rangeSearch(arr, 0, len(arr) - 1, 2, False)
