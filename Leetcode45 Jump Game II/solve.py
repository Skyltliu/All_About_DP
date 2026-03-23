from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = min(dp[i : i + nums[i] + 1]) + 1
        return dp[0]
    

#greedy:
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        l = r = 0
        n = len(nums)
        while r < n-1:
            farthest = r
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
           
            l = r
            r = farthest
            ans += 1
        return ans