# ═══════════════════════════════════════════════════════
#  Problem  : 0069. Sqrt(x)
#  URL      : https://leetcode.com/problems/sqrtx/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : July 24, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return abs(floor(x ** 0.5))
        