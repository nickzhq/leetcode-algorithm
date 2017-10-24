__author__ = 'Nick'

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high,mid = 0,len(nums)-1,0
        while(low <= high):
            mid = (low +  high)//2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        if high < mid:
            return mid
        elif low > mid:
            return low

m = Solution()
print ( m.searchInsert([1],2) )
