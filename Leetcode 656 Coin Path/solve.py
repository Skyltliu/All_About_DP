from typing import List

#memoization
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
    

#tabulation
class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        N = len(coins)
        dp = [float('inf')] * N
        nxt = [None] * N
        dp[-1] = 0
        for i in range(N-2, -1, -1):
            for j in range(1, maxJump+1):
                if i + j >= N:
                    break
                if coins[i + j] == -1:
                    continue
                if dp[i + j] == float('inf'):
                    continue
                store = dp[i+j] + coins[i+j]
                if store < dp[i]:
                    dp[i] = store
                    nxt[i] = i + j
        if dp[0] == float('inf'):
            return []
        ans = []
        curr = 0
        while curr is not None:
            ans.append(curr)
            if curr == N-1:
                break
            curr = nxt[curr]
        return [x+1 for x in ans]