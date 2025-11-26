class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        best_score = -1
        best_div = 0
        
        for d in divisors:
            score = 0
            for num in nums:
                if num % d == 0:
                    score += 1

            if score > best_score or (score == best_score and d < best_div):
                best_score = score
                best_div = d
        
        return best_div
