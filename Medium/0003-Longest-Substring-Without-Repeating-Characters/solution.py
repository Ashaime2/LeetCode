# ═══════════════════════════════════════════════════════
#  Problem  : 0003. Longest Substring Without Repeating Characters
#  URL      : https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2071031535/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 421 ms
#  Memory   : 12.6 MB
#  Solved   : July 17, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longueur_max = 0
        idx = 0

        while idx < len(s):
            fenetre = ""
            i = idx

            while i < len(s) and s[i] not in fenetre:
                fenetre += s[i]
                i += 1

            longueur_max = max(longueur_max, len(fenetre))
            idx += 1

        return longueur_max