# 980. Unique Paths III
# https://leetcode.com/problems/unique-paths-iii/
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        
        # 迭代器，用来返回当前位置的上下左右四个方向且可访问的位置
        def neighbors(r, c):
            for try_r, try_c in ((r+1, c), (r-1,c), (r, c+1), (r,c-1)):
                if 0 <= try_r < row and 0 <= try_c < col and grid[try_r][try_c] % 2 == 0:
                    yield try_r, try_c
        
        # 遍历grid，设置TODO是多少个零，同是寻找起点和终点
        todo = 0 
        self.sr, self.sc, self.er, self.ec = 0,0,0,0
        for r, _ in enumerate(grid):
            for c, val in enumerate(grid[r]):
                if val != -1: todo += 1
                if val == 1: self.sr, self.sc = r, c
                if val == 2: self.er, self.ec = r, c
        
        self.res = 0
        def dfs(r, c, todo):
            todo -= 1
            if todo < 0: return
            if r == self.er and c == self.ec:
                if todo == 0:
                    self.res += 1
                return
            
            grid[r][c] = -1
            for try_r, try_c in neighbors(r, c):
                dfs(try_r, try_c, todo)
            grid[r][c] = 0
            
        dfs(self.sr, self.sc, todo)
        return self.res
            
        
        