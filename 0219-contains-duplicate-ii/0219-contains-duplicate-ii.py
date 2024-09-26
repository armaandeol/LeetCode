class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
    
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            
            # Add current element to the set
            window.add(nums[i])
            
            # Maintain window size of at most k
            if len(window) > k:
                window.remove(nums[i - k])
        
        return False
        