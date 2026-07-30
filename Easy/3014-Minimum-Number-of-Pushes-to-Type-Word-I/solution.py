# ═══════════════════════════════════════════════════════
#  Problem  : 3014. Minimum Number of Pushes to Type Word I
#  URL      : https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/submissions/2088084352/?envType=daily-question&envId=2026-07-30
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : July 31, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def minimumPushes(self, word):
        n = len(word)

        if n <= 8:
            return n

        if n <= 16:
            return 8 + (n - 8) * 2

        if n <= 24:
            return 8 + 16 + (n - 16) * 3

        return 8 + 16 + 24 + (n - 24) * 4