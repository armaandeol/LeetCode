class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        travel = [0]
        for i in gain:
            travel.append(travel[-1] + i)
        return max(travel)