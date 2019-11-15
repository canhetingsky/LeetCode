#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        res = [1] * n  # 1:prime; 0:not prime
        res[0] = res[1] = 0
        for i in range(2, n):
            if res[i] == 1:
                for j in range(2, (n-1)//i + 1):  # less than number n
                    res[i * j] = 0

        return sum(res)
# @lc code=end

# Accepted
# 20/20 cases passed(872 ms)
# Your runtime beats 35.45 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(24.3 MB)
