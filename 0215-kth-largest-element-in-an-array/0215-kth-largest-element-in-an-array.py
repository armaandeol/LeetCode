class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        a = heapq.heappop(nums)
        return -a
        