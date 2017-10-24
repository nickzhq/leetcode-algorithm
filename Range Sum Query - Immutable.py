__author__ = 'Nick'

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if nums:
            self.nums = []
            self.nums.append( nums[0] )
            for i in range(1, len(nums)):
                self.nums.append( nums[i] + self.nums[-1] )
        else:
            self.nums = []


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.nums:
            if i != 0:
                return self.nums[j] - self.nums[i-1]
            else:
                return self.nums[j]
        else:
            return []


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
