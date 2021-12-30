#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 03. 数组中重复的数字.py
@Time    :   2020/09/15 22:10:53
@Author  :   Nick Zuo 
@Version :   3.7
@Contact :   903627391@qq.com
@Desc    :   None
'''
# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
# here put the import lib

# class Solution:
#     def findRepeatNumber(self, nums: List[int]) -> int:
#         visit = set()
#         res = None
#         for num in nums:
#             if num in visit:
#                 res = num
#                 break
#             visit.add(num)
        
#         return res


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            if nums[idx] == idx:
                continue
            if nums[nums[idx]] == nums[idx]: return nums[idx]
            nums[nums[idx]], nums[idx] = nums[idx], nums[nums[idx]]

        return -1
                

