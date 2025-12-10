class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        to_find = sum(nums) % p
        if to_find == 0:
            return 0
        
        last_index = {0: -1}
        cur = 0
        min_len = n + 1
        
        for i, val in enumerate(nums):
            cur = (cur + val) % p
            need = (cur - to_find) % p
            if need in last_index:
                min_len = min(min_len, i - last_index[need])
            last_index[cur] = i

        return -1 if min_len > n - 1 else min_len