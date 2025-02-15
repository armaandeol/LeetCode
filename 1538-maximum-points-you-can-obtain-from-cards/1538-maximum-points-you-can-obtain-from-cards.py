class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        
        total_sum = sum(cardPoints)

        min_subarray_sum = float('inf')
        current_subarray_sum = 0
        window_size = n - k

        for i in range(n):
            current_subarray_sum += cardPoints[i]

            if i >= window_size - 1:
                min_subarray_sum = min(min_subarray_sum, current_subarray_sum)
                current_subarray_sum -= cardPoints[i - (window_size - 1)]

        return total_sum - min_subarray_sum