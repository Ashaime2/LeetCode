# ═══════════════════════════════════════════════════════
#  Problem  : 0019. Remove Nth Node From End of List
#  URL      : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 4 ms
#  Memory   : 12.4 MB
#  Solved   : July 18, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def removeNthFromEnd(self, head, n):
        node = head
        length = 0

        while node:
            length += 1
            node = node.next

        # Remove the first node
        if n == length:
            return head.next

        node = head
        for _ in range(length - n - 1):
            node = node.next

        node.next = node.next.next

        return head