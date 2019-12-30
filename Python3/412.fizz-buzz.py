#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):  # from 1 to n
            s = ''
            if i % 3 == 0 and i % 5 == 0:  # multiples of three and five
                s = 'FizzBuzz'
            elif i % 3 == 0:  # multiples of three
                s = 'Fizz'
            elif i % 5 == 0:  # multiples of five
                s = 'Buzz'
            else:
                s = str(i)
            res.append(s)

        return res
# @lc code=end

# Accepted
# 8/8 cases passed (44 ms)
# Your runtime beats 73.11 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.9 MB)
