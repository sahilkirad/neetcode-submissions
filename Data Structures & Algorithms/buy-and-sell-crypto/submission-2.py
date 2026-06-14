class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=prices[0]
        max_profit=0
        for i in prices:
            profit=i-min1
            max_profit=max(max_profit,profit)
            min1=min(min1,i)
        return max_profit