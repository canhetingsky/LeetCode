#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_nums = list(map(int, version1.split('.')))
        version2_nums = list(map(int, version2.split('.')))

        # delete the consecutive 0 at the end
        while version1_nums:
            if version1_nums[-1] != 0:
                break
            version1_nums.pop()
        while version2_nums:
            if version2_nums[-1] != 0:
                break
            version2_nums.pop()

        index = 0
        while index < len(version1_nums) and index < len(version2_nums):
            if version1_nums[index] > version2_nums[index]:
                return 1
            elif version1_nums[index] < version2_nums[index]:
                return -1
            index += 1

        if len(version1_nums) > index:
            return 1
        if len(version2_nums) > index:
            return - 1
        return 0
# @lc code=end

# Accepted
# 72/72 cases passed(24 ms)
# Your runtime beats 97.59 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
