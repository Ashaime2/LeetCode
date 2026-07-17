# ═══════════════════════════════════════════════════════
#  Problem  : 0017. Letter Combinations of a Phone Number
#  URL      : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : July 18, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dico = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['u','t','v'],
            '9' : ['y','z','w','x'],
        }

        n = len(digits)
        sept = digits.count('7')
        neuf = digits.count('9')
        res = [''] * 3**(n-sept-neuf) * 4 ** (sept+neuf)

        for char in digits :
            i = 0
            if char == '7' or char == '9' :
                while i < n/4 :
                    res[i] += dico[char][0]
                    i += 1
                while i < 2*(n/4) :
                    res[i] += dico[char][1]
                    i += 1
                while i < 3*(n/4) :
                    res[i] += dico[char][2]
                    i += 1
                while i < n :
                    res[i] += dico[char][3]
                    i += 1
            else :
                while i < n/3 :
                    res[i] += dico[char][0]
                    i += 1
                while i < 2*(n/3) :
                    res[i] += dico[char][1]
                    i += 1
                while i < n :
                    res[i] += dico[char][2]
                    i += 1
        return res


