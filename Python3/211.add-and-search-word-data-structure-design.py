#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#

# @lc code=start


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if len(word) not in self.dict:
            self.dict[len(word)] = set()
        self.dict[len(word)].add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) in self.dict:
            def compare(src, dst):
                for i in range(len(dst)):
                    if dst[i] == '.':
                        continue
                    if dst[i] != src[i]:
                        return False
                return True
            for s in self.dict[len(word)]:
                if compare(s, word):
                    return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

# Accepted
# 13/13 cases passed(144 ms)
# Your runtime beats 97.29 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(20.5 MB)
