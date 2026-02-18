class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        return self.val(high, k) - self.val(low-1, k)
    def val(self, H, k):
        memo = {}
        digits = str(H)
        def dp(divi, zeros, pos, even_c, odd_c, tight):
            n = len(digits)
            if n == pos:
                if (not divi) and (not zeros) and (even_c == odd_c):
                    return 1
                else:
                    return 0
            key = (divi, zeros, pos, even_c, odd_c, tight)
            if key in memo:
                return memo[key]
            limit = 9
            if tight:
                limit = int(digits[pos])
            total = 0
            for d in range(limit + 1):
                next_zeros = zeros
                if not (zeros and d == 0):
                    next_zeros = False
                new_even_c = even_c
                new_odd_c = odd_c
                next_divi = divi
                if not next_zeros:
                    next_divi = (divi * 10 + d) % k
                    if d % 2 == 0:
                        new_even_c = even_c + 1
                    else:
                        new_odd_c = odd_c + 1
                if tight:
                    if d == limit:
                        new_tight = True
                    else:
                        new_tight = False
                else:
                    new_tight = False
                
                total += dp(next_divi, next_zeros, pos+1, new_even_c, new_odd_c, new_tight)
            memo[(divi, zeros, pos, even_c, odd_c, tight)] = total
            return total

                
        return dp(0, True, 0, 0, 0, True)