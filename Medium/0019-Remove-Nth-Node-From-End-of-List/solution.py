# ═══════════════════════════════════════════════════════
#  Problem  : 0019. Remove Nth Node From End of List
#  URL      : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 12.6 MB
#  Solved   : July 18, 2026
# ═══════════════════════════════════════════════════════

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head.next == None :
            return head
        node = head
        compteur = 0
        while node != None :
            compteur += 1
            node = node.next
        node = head
        for i in range(compteur-n-1):
            node = node.next
        bon = node
        effacer = node.next
        raccord = effacer.next
        bon.next = raccord
        return head

        