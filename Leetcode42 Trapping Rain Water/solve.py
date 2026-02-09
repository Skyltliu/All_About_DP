#standard DP solution: Time Complexity: O(n); Space Complexity: O(n)
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        leftmax = [0] * len(height)
        leftmax[0] = height[0]
        for i in range (1, len(height)):
            leftmax[i] = max(height[i], leftmax[i-1])
        n = len(height)
        rightmax=[0] * n
        rightmax[n-1]=height[n-1]
        for i in range(n-2, -1, -1):
            rightmax[i] = max(height[i], rightmax[i+1])
        count = 0
        for i in range(n):
            wall = min(leftmax[i], rightmax[i])
            water = wall - height[i]
            if (water) >0:
                count += water
        return count