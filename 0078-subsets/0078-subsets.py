class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res,sol = [],[]

        def backtrack(x):
            if x == n:
                res.append(sol[:])
                return 
            
            backtrack(x+1)

            sol.append(nums[x])
            backtrack(x+1)
            sol.pop()


        backtrack(0)
        return res