import random
def randomShuffle(arr):
    for i in xrange(len(arr)):
        j = random.randint(i, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    print randomShuffle([1,2,3])
