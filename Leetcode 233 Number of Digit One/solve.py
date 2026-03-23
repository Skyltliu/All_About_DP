#pure math:
from functools import cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        countr = 0
        i = 1
        while i <= n:
            divider = i * 10
            countr += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return countr
    

#digit dp
class Solution:
    def countDigitOne(self, n: int) -> int:
        h = str(n)
        @cache
        def dp(pos, tight, cnt):
            if len(h) == pos:
                return cnt
            ans = temp = 0
            limit = 9
            if tight:
                limit = int(h[pos])
            for d in range(limit+1):
                new_tight = tight and d == int(h[pos])
                if d == 1:
                    temp = 1
                ans += dp(pos+1, new_tight, cnt+temp)
                temp = 0
            return ans
        return dp(0, True, 0)