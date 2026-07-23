# ═══════════════════════════════════════════════════════
#  Problem  : 0067. Add Binary
#  URL      : https://leetcode.com/problems/add-binary/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : July 23, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        retenue = 0
        s = ''

        n = len(a)
        m = len(b)

        if m != n :
            if n > m :
                b = '0' * (n-m) + b
            else :
                a = '0' * (m-n) + a

        for i in range(len(a)) :
            if retenue == 1 :
                if int(a[-i]) + int(b[-i]) == 0 :
                    s = '1' + s
                elif int(a[-i]) + int(b[-i]) == 1 :
                    retenue = 1
                    s = '0' + s
                elif int(a[-i]) + int(b[-i]) == 1 :
                    retenue = 1
                    s = '1' + s
            else :
                if int(a[-i]) + int(b[-i]) < 2 :
                    s = str(int(a[-i] + b[-i])) + s
                else :
                    retenue = 1
                s = '0' + s

        if retenue == 1 :
            s = '1' + s
        
        return s
