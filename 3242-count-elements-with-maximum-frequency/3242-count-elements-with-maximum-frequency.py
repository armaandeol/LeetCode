from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        max_freq = 0
        freq = 0

        for num, count in freq_map.items():
            if count > max_freq:
                max_freq = count
                freq = count
            elif count == max_freq:
                freq += count 
        
        return freq