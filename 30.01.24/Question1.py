Best time To Buy And Sell


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
solution = Solution()
result = solution.maxProfit([7,1,5,3,6,4])
print(result)  

"logic 2:"

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [0] * n

        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i] - min(prices[:i]))

        return dp[-1]
solution = Solution()
result = solution.maxProfit([7,1,5,3,6,4])
print(result)  # Output: 5
