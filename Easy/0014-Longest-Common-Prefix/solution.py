# ═══════════════════════════════════════════════════════
#  Problem  : 0014. Longest Common Prefix
#  URL      : https://leetcode.com/problems/longest-common-prefix/submissions/2070454257/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : July 17, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        strs = sorted(strs, key=len)

        string = ''
        for  i in range(len(strs[0])):
            test = strs[0][i]
            for elt in strs :
                if elt[i]!=test :
                    return string
            string += test
        return string


