#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start


class NumArray:

    def __init__(self, nums: List[int]):
        # You may assume that the array does not change
        # There are many calls to sumRange function
        self.sums = []
        for i, num in enumerate(nums):
            if i == 0:
                self.sums.append(num)
            else:
                self.sums.append(self.sums[- 1] + num)

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j]-self.sums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

# Accepted
# 16/16 cases passed(76 ms)
# Your runtime beats 96.55 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(16.1 MB)
