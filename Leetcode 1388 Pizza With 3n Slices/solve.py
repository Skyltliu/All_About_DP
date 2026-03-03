from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        ms = len(slices)
        k = ms // 3
        
        def slicese(arr):
            m = len(arr)
            dp = [[0] * (k+1) for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, k+1):
                    dp[i][j] = dp[i-1][j]
                    take = arr[i-1]
                    if i >= 2:
                        take += dp[i-2][j-1]
                    elif j > 1:
                        continue
                    dp[i][j] = max(dp[i][j], take)
            return dp[m][k]
        return max(slicese(slices[:-1]), slicese(slices[1:]))