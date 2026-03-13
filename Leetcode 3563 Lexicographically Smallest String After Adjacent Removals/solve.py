from functools import cache


class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        A = [ord(c) - ord('a') for c in s]
        @cache
        def empty(i, j):
            if i > j:
                return True
            if abs(A[i] - A[j]) in [1, 25] and empty(i+1, j-1):
                return True
            return any(empty(i, k) and empty(k+1, j) for k in range(i+1, j, 2))
        @cache
        def dp(i):
            if i == n:
                return ""
            ans = s[i] + dp(i+1)
            for j in range(i+1, n, 2):
                if empty(i,j):
                    ans = min(ans, dp(j+1))
            return ans
        return dp(0)