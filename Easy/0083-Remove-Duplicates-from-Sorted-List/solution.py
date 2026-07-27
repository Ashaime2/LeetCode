# ═══════════════════════════════════════════════════════
#  Problem  : 0083. Remove Duplicates from Sorted List
#  URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/2083402890/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 3 ms
#  Memory   : 12.3 MB
#  Solved   : July 27, 2026
# ═══════════════════════════════════════════════════════

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head :
            return head
        if head.next == None :
            return head 

        actuel = head
        while actuel.next is not None : 
            if actuel.val == actuel.next.val :
                actuel.next = actuel.next.next
            else :
                actuel = actuel.next
        return head