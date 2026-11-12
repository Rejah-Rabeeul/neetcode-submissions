class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow=0
        ans=0
        val=0
        for fast in range(len(prices)):
            if prices[fast]<prices[slow]:
                slow=fast
                val=prices[slow]
            if prices[fast]>val:
                val=prices[fast]
                ans1=val-prices[slow]
                ans=max(ans,ans1)
        return ans