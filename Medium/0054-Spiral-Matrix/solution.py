# ═══════════════════════════════════════════════════════
#  Problem  : 0054. Spiral Matrix
#  URL      : https://leetcode.com/problems/spiral-matrix/
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

        while (i<m) and (j<n) and vus[proch] == 0 :
            if direction == 'd' :
                while i < m -1 and vus[(i,j)] == 0 :
                    L.append(matrix[i][j]) 
                    vus[(i,j)] = 1
                    i += 1
                j += 1
                proch = (i,j)
                direction = 'b'
            elif direction == 'b' :
                while j < n -1 and vus[(i,j)] == 0 :
                    L.append(matrix[i][j]) 
                    vus[(i,j)] = 1
                    j += 1
                i -= 1
                proch = (i,j)
                direction = 'g'
            elif direction == 'g' :
                while i > 0 and vus[(i,j)] == 0 :
                    L.append(matrix[i][j]) 
                    vus[(i,j)] = 1
                    i -= 1
                j -= 1
                proch = (i,j)
                direction = 'h'
            if direction == 'h' :
                while j > 0 and vus[(i,j)] == 0 :
                    L.append(matrix[i][j]) 
                    vus[(i,j)] = 1
                    j -= 1
                i += 1
                proch = (i,j)
                direction = 'd'

        return L
            
