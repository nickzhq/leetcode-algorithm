#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 04. 二维数组中的查找.py
@Time    :   2020/09/15 22:46:02
@Author  :   Nick Zuo 
@Version :   3.7
@Contact :   903627391@qq.com
@Desc    :   None
'''
# https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
# here put the import lib

# class Solution:
#     def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
#         if matrix == []:
#             return False

#         cols = len(matrix[0])
#         rows = len(matrix)

#         for row in range(rows):
#             for col in range(cols):
#                 if matrix[row][col] > target:
#                     break
#                 if matrix[row][col] == target:
#                     return True

#         return False

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or matrix == [] or matrix[0] == []:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target: return True
            elif matrix[row][col] > target: col -= 1
            elif matrix[row][col] < target: row += 1

        return False