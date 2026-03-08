from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n+1)
        dp[-1] = 0
        for i in range(n-1, -1, -1):
            curr = 0
            for k in range(3):
                if i + k + 1 > n:
                    break
                curr += stoneValue[i + k]
                dp[i] = max(dp[i], curr - dp[i+k+1])
        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"