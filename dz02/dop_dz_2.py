# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # if n % 2 != 0 or n <= 0:
        #     return False
        # return self.isPowerOfTwo(n / 2)

        # if n >= 0 and bin(n).count('1') == 1:
        #     return True
        # return False

        return (n & (n - 1) == 0) and n != 0
