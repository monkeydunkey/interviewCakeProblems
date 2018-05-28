if __name__ == '__main__':
    def buildRecurseSquare(completedMat, startmap):
        print 'HI'
        if len(completedMat) == len(completedMat[0]):
            # we have a square matrix
            return [completedMat]
        outLi = []
        currLength = len(completedMat)
        wordToLook = completedMat[0][currLength]
        print wordToLook, startmap[ord(wordToLook) - ord('a')]
        for w in startmap[ord(wordToLook) - ord('a')]:
            print w
            i = 0
            cand = True
            while i < currLength:
                if w[i] != completedMat[i][currLength]:
                    cand = False
                    break
                i += 1
            if cand:
                outLi.extend(buildRecurseSquare(completedMat + [w], startmap))
        return outLi


    def wordSquares(words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        startmap = [[] for x in xrange(26)]
        for w in words:
            startmap[ord(w[0]) - ord('a')].append(w)
        possibleSquares = []
        for w in words:
            possibleSquares.extend(buildRecurseSquare([w], startmap))
            print possibleSquares
        return possibleSquares

    print wordSquares(["area","lead","wall","lady","ball"])
