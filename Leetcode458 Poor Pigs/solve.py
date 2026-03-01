class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
            turns = minutesToTest // minutesToDie
            pigs = 0
            states = turns + 1
            while True:
                if states ** pigs >= buckets:
                    break
                pigs += 1
            return pigs