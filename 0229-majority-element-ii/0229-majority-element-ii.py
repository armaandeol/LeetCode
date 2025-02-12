class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        ans = []

        counter = Counter(nums)

        for num, count in counter.items():
            if count > n:
                ans.append(num)

        return ans