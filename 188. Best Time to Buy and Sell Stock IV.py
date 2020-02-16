# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        """
        if k >= len(prices): return sum([v-u for u,v in zip(prices,prices[1:]) if v-u>=0] or [0])
        
        sell = [ 0 for _ in xrange(k+1)]
        buy  = [ -float('inf') for _ in xrange(k+1)]
        
        for p in prices:
            for idx in xrange(k,0,-1):
                sell[idx] = max(sell[idx], buy[idx] + p)
                buy[idx]  = max(buy[idx], sell[idx - 1] - p)
                
        return sell[k]
        """
        
        profit = 0
        if k >= len(prices):
            for i in xrange(1, len(prices)):
                profit += ( prices[i] - prices[i-1] ) if prices[i] > prices[i-1] else 0
            return profit
        
        buy  = [float('inf')] * (k+1)
        sell = [0] * (k+1)
        for p in prices:
            """
            每一次买入时，其实都要调整基准
            第一次买入时，基准其实是0，只是多数人没意识到
            第二次买入及以后每次买入时，基准是第一次卖出时所得，所以要减去
            """
            for idx in xrange(1, k + 1):
                buy[idx]  = min(buy[idx], p - sell[idx - 1])
                sell[idx] = max(sell[idx], p - buy[idx])
        
        return sell[k]
