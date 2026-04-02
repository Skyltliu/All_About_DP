from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1
        res = nums[0]
        for curr in nums:
            tmp = curr * curMax
            curMax = max(curr, max(curr * curMax, curr * curMin))
            curMin = min(curr, min(curr * curMin, tmp))
            res = max(res, curMax)

        return res