# 1314. Matrix Block Sum
# https://leetcode.com/problems/matrix-block-sum/
# https://leetcode.com/problems/matrix-block-sum/discuss/499970/Problem-explanation-in-Python-Step-by-Step-O(m*n)-98-speed-and-100-memory
class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        rowSum = [[0 for _ in range(len(mat[i]))] for i in range(len(mat))]
        res = [[0 for _ in range(len(mat[i]))] for i in range(len(mat))]
        
        # Compute the sum of every group in the row with a DP
        # complexity: O(m*n)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if j > 0: # 根据公式rowSum[i][j] = rowSum[i][j-1]-a+b 只能处理当前行第二个开始的元素
                    a = mat[i][j-K-1] if j-K-1 >= 0 else 0 # or 0
                    b = mat[i][j+K] if j+K < len(mat[i]) else 0 # or 0
                    rowSum[i][j] = rowSum[i][j-1]-a+b
                else: # 处理当前行的第一个元素
                    for k in range(0, min(j+K+1, len(mat[i]))):
                        rowSum[i][j] += mat[i][k]
        
        # Uses the computed sum of rows to compute the sum
        # of the squares with the same DP but now for columns
        # complexity: O(m*n)
        for i in range(len(rowSum)):
            for j in range(len(rowSum[i])):
                if i > 0: # 处理当前列第二个元素
                    a = rowSum[i-K-1][j] if i-K-1 >= 0 else 0 # or 0
                    b = rowSum[i+K][j] if i+K < len(rowSum) else 0 # or 0
                    res[i][j] = res[i-1][j]-a+b
                else: # 处理当前列的第一个元素
                    for k in range(0, min(i+K+1, len(rowSum))):
                        res[i][j] += rowSum[k][j]
        
        # total complexity: O(m*n)
        return res