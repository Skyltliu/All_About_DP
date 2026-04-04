class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        dp = [0] * (n+1)
        for num in [1, 2, 3]:
            dp[num] = num
        for i in range(4, n+1):
            for j in range(1, i):
                dp[i] = max(i, max(dp[i], j * dp[i-j]))
        return dp[n]