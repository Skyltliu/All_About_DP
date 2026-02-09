from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        answer = []
        
        for i in range(n):
            for left_string in self.generateParenthesis(i):
                for right_string in self.generateParenthesis(n-i-1):
                    answer.append('(' + left_string + ')' + right_string)
        return answer