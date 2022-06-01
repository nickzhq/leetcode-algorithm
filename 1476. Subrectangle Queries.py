# coding=utf-8
# @Time     : 01th June, 2022  20:33
# @Author   : Nick Z
# @Email    : nick_zz@qq.com
# @File     : 1476. Subrectangle Queries.py
# @Software : PyCharm 
# =======================================================
# https://leetcode.com/problems/subrectangle-queries/
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.origin = rectangle[:]
        self.update = []


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.update.append([row1, col1, row2, col2, newValue])


    def getValue(self, row: int, col: int) -> int:
        for row1, col1, row2, col2, value in self.update[::-1]:
            if row1 <= row <= row2 and col1 <= col <= col2:
                return value

        return self.origin[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)