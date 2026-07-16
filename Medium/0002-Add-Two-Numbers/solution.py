# ═══════════════════════════════════════════════════════
#  Problem  : 0002. Add Two Numbers
#  URL      : https://leetcode.com/problems/add-two-numbers/submissions/2070108343/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 8 ms
#  Memory   : 12.6 MB
#  Solved   : July 16, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        noeud = ListNode(0)
        courant = noeud
        retenue = 0

        while l1 or l2 or retenue :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            somme = x+y+retenue
            chiffre = somme%10
            retenue = somme//10
            courant.next = ListNode(chiffre)
            courant = courant.next

            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next
        return noeud.next