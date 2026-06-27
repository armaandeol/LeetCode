class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        if 1 in freq:
            ans = max(ans, freq[1] if freq[1] % 2 else freq[1] - 1)

        for i in list(freq.keys()):
            if i == 1:
                continue
            
            curr = i
            length = 0

            while freq.get(curr,0) >= 2:
                length += 2
                curr = curr * curr
            if freq.get(curr,0) >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans,length)
        return ans