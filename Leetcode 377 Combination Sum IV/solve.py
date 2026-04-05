from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        #optimization line:
        nums.sort()
        for combi in range(target+1):
            for num in nums:
                if combi - num >= 0:
                    dp[combi] += dp[combi-num]
                #optimization condition:
                else:
                    break
        return dp[target] 