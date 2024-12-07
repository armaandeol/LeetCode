class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        prev_num = None
        Unique = True
        for num in nums:
            if num == prev_num:
                Unique = False
            else:
                Unique = True
            prev_num = num
            if Unique:
                nums[k] = num
                k += 1
                Unique = False
        return k
        
        