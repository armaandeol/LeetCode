class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key,value in count.items():
            if value != 2:
                return key