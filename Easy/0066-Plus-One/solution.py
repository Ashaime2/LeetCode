# ═══════════════════════════════════════════════════════
#  Problem  : 0066. Plus One
#  URL      : https://leetcode.com/problems/plus-one/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : July 24, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        if digits[-1] != 9 :
            digits[-1] += 1
            return digits
        
        for i in range(n) :
            piv = digits[-(i+1)]
            if piv == 9 :
                piv = 0
            else :
                piv += 1
                return digits

        return [1] + digits