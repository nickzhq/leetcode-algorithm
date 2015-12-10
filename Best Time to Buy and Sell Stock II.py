__author__ = 'Nick'

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        result = 0
        for i in range(1,len(prices)):
            result += max(0,prices[i]-prices[i-1])

        return result
        '''
        return sum((prices[i]-prices[i-1] for i in range(1,len(prices)) if prices[i-1] < prices[i]))