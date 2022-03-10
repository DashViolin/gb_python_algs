from typing import List


# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicatePythonic(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicateByDict(self, nums: List[int]) -> bool:
        distinct = {}
        for num in nums:
            distinct.setdefault(num, None)
        return len(nums) != len(distinct)

    def containsDuplicate(self, nums: List[int]) -> bool:
        prev = None
        for num in sorted(nums):
            if num == prev:
                return True
            prev = num
        return False
