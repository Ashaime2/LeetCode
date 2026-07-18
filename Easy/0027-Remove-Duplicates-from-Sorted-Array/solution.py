# ═══════════════════════════════════════════════════════
#  Problem  : 0027. Remove Duplicates from Sorted Array
#  URL      : https://leetcode.com/problems/remove-element/description/
#  Difficulty : Easy
#  Language : python
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