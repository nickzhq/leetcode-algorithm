#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   50. Pow(x, n).py
@Time    :   2020/09/15 22:07:42
@Author  :   Nick Zuo 
@Version :   3.7
@Contact :   903627391@qq.com
@Desc    :   None
'''

# https://leetcode-cn.com/problems/powx-n/
# here put the import lib

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper( N: int ) -> float:
            res = 1.0
            new_x = x

            while(N > 0):
                if N % 2 == 1:
                     res *= new_x
                new_x *= new_x
                N = N // 2
            
            return res
        
        return helper(n) if n > 0 else 1.0 / helper(-n)