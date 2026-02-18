class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        count = 0
        index = 0
        countr = [0] * (len(s2) + 1)
        indexr = [0] * (len(s2) + 1)
        for i in range(n1):
            for j in range(len(s1)):
                if s1[j] == s2[index]:
                    index += 1
                if index == (len(s2)):
                    index = 0
                    count += 1
            countr[i] = count
            indexr[i] = index
            for k in range(i):
                if indexr[k] == index:
                    pre_count = countr[k]
                    pattern_count = (countr[i] - countr[k]) * ((n1 - k - 1) // (i - k))
                    remain_count = countr[k + (n1 - k - 1) % (i - k)] - countr[k]
                    return (pre_count + pattern_count + remain_count) // n2
        return countr[n1 - 1] // n2
