from typing import List

#tabulation
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
    
#memoization
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        memo = {}
        ans= self.helper(cost, 1, target, memo)
        return ans if ans is not None else '0'
    def helper(self, cost, index, t, memo):
        key = (index, t)
        if key in memo:
            return memo[key]
        if t == 0:
            return ""
        if t < 0 or index > 9:
            return None
        suffix = self.helper(cost, 1, t-cost[index-1], memo)
        take = None if suffix is None else str(index) + suffix
        skip = self.helper(cost, index+1, t, memo)
        res = self.bigger(take, skip)
        memo[(index, t)] = res
        return res
    def bigger(self, a, b):
        if a is None:
            return b
        elif b is None:
            return a
        if len(a) != len(b):
            return a if len(a) > len(b) else b
        return a if a > b else b