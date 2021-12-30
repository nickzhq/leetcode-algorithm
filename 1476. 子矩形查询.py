#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1476. 子矩形查询.py
@Time    :   2020/07/14 21:11:34
@Author  :   Nick Zuo 
@Version :   3.7
@Contact :   903627391@qq.com
@Desc    :   这里没有暴力更新数值，而是通过hashmap的方式记录数值，当坐标处在hashmap的key中，直接取出
'''

# here put the import lib

# https://leetcode-cn.com/problems/subrectangle-queries/

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.hashmap = {}


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.hashmap[(row1, col1, row2, col2)] = newValue

    def getValue(self, row: int, col: int) -> int:
        res = self.rectangle[row][col]
        for row1, col1, row2, col2 in self.hashmap.keys():
            if row1 <= row <= row2 and col1 <= col <= col2:
                res = self.hashmap[(row1, col1, row2, col2)]
        
        return res



# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
