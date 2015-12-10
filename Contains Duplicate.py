__author__ = 'Nick'

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = set(nums)
        if ( len(res) < len(nums) ):
            return True
        else:
            return False
        # return len(nums) != len(set(nums))