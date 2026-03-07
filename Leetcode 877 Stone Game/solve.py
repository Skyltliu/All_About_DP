from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        memo = {}
        
        def helper(i, j):
            if i > j:
                return 0
            key = (i, j)
            if key in memo:
                return memo[key]
            m = (j - i + 1)
            parity = (N - m) % 2
            if parity == 0:
                res = max(piles[i] + helper(i+1, j), piles[j] + helper(i, j-1))
                memo[(i, j)] = res
                return res
            else:
                res = min(-piles[i] + helper(i+1, j), -piles[j] + helper(i, j-1))
                memo[(i, j)] = res
                return res
                
        return helper(0, N-1) > 0