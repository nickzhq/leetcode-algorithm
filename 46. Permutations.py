class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrace(idx_cur, end):
            if idx_cur == end:
                # res.append(nums)   # 数组是引用，当完成所有计算后，数组保持原始状态，res中存储的所有结果都会变成原始状态
                res.append(nums[:])  # 这样写相当于把数组复制了一份，然后加到了结果中，当所有计算完成后，数组会变成原始状态
                return
            
            for idx in xrange(idx_cur, end):
                nums[idx], nums[idx_cur] = nums[idx_cur], nums[idx]
                backtrace( idx_cur + 1, end )
                nums[idx], nums[idx_cur] = nums[idx_cur], nums[idx]
                
        res = []
        backtrace( 0, len(nums) )
        return res
        