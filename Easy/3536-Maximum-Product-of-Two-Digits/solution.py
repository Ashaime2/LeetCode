# ═══════════════════════════════════════════════════════
#  Problem  : 3536. Maximum Product of Two Digits
#  URL      : https://leetcode.com/problems/maximum-product-of-two-digits/?envType=daily-question&envId=2026-07-30
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : July 31, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        a, b = 0, 0

        for char in n :
            a = min(char, a)
            b = max(char, b)
        return a*b

        
        