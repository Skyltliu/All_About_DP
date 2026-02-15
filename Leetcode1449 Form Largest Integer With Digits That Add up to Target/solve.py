from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [-float('inf')] * (target + 1)
        dp[0] = 0
        for i in range(1, target+1):
            for t in range(9):
                c = cost[t]
                if i >= c:
                    dp[i] = max(dp[i], dp[i - c] + 1)
        if dp[target] < 0:
            return "0"
        #phase 2
        curr_target = target
        res = []
        while curr_target > 0:
            for i in range(8, -1, -1):
                d = cost[i]
                if curr_target >= d and (dp[curr_target - d] + 1 == dp[curr_target]):
                    res.append(str(i+1))
                    curr_target -= d
                    break
        return "".join(res)