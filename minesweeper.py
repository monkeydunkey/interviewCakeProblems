'''
My implementation of mine sweeper

in map -1 maps the position of the mine
'''
import random

class mineSweeper(object):
    '''
    Possible game States
    'Victory': found all the mines
    'Lost': Landed on a mine
    'Progress': Game is in progress
    '''
    def __init__(self, height, width, percentMine):
        self.mineMap = [[0 for x in xrange(width)] for y in xrange(height)]
        self.visibilityMap = [[0 for x in xrange(width)] for y in xrange(height)]
        self.totalPositions = height * width
        self.mines = int(height * width * percentMine)
        self.state = 'Progress'
        self.height = height
        self.width = width
        # Placing the mines on the map
        for mine in xrange(self.mines):
            oldPos = True
            while oldPos:
                position_h, position_w  = int(random.random() * height), int(random.random() * width)
                oldPos = not (self.mineMap[position_h][position_w] == 0)
            self.mineMap[position_h][position_w] = -1
            for x in range(-1, 2):
                if position_w + x >= 0 and position_w + x < width:
                    for y in range(-1, 2):
                        if y == 0 and x == 0:
                            continue
                        if position_h + y >= 0 and position_h + y < height:
                            #print self.mineMap[h + y][w + x], h + y, w + x, (1 if self.mineMap[h + y][w + x] == -1 else 0)
                            self.mineMap[position_h + y][position_w + x] += 1

    def getState(self):
        return self.state

    def explore(self, position):
        x, y = position
        if self.mineMap[y][x] == -1:
            self.state = 'Lost'
            return
        # Now the user did not step on a mine time to make the neighbour cells visible
        # A possible way to do that will be implement this is to use breadth first search
        queue = [(x, y)]
        while len(queue):
            x, y = queue.pop(0)
            self.visibilityMap[y][x] = 1
            for i in range(-1, 2):
                if x + i > 0 and x + i < self.width:
                    for z in range(-1, 2):
                        if i == 0 and z == 0:
                            continue
                        if y + z > 0 and y + z < self.height:
                            if self.mineMap[y + z][x + i] == 0 and self.visibilityMap[y + z][x + i] == 0:
                                queue.append((x + i, y + z))
                            elif self.mineMap[y + z][x + i] != -1:
                                self.visibilityMap[y + z][x + i] = 1

    def printMap(self):
        #this function prints the map on the terminal
        print '\n\n'
        for y in xrange(self.height):
            rowStr = []
            for x in xrange(self.width):
                rowStr.append(str(self.mineMap[y][x]) if self.visibilityMap[y][x] == 1 else '-')
            print ' '.join(rowStr)

if __name__ == '__main__':
    inputCorrect = True
    try:
        height = input('height of the map: ')
        width = input('width of the map: ')
        minePercentage = float(raw_input('percentage mines: '))
    except Exception as e:
        print 'Input is not of correct format', e
        inputCorrect = False
    if inputCorrect:
        ms = mineSweeper(height, width, minePercentage)
        while ms.state == 'Progress':
            print 'going to loop'
            ms.printMap()
            validateInput = False
            while not validateInput:
                inp = raw_input('Provide position to check in comma seprated format: ')
                if len(inp.split(',')) > 2:
                    print 'More than 2 values provide. Please provide correct input'
                    continue
                try:
                    x, y = map(lambda x: int(x.strip()), inp.split(','))
                    if x < 0 or x > width or y < 0 or y > height:
                        print 'Invalid coordinates provided'
                        continue
                except Exception as e:
                    print 'Invalid coordinates provided', e
                    continue
                validateInput = True
            ms.explore((x, y))
        if ms.state == 'Victory':
            print 'Congrats you won the game'
        else:
            print 'You stepped on a mine. Better luck next time'
