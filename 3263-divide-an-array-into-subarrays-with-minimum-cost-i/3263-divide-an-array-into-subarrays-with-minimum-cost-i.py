class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        summ = nums[0]
        nums.remove(nums[0])
        for i in range(2):
            summ += min(nums)
            nums.remove(min(nums))
        return summ 
