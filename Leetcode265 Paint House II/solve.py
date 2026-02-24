from typing import List

#regular dp solution:
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        for house in range(1, len(costs)):
            for k in range(len(costs[0])):
                mini = float('inf')
                for i in range(len(costs[0])):
                    if i == k:
                        continue
                    mini = min(mini, costs[house-1][i])
                costs[house][k] += mini
        
        return min(costs[-1])
    
#time optimized dp:
