class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        buy = [-float("inf") for _ in range(n + 1)]
        sell = [0 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i - 1] - fee)
            sell[i] = max(sell[i - 1], prices[i - 1] + buy[i - 1])
        
        return max(sell[n], buy[n])
