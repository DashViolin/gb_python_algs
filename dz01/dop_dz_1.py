# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != last:
                last = nums[i]
                nums[k] = nums[i]
                k += 1
        return k
