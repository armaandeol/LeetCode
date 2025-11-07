class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0]
        for s in stations:
            prefix.append(prefix[-1] + s)
        power = [prefix[min(n, i + r + 1)] - prefix[max(0, i - r)] for i in range(n)]
        
        def can(x):
            added = [0] * n
            curr_add = 0
            used = 0

            for i in range(n):
                if i - r - 1 >= 0:
                    curr_add -= added[i - r - 1]

                if power[i] + curr_add < x:
                    need = x - (power[i] + curr_add)
                    used += need
                    if used > k:
                        return False

                    pos = min(n - 1, i + r)
                    added[pos] += need
                    curr_add += need

            return True

        lo, hi = min(power), max(power) + k
        ans = lo

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans