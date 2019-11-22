#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = ''
        self.dfs(grid, i+1, j)  # down
        self.dfs(grid, i-1, j)  # up
        self.dfs(grid, i, j+1)  # right
        self.dfs(grid, i, j-1)  # left
# @lc code=end

# Accepted
# 47/47 cases passed(140 ms)
# Your runtime beats 92.8 % of python3 submissions
# Your memory usage beats 96.58 % of python3 submissions(13.6 MB)
