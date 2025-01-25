class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def mod_exp(base, exp, mod):
            if exp == 0:
                return 1
            half = mod_exp(base, exp // 2, mod)
            half = (half * half) % mod
            return (half * base) % mod if exp % 2 else half

        even_count = (n + 1) // 2
        odd_count = n // 2

        even_part = mod_exp(5, even_count, MOD)
        odd_part = mod_exp(4, odd_count, MOD)

        return (even_part * odd_part) % MOD