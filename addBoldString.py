class trieNode(object):
    def __init__(self, val=None):
        self.val = None
        self.wordEnd = False
        self.children = {}


def addToTrie(trieHead, word):
    temp = trieHead
    for w in word:
        if temp.children.get(w, None) is None:
            temp.children[w] = trieNode(w)
        temp = temp.children[w]
    temp.wordEnd = True

def addBoldStrings(s, wordList):
    trieHead = trieNode()
    for w in wordList:
        addToTrie(trieHead, w)

    stInd, endInd = None, None
    i = 0
    s = list(s)
    ranges = []
    while i < len(s):
        tempNode = trieHead
        if tempNode.children.get(s[i], None) is not None:
            j = i
            tempStInd = j
            if endInd is not None and endInd < j:
                ranges.append((stInd, endInd))
                endInd = None
                stInd = None
            else:
                tempStInd = j if stInd is None else stInd
            while j < len(s) and tempNode.children.get(s[j], None) is not None:
                tempNode = tempNode.children[s[j]]
                j += 1
            if tempNode.wordEnd:
                endInd = j
                stInd = tempStInd if stInd is None else stInd
            else:
                tempStInd = None
        i += 1
    if stInd is not None and endInd is not None:
        ranges.append((stInd, endInd))
    print ranges
    for ran in reversed(ranges):
        s.insert(ran[1], '</b>')
        s.insert(ran[0], '<b>')
    return ''.join(s)

print addBoldStrings('abcxyz123', ["abc","123"])
print addBoldStrings('aaabb123', ["aaa", "aab"])
print addBoldStrings('aaaaa', ["a"])
print addBoldStrings('', ["aba", "123"])
print addBoldStrings('12345678', ["123", "456"])
print addBoldStrings('xhhjzbkvpmasiypsqqjobufcqmlhdjffrdohsxgksftaekzhwzydhbfdiylihnvjlvpoptnqigszckimljbepgisnmyszfsxkxyfdfqngytfuihepohapvhbyhqydvroflfnsyjmygtykdejfudrhxxawcewgiguiwsvqrgbxrbdnrvguzjftqcsjbvjlbxfsvzpdpmtlzobwnxrtgisbcqmhugncjwgatfctydryakvbnmlbiftndfefylsmlebzdumefuflwhtwijtrhhhmknklalgqjaoicmnywtvzldbeftkydjsdkkonayhdxhrjazosqloilagcwzeezavnsqelxqhtlzymedxmkrovxhkrgfenyhxgdroeejedbwpnkqbqknalwgxoxweyxngorvrpnfkvagdqkbtuayaihyhwcsdtjzzvxfavrhzgf', ["xh","hj","zb","kv","pm","as","iy","ps","qq","jo","bu","fc","qm","lh","dj","ff","rd","oh","sx","gk","sf","ta","ek","zh","wz","yd","hb","fd","li","hn","vj","lv","po","pt","nq","ig","sz","ck","im","lj","be","pg","is","nm","ys","zf","kx"])
print addBoldStrings('abc1234', ["abc", "234"])
