class node(object):
    def __init__(self, value):
        self.value = value
        self.count = 0
        self.children = [None] * 26

class trie(object):
    def __init__(self):
        self.head = node(None)

    def addString(self, st):
        temp = self.head
        for c in st:
            ind = ord(c) - ord('a')
            temp.count += 1
            if temp.children[ind] is None:
                temp.children[ind] = node(c)
            temp = temp.children[ind]

        temp.count += 1
    #this is specific to getting a prefix for a string
    def getPrefix(self, st):
        temp = self.head
        prefix = ''
        for c in st:
            ind = ord(c) - ord('a')
            if temp.count == 1:
                if temp == self.head:
                    prefix += c
                break
            if temp.children[ind] is None:
                return 'The string was not in trie yet'
            
            temp = temp.children[ind]
            prefix += c
        return prefix


if __name__ == '__main__':
    t1 = trie()
    t1.addString('testa')
    print t1.getPrefix('testa')

    t1.addString('testb')
    print t1.getPrefix('testb')

    t2 = trie()
    li = ["zebra", "dog", "duck", "dove"]
    for l in li:
        t2.addString(l)
    for i in li:
        print t2.getPrefix(i)



