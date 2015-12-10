__author__ = 'Nick'

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        nums.sort()
        if nums[0] != 0:
            return 0
        length = len(nums)
        for i in range(length):
            if i+1 == length:
                return nums[i] + 1
            elif abs(nums[i+1] - nums[i]) != 1:
                return nums[i] + 1
        '''
        length = len(nums)
        total = length*(length+1)/2
        summ = sum(nums)
        return total -summ
