#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):  # The given board size is always 9x9
            row = board[i]
            if not self.isValidRowOrColumn(row):  # check each row
                return False

            column = [row[i] for row in board]
            if not self.isValidRowOrColumn(column):  # check each column
                return False

        for h in range(3):  # h:horizon index for sub_boxes
            for v in range(3):  # v:vertical index for sub_boxes
                sub_box = [board[x][y]
                           for x in range(3*h, 3*h + 3) for y in range(3*v, 3*v + 3)]
                if not self.isValidRowOrColumn(sub_box):
                    return False

        return True

    def isValidRowOrColumn(self, row: List[str]) -> bool:
        # Only the filled cells need to be validated
        unit = [c for c in row if c != '.']

        return len(set(unit)) == len(unit)

# @lc code=end

# Accepted
# 504/504 cases passed(108 ms)
# Your runtime beats 79.24 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions(14 MB)
