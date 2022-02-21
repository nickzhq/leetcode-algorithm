# coding=utf-8
# @Time     : 05th January, 2022  19:34
# @Author   : Nick Z
# @Email    : nick_zz@qq.com
# @File     : 131. Palindrome Partitioning.py
# @Software : PyCharm 
# =======================================================

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.isPalindrome = lambda s: s == s[::-1]
        res = []
        self.helper(s, res, [])
        return res

    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.helper(s[i:], res, path + [s[:i]])