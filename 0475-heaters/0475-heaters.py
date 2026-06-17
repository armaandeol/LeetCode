class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        
        j = 0
        radius = 0

        for house in houses:

            while (
                j < len(heaters) - 1 and
                abs(heaters[j + 1] - house) <= abs(heaters[j] - house)
            ):
                j += 1

            radius = max(radius, abs(heaters[j] - house))

        return radius