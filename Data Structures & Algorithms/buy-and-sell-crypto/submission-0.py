class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            curr = prices[i]
            if curr < lowest:
                lowest = curr
            else:
                profit = curr - lowest
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit