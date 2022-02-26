# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # def make_iteration(s: list[str], index: int):
        #     if index == round(len(s)):
        #         return
        #     s[index], s[len(s) - index - 1] = s[len(s) - index - 1], s[index]
        #     make_iteration(s, index + 1)
        # make_iteration(s, 0)

        for i in range(round(len(s) / 2)):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
