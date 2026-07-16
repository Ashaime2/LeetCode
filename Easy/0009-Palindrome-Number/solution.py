# ═══════════════════════════════════════════════════════
#  Problem  : 0009. Palindrome Number
#  URL      : https://leetcode.com/problems/palindrome-number/submissions/2070448280/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 11 ms
#  Memory   : 12.2 MB
#  Solved   : July 17, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]