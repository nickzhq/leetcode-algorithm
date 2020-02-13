class Solution(object):
    res = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs([], [], [], n)
        return [[ "."*i + "Q" + "."*(n-1-i) for i in col] for col in self.res]
    
    
    def dfs(self, queens, xy_sub, xy_sum, n):
        q = len(queens)
        if n == q:
            self.res.append(queens)
            return None
        for i in xrange(n):
            if i not in queens and q-i not in xy_sub and q+i not in xy_sum:
                self.dfs(queens+[i], xy_sub+[q-i], xy_sum+[q+i], n)
        