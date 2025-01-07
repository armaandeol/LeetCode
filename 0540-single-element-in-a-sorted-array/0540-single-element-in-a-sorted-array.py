class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        number = Counter(nums)
        for key,value in number.items():
            if value != 2:
                return key