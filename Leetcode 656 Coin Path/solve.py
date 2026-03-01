from typing import List


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        nxt = [None] * len(coins)
        has_cache = [None] * len(coins)
        cache = [None] * len(coins)
        def dp(index):
            if index == len(coins) - 1:
                return 0
            if has_cache[index]:
                return cache[index]
            best = float('inf')
            for i in range(1,maxJump+1):
                if index+i < len(coins) and coins[index+i] != -1:
                    if best > dp(index+i) + coins[index+i]:
                        best = dp(index+i) + coins[index+i]
                        nxt[index] = index + i
            has_cache[index] = True
            cache[index] = best
            return best
        r = dp(0)
        if r == float('inf'):
            return []
        ans = [0]
        while ans[-1] != len(coins) - 1:
            ans.append(nxt[ans[-1]])
        return [x + 1 for x in ans]