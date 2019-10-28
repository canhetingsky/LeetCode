#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        pre_seq = self.countAndSay(n - 1)
        new_seq = ''
        for i in range(len(pre_seq)):
            c = pre_seq[i]
            if i > 0 and c == new_seq[-1]:
                continue

            count = 0
            for j in range(i, len(pre_seq)):
                if pre_seq[j] == c:
                    count += 1
                else:
                    break
            new_seq += (str(count) + c)

        return new_seq
# @lc code=end

# Accepted
# 18/18 cases passed(40 ms)
# Your runtime beats 76.5 % of python3 submissions
# Your memory usage beats 6.38 % of python3 submissions(13.7 MB)
