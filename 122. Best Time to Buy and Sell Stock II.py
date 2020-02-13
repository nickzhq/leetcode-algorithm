# 122. Best Time to Buy and Sell Stock II
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for idx in xrange( 1, len(prices) ):
            if prices[idx] > prices[idx - 1]:
                profit += prices[idx] - prices[idx - 1]
                
        return profit