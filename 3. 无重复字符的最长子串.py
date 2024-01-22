#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3. 无重复字符的最长子串.py
@Time    :   2020/07/17 21:17:48
@Author  :   Nick Zuo 
@Version :   3.7
@Contact :   903627391@qq.com
@Desc    :   None
'''
# 638157801
# here put the import lib
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 利用set的特性保存数据
        occupied = set()
        # 尾指针
        tail = 0
        # 最终结果记录
        res = 0
        # 遍历字符串
        for i in range(len(s)):
            # 窗口滑动时，排除最左边的字符
            if i != 0:
                occupied.remove(s[i-1])
            # 找出以i为起点的最长不重复的字符串
            # 所以需要以下两个条件
            while tail < len(s) and s[tail] not in occupied:
                occupied.add(s[tail])
                tail += 1
            
            res = max(res, tail-i)

        return res


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         head = -1
#         char_dict = {}

#         for i,c in enumerate(s):
#             if c in char_dict and char_dict[c] > head:
#                 head = char_dict[c]
#                 char_dict[c] = i
#             else:
#                 char_dict[c] = i
#                 res = max(res, i-head)

#         return res

