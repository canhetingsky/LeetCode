#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []

        # solution 1
        # if len(digits) == 1:
        #     return list(mapping.get(digits[0]))
        # pres = self.letterCombinations(digits[:-1])
        # return self.combine(pres, digits[-1], mapping)

        # solution 2
        lets = ['']
        for digit in digits:
            lets = self.combine(lets, digit, mapping)
        return lets

    def combine(self, pres, digit, mapping):
        lets = []

        for pre in pres:
            for c in mapping.get(digit):
                lets.append(pre + c)
        return lets
# @lc code=end
