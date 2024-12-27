class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        i = len(nums) // 3
        ans = []

        counter = Counter(nums)

        for num, count in counter.items():
            if count > i:
                ans.append(num)

        return ans