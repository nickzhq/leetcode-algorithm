# 1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
class Solution:
    def __init__(self):
        self.res = sys.maxsize
        
    def convert(self, mat, m, n, i, j):
        for di, dj in ((0,0), (1,0), (-1,0), (0,1), (0, -1)):
            i0, j0 = i + di, j + dj
            if 0 <= i0 < m and 0 <= j0 < n:
                mat[i0][j0] ^= 1
        
    def dfs(self, mat, m, n, pos, flip_cnt):
        if pos == m * n:
            if all(mat[i][j] == 0 for i in range(m) for j in range(n)):
                self.res = min(self.res, flip_cnt)
            return

        # pos // n 是 row
        # pos % n 是 col
        x, y = pos // n, pos % n
        # 第一行，每个位置都可以翻或不翻
        if x == 0:
            # not flip
            self.dfs(mat, m, n, pos + 1, flip_cnt)

            # flip
            self.convert(mat, m, n, x, y)
            self.dfs(mat, m, n, pos + 1, flip_cnt + 1)
            self.convert(mat, m, n, x, y)
        else:
            # 从第二行开始，依据上一个位置是不是1
            if mat[x-1][y] == 0:
                # not flip
                self.dfs(mat, m, n, pos + 1, flip_cnt)
            else:
                # flip
                self.convert(mat, m, n, x, y)
                self.dfs(mat, m, n, pos + 1, flip_cnt + 1)
                self.convert(mat, m, n, x, y)
    
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        self.dfs(mat, m, n, 0, 0)
        return self.res if self.res != sys.maxsize else -1
        