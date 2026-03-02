from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums):
        rob1 = rob2 = 0
        for num in nums:
            curr = max(rob2, rob1 + num)
            rob1 = rob2
            rob2 = curr
        return rob2