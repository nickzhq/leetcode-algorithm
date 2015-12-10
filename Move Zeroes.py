__author__ = 'Nick'
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # nums.sort(cmp= lambda a, b: -1 if b == 0 else 0)
        if( nums.count(0) != 0 ):
            for i in range(0,nums.count(0)):
                nums.remove(0)
                nums.append(0)
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = sorted(nums,  key = lambda  b: -1 if b == 0 else 0)
        print(nums)

m = Solution()
m.moveZeroes([0,1,0,3,12])