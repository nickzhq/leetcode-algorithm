__author__ = 'Nick'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        dict = {}
        for i in nums:
            if i in dict.keys():
                dict[i] += 1
            else:
                dict[i] = 0
                dict[i] += 1
        res = nums[0]
        for i in dict.keys():
            if dict[i] > dict[res]:
                res = i
        return res
        '''
        return sorted(nums)[len(nums)//2]

# Bit manipulation
def majorityElement5( nums):
    bit = [0]*32
    for num in nums:
        for j in range(32):
            bit[j] += num >> j & 1
    res = 0
    for i, val in enumerate(bit):
        if val > len(nums)//2:
            # if the 31th bit if 1,
            # it means it's a negative number
            if i == 31:
                res = -((1<<31)-res)
            else:
                res |= 1 << i
    return res


print( majorityElement5([3,2,3,9,0,9,9,9,9,9]) )