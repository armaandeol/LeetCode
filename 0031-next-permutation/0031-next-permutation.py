class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        right = len(nums) - 1
        while right > 0 and nums[right - 1] >= nums[right]:
            right -= 1

        if right == 0:
            nums.reverse()
            return nums

        pivot = right - 1
        successor = len(nums) - 1
        while nums[successor] <= nums[pivot]:
            successor -= 1


        nums[pivot], nums[successor] = nums[successor], nums[pivot]


        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        