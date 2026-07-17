# ═══════════════════════════════════════════════════════
#  Problem  : 0013. Roman to Integer
#  URL      : https://leetcode.com/problems/roman-to-integer/submissions/2071084414/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 9 ms
#  Memory   : 12.4 MB
#  Solved   : July 17, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        n = len(s)

        dico = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
        }

        flag = False

        for i in range(n) :
            if flag :
                flag = False
                continue

            if i < n-1 :
                if dico[s[i]] < dico[s[i+1]] :
                    num += dico[s[i+1]] - dico[s[i]]
                    flag = True
                    continue
                    
            num += dico[s[i]]
        
        return num