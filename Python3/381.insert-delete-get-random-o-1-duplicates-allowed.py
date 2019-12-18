#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.nums:
            self.nums.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.nums)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

# Accepted
# 28/28 cases passed(244 ms)
# Your runtime beats 5.12 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(16.7 MB)
