# ═══════════════════════════════════════════════════════
#  Problem  : 0013. Roman to Integer
#  URL      : https://leetcode.com/problems/roman-to-integer/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : July 17, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        num = 0
        flag = False
        
        for i in range(n) :
            if flag :
                flag = False 
                continue

            if s[i] == 'M' :
                num += 1000

            if s[i] == 'D' :
                num += 500

            if s[i] == 'C' :
                if i<n-1 :
                    if s[i+1] == 'M' :
                        num += 900
                        flag = True
                    elif s[i+1] == 'D' :
                        num += 400
                        flag = True
                num += 100

            if s[i] == 'L' :
                num += 50

            if s[i] == 'X' :
                if i<n-1 :
                    if s[i+1] == 'C' :
                        num += 90
                        flag = True
                    elif s[i+1] == 'L' :
                        num += 40
                        flag = True
                num += 10

            if s[i] == 'I' :
                if i<n-1 :
                    if s[i+1] == 'X' :
                        num += 9
                        flag = True
                    elif s[i+1] == 'V' :
                        num += 4
                        flag = True
                num += 1
                
        return num
