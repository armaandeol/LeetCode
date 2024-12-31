class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d = Counter(nums)
        for key,value in d.items():
            if value != 2:
                return key