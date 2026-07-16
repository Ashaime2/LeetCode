# ═══════════════════════════════════════════════════════
#  Problem  : 0074. Search a 2D Matrix
#  URL      : https://leetcode.com/problems/search-a-2d-matrix/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : July 16, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target in matrix :
            return True
        else :
            return False