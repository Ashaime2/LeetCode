# ═══════════════════════════════════════════════════════
#  Problem  : 0020. Valid Parentheses
#  URL      : https://leetcode.com/problems/valid-parentheses/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : July 17, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ouvrants = ['(' , '[', '{']
        pile = [] 
        for char in s :
            if char in ouvrants :
                pile.append(char)
            else :
                if len(pile) == 0 :
                    return False
                if not pile.pop() == char :
                    return False
        if len(pile) == 0 :
            return True
        else : 
            return False
