class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        rangu = [-1,-1]
        status1,status2 = True, True
        for i in range(len(nums)):
            if nums[i] == target and status1:
                rangu[0] = i
                status1 = False

            if nums[-i-1] == target and status2:
                rangu[1] = len(nums)-i-1
                status2 = False

            if not status1 and not status2:
                return rangu
        return rangu