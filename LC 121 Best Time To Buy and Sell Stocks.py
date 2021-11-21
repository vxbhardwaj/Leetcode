class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxprofit=0
        profit=0
        while r<len(prices):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                maxprofit=max(profit,maxprofit)
            else:
                l=r
            r+=1
        return maxprofit