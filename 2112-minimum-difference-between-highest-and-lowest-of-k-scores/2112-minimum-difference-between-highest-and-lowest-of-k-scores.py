class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        dis = float('inf')
        
        for i in range(len(nums)-k+1):
            if not nums[i+k-1]:
                pass
            else:
                dis = min(dis,abs(nums[i]-nums[i+k-1]))
        return dis