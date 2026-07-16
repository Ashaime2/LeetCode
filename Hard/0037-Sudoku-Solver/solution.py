# ═══════════════════════════════════════════════════════
#  Problem  : 0037. Sudoku Solver
#  URL      : https://leetcode.com/problems/sudoku-solver/
#  Difficulty : Hard
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : July 17, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def loc_square(i, j):
            return (i // 3) * 3, (j // 3) * 3

        
        def verif_ligne(num, i):
            return num not in board[i]

        def verif_col(num, j):
            return all(board[row][j] != num for row in range(9))

        def verif_square(num, i, j) :
            k,l = loc_square(i,j)
            square = [x for row in board[k:k+3] for x in row[l:l+3]]
            if num in square :
                return False
            return True
        
        dico = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    dico[(i, j)] = {board[i][j]}
                else:
                    dico[(i, j)] = set()
                    for num in map(str, range(1, 10)):
                        if (verif_ligne(num, i) and verif_col(num, j) and verif_square(num, i, j)):
                            dico[(i, j)].add(num)

        def verif_case(num, i, j) :
            if verif_ligne(num, i) and verif_col(num, j) and verif_square(num, i, j) and board[i][j] == ".":
                dico[(i,j)].add(num)
            if board[i][j] != "." :
                dico[(i,j)].add(board[i][j])

        for num in range(1,10) :
            for i in range(9) :
                for j in range(9) :
                    verif_case(str(num),i,j)

        def eliminer(num, i, j) :
            for k in range(9) :
                dico[(k,j)].discard(num)
                dico[(i,k)].discard(num)
            k,l = loc_square(i,j)
            for a in range(3) :
                for b in range(3) :
                    dico[(k+a,l+b)].discard(num)

        def attribuer(num, i, j):
            if board[i][j] != ".":
                return False
            board[i][j] = num
            eliminer(num, i, j)
            dico[(i, j)] = {num}
            return True

        def solveur():
            while any("." in row for row in board):
                modification = False

                # Une seule possibilité dans une case
                for key in dico:
                    i, j = key

                    if len(dico[key]) == 1 and board[i][j] == ".":
                        num = next(iter(dico[key]))
                        if attribuer(num, i, j) :
                            modification = True

                # Un chiffre possible dans une seule case d'une ligne
                for i in range(9):
                    for num in map(str, range(1, 10)):
                        positions = [(i, j) for j in range(9) if num in dico[(i, j)] and board[i][j] == "."]
                        if len(positions) == 1:
                            row, col = positions[0]
                            if attribuer(num, row, col) :
                                modification = True

                # Un chiffre possible dans une seule case d'une colonne
                for j in range(9):
                    for num in map(str, range(1, 10)):
                        positions = [(i, j) for i in range(9) if num in dico[(i, j)] and board[i][j] == "."]
                        if len(positions) == 1:
                            row, col = positions[0]
                            attribuer(num, row, col)
                            if attribuer(num, row, col) :
                                modification = True

                # Un chiffre possible dans une seule case d'un carré
                for i in range(3) :
                    for j in range(3):
                        for num in map(str, range(1,10)):
                            positions = []
                            for k in range(3):
                                for l in range(3):
                                    if num in dico[(i*3+k,j*3+l)] and board[i * 3 + k][j * 3 + l] == "." :
                                        positions.append((i*3+k,j*3+l))
                            if len(positions) == 1 :
                                row, col = positions[0]
                                if attribuer(num, row, col) :
                                    modification = True
                        

                if not modification:
                    break