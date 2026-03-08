from functools import lru_cache
from typing import List

#top down (which is always unacceptable)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] + piles[i]
        @lru_cache(None)
        def helper(i, M):
            if i >= n:
                return 0
            elif (n-i) <= 2 * M:
                return suffix[i]
            else:
                best = 0
                for X in range(1, 2*M + 1):
                    best = max(best, suffix[i] - helper(i+X, max(M, X)))
                return best
        return helper(0, 1)
    
#bottom up(true dp)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] + piles[i]
        dp = [[0] * (n+1) for _ in range(n)]
        for i in range(n-1, -1, -1):
            for m in range(1, n+1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix[i]
                else:
                    for X in range(1, 2*m+1):
                        dp[i][m] = max(dp[i][m], suffix[i] - dp[i+X][max(m, X)])
        return dp[0][1]