# ═══════════════════════════════════════════════════════
#  Problem  : 0036. Valid Sudoku
#  URL      : https://leetcode.com/problems/valid-sudoku/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : July 16, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Row verif :
        for L in board :
            if not len(L) == len(set(L)) :
                return False
        
        # Col verif :
        for i in range(9) :
            if not len(board[:][i]) == len(set(board[:][i])) :
                return False

        # Square verif :
        for i in range(3) :
            for j in range(3) :
                square = [x for row in matrix[i:i+3] for x in row[j:j+3]]
                if not len(square) == len(set(square)) :
                    return False
        
        return True