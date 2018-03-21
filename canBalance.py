def canBalance(arr):
    # if we are dealing only with integers then the a simpler rejection can be whether sum is odd or not
    arrSum = sum(arr)
    balSum = 0
    for a in arr:
        balSum += a
        if balSum * 2 == arrSum:
            return True

    return False

if __name__ == '__main__':
    print canBalance([1, 1, 1, 2, 1])
    print canBalance([2, 1, 1, 2, 1])
    print canBalance([10, 10])
