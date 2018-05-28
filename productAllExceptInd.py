def findProductWithoutDiv(arr):
    prodTill = [1]
    for i in xrange(1, len(arr)):
        prodTill.append(prodTill[-1] * arr[i-1])
    prodTillNow = arr[-1]
    for i in xrange(len(arr) - 2, -1, -1):
        prodTill[i] = prodTillNow * prodTill[i]
        prodTillNow *= arr[i]
    return prodTill

def findProductWithDiv(arr):
    productWithoutZero = 1
    product = 1
    zeroCount = 0
    for a in arr:
        product *= a
        productWithoutZero *= (1 if a == 0 else a)
        zeroCount += (1 if a == 0 else 0)
        if zeroCount > 1:
            return [0] * len(arr)
    for i, a in enumerate(arr):
        arr[i] = product/a if a != 0 else productWithoutZero
    return arr

print findProductWithoutDiv([1, 2, 3])
print
print findProductWithDiv([1, 2, 3])
print 
print findProductWithoutDiv([1, 2, 0, 1])
print 
print findProductWithDiv([1, 2, 0, 1])
