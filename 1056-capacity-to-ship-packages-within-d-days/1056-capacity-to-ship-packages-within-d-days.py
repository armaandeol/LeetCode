class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            total = 0
            day_count = 1
            for w in weights:
                if total + w > capacity:
                    day_count += 1
                    total = w
                    if day_count > days:
                        return False
                else:
                    total += w
            return True

        left, right = max(weights),sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else :
                left = mid + 1
        return left