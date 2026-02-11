class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        maxn = 0
        for i in range(1, len(s)):
            if s[i] == "(":
                continue
            if s[i] == ")":
                if s[i - 1] == "(":
                    maxn = max(maxn, (dp[i - 2] if i >= 2 else 0) + 2)
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                else:
                    if i - dp[i - 1] > 0 and s[i - dp[i-1] - 1] == "(":
                        maxn = max(maxn, 2 + dp[i-1] + (dp[i-dp[i-1]-2] if i - dp[i-1] >= 2 else 0))
                        dp[i] = 2 + dp[i-1] + (dp[i-dp[i-1]-2] if i - dp[i-1] >= 2 else 0)
        return maxn
