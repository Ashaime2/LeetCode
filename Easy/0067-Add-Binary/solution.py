# ═══════════════════════════════════════════════════════
#  Problem  : 0067. Add Binary
#  URL      : https://leetcode.com/problems/add-binary/submissions/2078691041/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 16 ms
#  Memory   : 12.2 MB
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
                if int(a[-(i+1)]) + int(b[-(i+1)]) == 0 :
                    s = '1' + s
                    retenue = 0
                elif int(a[-(i+1)]) + int(b[-(i+1)]) == 1 :
                    retenue = 1
                    s = '0' + s
                elif int(a[-(i+1)]) + int(b[-(i+1)]) == 2 :
                    retenue = 1
                    s = '1' + s
            else :
                if int(a[-(i+1)]) + int(b[-(i+1)]) < 2 :
                    s = str(int(a[-(i+1)]) + int(b[-(i+1)])) + s
                else :
                    retenue = 1
                    s = '0' + s

        if retenue == 1 :
            s = '1' + s
        
        return s
