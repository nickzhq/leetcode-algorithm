__author__ = 'Nick'
'''
class solution:
    def totalNQueens(self, n):
        self.res = 0
        self.dfs([-1]*n, 0)
        return self.res

    # nums is type list
    # index is number of row
    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):

                self.dfs(nums, index+1)

    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[n]-nums[i]) in(0,n-i):
                return False
        return True

m = solution()
#print(m.totalNQueens(1))
print(m.totalNQueens(4))
#print(m.totalNQueens(2))
'''
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return list(self.queens(n))

    def conflict(self,state, nextX):
        nextY = len(state)
        for i in range(nextY):
            if abs(state[i] - nextX) in (0,nextY):
                return True
        return False

    def queens( self, num = 8, state=() ):
        for pos in range(num):
            if not self.conflict(state, pos):
                if len(state) == num - 1:
                    #self.res += 1
                    yield (pos,)
                else:
                    for result in self.queens(num, state+(pos,)):
                        yield (pos,)+result

    def prettyprint(self,solution):
        def lines(pos, length = len(solution)):
            return '.'*(pos) +"Q"+'.'*(length-pos-1)
        for pos in solution:
            print(lines(pos))

m = Solution()
print(  list(m.queens(num = 2) )  )