
def findkth(encoded, k):
    currStr = ''
    tempStr = ''
    freq = ''
    totalCount = 0
    for i in encoded:
        if i.isdigit():
            freq += i
        else:
            if len(freq) > 0:
                counts = int(freq)
                if totalCount + counts * len(currStr) >= k:
                    #we have the get the kth instance now
                    return (currStr * counts)[k - totalCount - 1]
                totalCount += (counts * len(currStr))
                currStr = ''
                freq = ''
            currStr += i
    if len(freq) > 0:
        counts = int(freq)
        if totalCount + counts * len(currStr) >= k:
            #we have the get the kth instance now
            return (currStr * counts)[k - totalCount - 1]
    return 'dencrypted string has length less than k'


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    print findkth('a2b2c3', 5)
    print findkth('ab4c2ed3', 9)
    print findkth('ab4c12ed3', 21)
