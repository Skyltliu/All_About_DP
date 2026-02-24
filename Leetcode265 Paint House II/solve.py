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
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        for house in range(1, len(costs)):
            min_color = second_color = None
            
            for color in range(len(costs[0])):
                if min_color is None or costs[house-1][color] < costs[house-1][min_color]:
                    second_color = min_color
                    min_color = color
                elif second_color is None or costs[house-1][color] < costs[house - 1][second_color]:
                    second_color = color
            for k in range(len(costs[0])):
                if k == min_color:
                    costs[house][k] += costs[house-1][second_color]
                else:
                    costs[house][k] += costs[house-1][min_color]
            
        return min(costs[-1])