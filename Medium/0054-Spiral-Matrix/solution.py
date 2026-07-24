# ═══════════════════════════════════════════════════════
#  Problem  : 0054. Spiral Matrix
#  URL      : https://leetcode.com/problems/spiral-matrix/submissions/2079616403/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : July 24, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        L = []
        vus = {}
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m) :
            for j in range(n) :
                vus[(i,j)] = 0

        i, j = 0,0
        proch = (i,j)
        direction = 'd'

        while len(L) < m * n:
            if direction == 'd' :
                while j < n and vus[(i,j)] == 0 :
                    L.append(matrix[i][j]) 
                    vus[(i,j)] = 1
                    j += 1
                i += 1
                j -= 1
                proch = (i,j)
                direction = 'b'
            elif direction == 'b' :
                while i < m and vus[(i,j)] == 0 :
                    L.append(matrix[i][j]) 
                    vus[(i,j)] = 1
                    i += 1
                j -= 1
                i -= 1
                proch = (i,j)
                direction = 'g'
            elif direction == 'g' :
                while j >= 0 and vus[(i, j)] == 0 :
                    L.append(matrix[i][j]) 
                    vus[(i,j)] = 1
                    j -= 1
                i -= 1
                j += 1
                proch = (i,j)
                direction = 'h'
            elif direction == 'h' :
                while i >= 0 and vus[(i, j)] == 0 :
                    L.append(matrix[i][j]) 
                    vus[(i,j)] = 1
                    i -= 1
                j += 1
                i += 1
                proch = (i,j)
                direction = 'd'

        return L
            
