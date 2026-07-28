# ═══════════════════════════════════════════════════════
#  Problem  : 0155. Min Stack
#  URL      : https://leetcode.com/problems/min-stack/submissions/2085045006/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 200 ms
#  Memory   : 24.9 MB
#  Solved   : July 28, 2026
# ═══════════════════════════════════════════════════════

class MinStack(object):

    def __init__(self):
        self.liste = []
        self.minimums = []

    def push(self, value):
        self.liste.append(value)

        if not self.minimums:
            self.minimums.append(value)
        else:
            self.minimums.append(min(value, self.minimums[-1]))

    def pop(self):
        self.liste.pop()
        self.minimums.pop()

    def top(self):
        return self.liste[-1]

    def getMin(self):
        return self.minimums[-1]