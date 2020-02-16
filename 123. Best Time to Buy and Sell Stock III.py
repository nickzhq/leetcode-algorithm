# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        fir_sell = sec_sell = 0
        fir_buy = sec_buy = float('inf')

        for p in prices:
            # 这里先min后max，是因为先买后卖符合人的惯性思维，同时钱上表示用正号记录，所以会出现在买时用min，在卖时用max
            # 如果抛弃这种思维，改用收益来表示，在买入时当前收益就是 -price，此时要做对比就要用 max了, 同时在初始值也要相应的变化
            fir_buy = min(fir_buy, p)
            fir_sell = max(fir_sell, p - fir_buy)
            sec_buy = min(sec_buy, p - fir_sell)
            sec_sell = max(sec_sell, p - sec_buy)
            

        return sec_sell