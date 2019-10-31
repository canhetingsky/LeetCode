#!/usr/bin/python3
# encoding: utf-8
#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        palindrome = ''
        for i in range(length):
            # for even, like "abba"
            temp = self.getPalindrome(s, i, i + 1)
            if len(temp) > len(palindrome):
                palindrome = temp

            # for odd , like "aba"
            temp = self.getPalindrome(s, i, i)
            if len(temp) > len(palindrome):
                palindrome = temp

        return palindrome

    def getPalindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1:r]
