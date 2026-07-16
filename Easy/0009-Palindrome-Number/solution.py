# ═══════════════════════════════════════════════════════
#  Problem  : 0009. Palindrome Number
#  URL      : https://leetcode.com/problems/palindrome-number/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : July 17, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        n = len(num)
        for i in range(n//2) :
            if num[i]!=num[-i] :
                return False
        return True