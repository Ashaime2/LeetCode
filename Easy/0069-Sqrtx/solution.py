# ═══════════════════════════════════════════════════════
#  Problem  : 0069. Sqrt(x)
#  URL      : https://leetcode.com/problems/sqrtx/submissions/2079687409/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : July 24, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(abs(floor(x ** 0.5)))
        