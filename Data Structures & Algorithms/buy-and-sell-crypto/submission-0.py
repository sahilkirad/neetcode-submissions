class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        i=0
        j=len(prices)-1
        while(i<j):
            if(prices[i]<prices[j]):
                diff=prices[j]-prices[i]
                ans=max(diff,ans)
            j=j-1
            i=i+1
        return ans