# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # On LeeCode site: Time Limit Exceeded on submitting:
        # zeros = 0
        # i = 0
        # for item in nums:
        #     if not item:
        #         zeros += 1
        # while zeros:
        #     if not nums[i]:
        #         zeros -= 1
        #         for j in range(i + 1, len(nums)):
        #             nums[j], nums[j - 1] = nums[j - 1], nums[j]
        #     else:
        #         i += 1

        # Accepted (More pythonic way :))
        # Комментарий: Удаление из массива - линейное. Много удалений и будет уже квадратичное время.
        # Посмотри оптимальное решение здесь: https://pastebin.com/301eeKMR
        # zeros_count = 0
        # while 0 in nums:
        #     nums.remove(0)
        #     zeros_count += 1
        # while zeros_count:
        #     nums.append(0)
        #     zeros_count -= 1

        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        while index < len(nums):
            nums[index] = 0
            index += 1
