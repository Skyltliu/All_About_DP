from typing import List


class Solution:
    #recursion solution (no caching)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        answer = []
        
        for i in range(n):
            for left_string in self.generateParenthesis(i):
                for right_string in self.generateParenthesis(n-i-1):
                    answer.append('(' + left_string + ')' + right_string)
        return answer
    
    #true bottom up dp solution:
    #instead of recursing on all possible permutations, we store all possibilities in each dp[i]
    def generateParenthesis2(self, n: int) -> list[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for k in range(1, n + 1):
            ans = []
            for i in range(k):
                for left in dp[i]:
                    for right in dp[k - i - 1]:
                        ans.append("(" + left + ")" + right)
            dp[k] = ans

        return dp[n]