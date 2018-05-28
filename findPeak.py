def findPeak(arr, left, right):
    if left + 1 >= right:
        return left if arr[left] > arr[right] else right
        
    mid = (left + right) // 2
    if arr[mid] <= arr[mid + 1]:
        return findPeak(arr, mid + 1, right)
    elif arr[mid] <= arr[mid - 1]:
        return findPeak(arr, left, mid - 1)
    return mid



print findPeak([1,2,3,4,5,6], 0, 5)
print findPeak([1,2,1,4,5,7], 0, 5)
print findPeak([1,5,4,3,5,7], 0, 5)
print findPeak([1,2,5,3,6,7], 0, 5)
