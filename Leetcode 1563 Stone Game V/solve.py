from functools import lru_cache
from typing import List

#O(n^3) standard top down dp solution (does not pass)
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = [0] * (len(stoneValue)+1)
        for i in range(len(stoneValue)):
            prefix[i+1] = prefix[i] + stoneValue[i]
        @lru_cache(None)
        def dfs(l, r):
            if l == r:
                return 0
            best = 0
            for k in range(l, r):
                left = prefix[k+1] - prefix[l]
                right = prefix[r+1] - prefix[k+1]
                if left < right:
                    best = max(best, left + dfs(l, k))
                elif right < left:
                    best = max(best, right + dfs(k+1, r))
                else:
                    best = max(best, left + max(dfs(l, k), dfs(k+1, r)))
                

            return best
        return dfs(0, len(stoneValue) - 1)
    
#Knuth's Optimization solution with sliding balance point (M)
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        p = [0] * (n+1)
        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]
        for i in range(n):
            maxL[i][i] = maxR[i][i] = stoneValue[i]
        for i in range(n):
            p[i+1] = p[i] + stoneValue[i]
        for i in range(n-2, -1, -1):
            mid = i
            for j in range(i+1, n):
                total = p[j+1] - p[i]
                while mid < j and (p[(mid)+1]-p[i]) * 2 <= total:
                    mid += 1
                if mid > i:
                    dp[i][j] = max(dp[i][j], maxL[i][mid-1])
                if mid < j:
                    dp[i][j] = max(dp[i][j], maxR[mid+1][j])
                if (p[(mid-1) + 1] - p[i]) * 2 == total:
                    dp[i][j] = max(max(dp[i][j], maxR[mid][j]), maxL[i][mid-1])
                maxL[i][j] = max(maxL[i][j-1], total + dp[i][j])
                maxR[i][j] = max(maxR[i+1][j], total + dp[i][j])
        return dp[0][n-1]
