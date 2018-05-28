'''
Queue using 2 stacks such that m calls take O(m) runtime
'''

class queue(object):
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, val):
        self.st1.append(val)

    def pop(self, val):
        if len(self.st2) == 0:
            while len(self.st1):
                self.st2.append(self.st1.pop())
        return st2.pop() if len(st2) > 0 else None



