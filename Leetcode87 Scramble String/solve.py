class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = [[[False for _ in range(31)]for _ in range(31)] for _ in range(31)]
        n = len(s1)
        for x in range(1, n+1):
            for i in range(n-x+1):
                for j in range(n-x+1):
                    if x == 1:
                        dp[i][j][x] = (s1[i] == s2[j])
                        continue
                    for y in range(1, x):
                        if dp[i][j][y] and dp[i+y][j+y][x-y]:
                            dp[i][j][x] = True
                            break
                        if dp[i][j + (x - y)][y] and dp[i + y][j][x - y]:
                            dp[i][j][x] = True
                            break
        return dp[0][0][n]
