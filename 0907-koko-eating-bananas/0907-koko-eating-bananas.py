class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateTotalHours(piles, hourly):
            totalH = 0
            for pile in piles:
                totalH += math.ceil(pile / hourly)
            return totalH

        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if calculateTotalHours(piles, mid) <= h:
                right = mid  
            else:
                left = mid + 1 

        return left