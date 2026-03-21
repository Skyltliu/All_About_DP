from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}
        for i in range(len(s)-1, -1, -1):
            valid = []
            for j in range(i, len(s)):
                subword = s[i : j+1]
                if j == len(s)-1:
                    if self.inDict(subword, wordDict):
                        valid.append(subword)
                else:
                    sentences = dp.get(j+1, [])
                    for sentence in sentences:
                        if self.inDict(subword, wordDict):
                            appendword = subword + " " + sentence
                            valid.append(appendword)
            dp[i] = valid
        return dp.get(0, [])
    def inDict(self, word, Dict):
        return word in Dict