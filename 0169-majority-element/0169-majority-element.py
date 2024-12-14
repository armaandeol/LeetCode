class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = defaultdict(int)
        for num in nums:
            a[num] += 1
        prev,max = 0,0
        for key,value in a.items():
            if value > prev:
                if value > max:
                    max = value
                    b = key
                    prev = value
        return b
        