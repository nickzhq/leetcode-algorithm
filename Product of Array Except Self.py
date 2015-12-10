__author__ = 'Nick'

def productExceptSelf( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    n = len(nums)

    if n < 2:
        return nums
    res = list(nums)
    # transform nums such that nums[i] = num[1] x nums[2] x ... x nums[i - 1]
    nums[0] = 1
    for i in range(1, n):
        nums[i] = nums[i - 1] * res[i - 1]

    # transform res such that res[i] = res[i + 1] x res[i + 2] x ... x res[n - 1]
    tmp = res[-1]
    res[-1] = 1
    for i in reversed(range(0, n - 1)):
        t = res[i]
        res[i] = tmp * res[i + 1]
        tmp = t

    # transform res such that res[i] = res[1] x res[2] x ... x res[i  - 1] x res[i + 1] x ... x res[n - 1]
    for i in range(1, n):
        res[i] *= nums[i]

    return res

nums=[1,3,5,6]
res=productExceptSelf(nums)
print(res)
