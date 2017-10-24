__author__ = 'Nick'

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        value = 0
        for i in range(0, total):
            if total - 1  - i > 1:
                if nums[i] > nums[i + 1]:
                    value += nums[i]
                else:
                    value += nums[i+1]
                i += 1
            else:
                value += nums[total - 1]

        return value
