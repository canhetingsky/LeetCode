#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1]
        for i in range(1, n):
            fac.append(fac[-1] * i)  # a list [1, 1, 2, 6..., (n-1)!]

        res = ''
        nums = list(range(1, n + 1))  # a list [1, 2..., n]
        k = k - 1
        while n > 0:
            q, r = divmod(k, fac[n - 1])  # quotient and remainder
            res += str(nums[q])
            del nums[q]
            k = r
            n -= 1

        return res
# @lc code=end

# Accepted
# 200/200 cases passed(36 ms)
# Your runtime beats 80.57 % of python3 submissions
# Your memory usage beats 8.33 % of python3 submissions(13.8 MB)
