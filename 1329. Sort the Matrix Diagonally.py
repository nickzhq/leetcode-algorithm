# https://leetcode.com/problems/sort-the-matrix-diagonally/
from collections import defaultdict
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # dict_rec = {}
        dict_rec = defaultdict(list)
        for row in xrange(len(mat)):
            for col in xrange(len(mat[0])):
                # if row - col in dict_rec:
                #     dict_rec[row - col].append(mat[row][col])
                # else:
                #     dict_rec[row - col] = [mat[row][col]]
                dict_rec[row - col].append(mat[row][col])
                    
        # sort
        for key in dict_rec:
            dict_rec[key].sort()
            
        for row in xrange(len(mat)):
            for col in xrange(len(mat[0])):
                mat[row][col] = dict_rec[row - col][0]
                del(dict_rec[row - col][0])
                
        return mat
        
        