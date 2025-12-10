class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mini = complexity[0]
        if mini in complexity[1:]:
            return 0
        
        # for i in range(1,len(complexity)):
        #     if complexity[0] > complexity[i]:
        #         return 0
        if mini > min(complexity):
            return 0
        
        n = len(complexity) - 1
        ans = 1
        while n != 0:
            ans *= n
            n -= 1
        MOD = 10**9 + 7 
        return ans % MOD