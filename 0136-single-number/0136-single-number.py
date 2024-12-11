class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f = defaultdict(int)
        for ch in  nums:
            f[ch] += 1
        for key, value in f.items():
            if value == 1:
                return key
        