from typing import List
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        e1 = e2 = o1 = o2 = 0
        mod = 10**9+7
        for x in nums:
            if x % 2 == 0:
                new_e1 = (1+o1+o2) 
                new_e2 = e1 
                e1 = e1 + new_e1
                e2 = e2 + new_e2
            else:
                new_o1 = (1+e1+e2) 
                new_o2 = o1
                o1 = o1 + new_o1
                o2 = o2 + new_o2
        return (e1+e2+o1+o2) % mod