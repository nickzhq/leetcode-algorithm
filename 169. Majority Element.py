# coding=utf-8
# @Time     : 21th February, 2022  21:14
# @Author   : Nick Z
# @Email    : nick_zz@qq.com
# @File     : 169. Majority Element.py
# @Software : PyCharm 
# =======================================================
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Boyer-Moore voting algorithm

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1

        return candidate


