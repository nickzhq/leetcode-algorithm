# coding=utf-8
# @Time     : 21th December, 2023  09:20
# @Author   : Nick Z
# @Email    : nick_zz@qq.com
# @File     : 2556. Disconnect Path in a Binary Matrix by at Most One Flip.py
# @Software : PyCharm 
# =======================================================

class Solution:
    def isPossibleToCutPath(self, grid):
        if len(grid) == 1 and len(grid[0]) == 2:
            return False
        paths = []
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        def path_travesal(row, col, traversal ):
            nonlocal grid, paths, max_row, max_col
            if grid[row][col] == 0:
                return
            if row == max_row and col == max_col:
                paths.append(traversal)
                return
            else:
                if row + 1 <= max_row:
                    path_travesal(row + 1, col, traversal + [[row + 1, col]])
                if col + 1 <= max_col:
                    path_travesal(row, col + 1, traversal + [[row, col + 1]])

        # step 1: find all possible the path
        path_travesal(0, 0, [[0, 0]])

        # step 2: statistics from each index(m,n) of the each path
        if paths:
            stat = {}
            for path in paths:
                for pos in path:
                    if str(pos) in stat.keys():
                        stat[str(pos)] += 1
                    else:
                        stat[str(pos)] = 1
            #if str([0, 0]) in stat.keys():
            del stat[str([0, 0])]
            #if str([max_row, max_col]) in stat.keys():
            del stat[str([max_row, max_col])]

            # step 3: if the index(m,n) is included by the each path, it is to make the matrix disconnect. Otherwise, return False.
            #if stat.values() is not None:
            max_used_index_val = max(stat.values())
            #else:
            #    max_used_index_val = -1
        else:
            return True
        return max_used_index_val == len(paths)


if __name__ == "__main__":
    t = Solution()
    r = t.isPossibleToCutPath([[1,1,1],[0,0,0],[1,1,1]])
    print(r)