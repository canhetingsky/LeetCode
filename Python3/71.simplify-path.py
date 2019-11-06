#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for token in path.split('/'):
            if token in ('', '.'):
                pass
            elif token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)

        return '/' + '/'.join(stack)
# @lc code=end

# Accepted
# 254/254 cases passed(24 ms)
# Your runtime beats 99.96 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
