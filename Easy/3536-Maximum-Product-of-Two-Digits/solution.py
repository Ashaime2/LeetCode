# ═══════════════════════════════════════════════════════
#  Problem  : 3536. Maximum Product of Two Digits
#  URL      : https://leetcode.com/problems/maximum-product-of-two-digits/?envType=daily-question&envId=2026-07-30
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : July 31, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        p = len(n)
        compteur = 0
        for i in range(p) :
            for j in range(p) :
                if i != j :
                    compteur = max(compteur, i*j)
        return compteur
        
        