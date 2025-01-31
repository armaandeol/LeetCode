class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        minsum = 0
        stack = []
        
        for next_smaller in range(n + 1):
            while stack and (next_smaller == n or arr[stack[-1]] > arr[next_smaller]):
                i = stack.pop()
                prev_smaller = stack[-1] if stack else -1
                minsum += arr[i] * (next_smaller - i) * (i - prev_smaller)
                minsum %= MOD  
            stack.append(next_smaller)
        
        return minsum
