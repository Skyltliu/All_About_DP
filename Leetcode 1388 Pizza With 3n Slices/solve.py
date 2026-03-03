from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def slicese(arr):
            k = len(slices) // 3
            dp = [[0] * (k+1) for _ in range(len(arr) + 1)]
            m = len(arr)
            for i in range(1, m+1):
                for j in range(1, k+1):
                    dp[i][j] = dp[i-1][j]
                    if i >= 2:
                        dp[i][j] = max(dp[i][j], dp[i-2][j-1] + arr[i-1])
                    elif j == 1:
                        dp[i][j] = max(dp[i][j], arr[i-1])
            
            return dp[m][k]
        return max(slicese(slices[:-1]), slicese(slices[1:]))