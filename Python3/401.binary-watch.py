#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num > 10:
            return []

        times = []
        for h in range(12):  # 4 LEDs represent the hours (0-11)
            for m in range(60):  # 6 LEDs represent the minutes (0-59)
                if (bin(h) + bin(m)).count('1') == num:  # n LEDs are currently on
                    hour_str = str(h)
                    minute_str = str(m) if m >= 10 else '0' + str(m)
                    times.append(hour_str + ':' + minute_str)

        return times
# @lc code=end

# Accepted
# 10/10 cases passed (24 ms)
# Your runtime beats 97.72 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
