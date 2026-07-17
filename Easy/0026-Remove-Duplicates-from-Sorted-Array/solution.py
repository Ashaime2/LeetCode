# ═══════════════════════════════════════════════════════
#  Problem  : 0026. Remove Duplicates from Sorted Array
#  URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/2071623345/
#  Difficulty : Easy
#  Language : Python
#  Runtime  : 0 ms
#  Memory   : 13.7 MB
#  Solved   : July 18, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1