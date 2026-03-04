from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        k = 2
        dp = [[[float('-inf')] * (k+1) for _ in range(2)] for _ in range(n)]
        for i in range(k+1):
            dp[0][0][i] = 0
            dp[0][1][i] = -prices[0]
        for i in range(1, n):
            for j in range(k+1):
                dp[i][1][j] = max(dp[i-1][1][j], dp[i-1][0][j] - prices[i])
                dp[i][0][j] = 0
                if j >= 1:
                    dp[i][0][j] = max(dp[i-1][0][j], dp[i-1][1][j-1] + prices[i])
                
        return max(dp[n-1][0])