from functools import cache
from typing import List

#Standard dp with memo:
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        @cache
        def is_concatenated(word, count):
            if not word:
                return count >= 2
            for i in range(1, len(word) + 1):
                if word[:i] in d:
                    if is_concatenated(word[i:], count + 1):
                        return True
            return False
        res = []
        for w in words:
            if w:
                if is_concatenated(w, 0):
                    res.append(w)
        return res
    
#bottom up dp:
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        res = []
        for word in words:
            if not word:
                continue
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in d and i-j < len(word):
                        dp[i] = True
                        break
            if dp[len(word)]:
                res.append(word)
        return res