# ═══════════════════════════════════════════════════════
#  Problem  : 0155. Min Stack
#  URL      : https://leetcode.com/problems/min-stack/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : July 28, 2026
# ═══════════════════════════════════════════════════════

class MinStack(object):

    def __init__(self):
        self.liste = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.liste.append(value)
        

    def pop(self):
        """
        :rtype: None
        """
        self.liste = self.liste[::-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.liste[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.liste)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()