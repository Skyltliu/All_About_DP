from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        def z_function(s: str) -> List[int]:
            n = len(s)
            z = [0] * n
            l = r = 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z

        def jump(nums: List[int]) -> int:
            res = 0
            l = r = 0
            while r < len(nums):
                farthest = 0
                for i in range(l, r+1):
                    farthest = max(farthest, i + nums[i])
                if farthest == r:
                    return -1
                l = r+1
                r = farthest
                res += 1
            return res

        n = len(target)
        prefixes = [0] * n
        for w in words:
            z = z_function(w + "#" + target)
            off = len(w) + 1
            for i in range(off, len(z)):
                prefixes[i - off] = max(prefixes[i - off], z[i])

        return jump(prefixes)