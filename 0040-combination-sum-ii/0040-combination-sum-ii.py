class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        candidates.sort()

        def helper(ind, target):
            if target == 0:
                sol.append(res[:])
                return
            for i in range(ind,len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                res.append(candidates[i])
                helper(i+1,target-candidates[i])
                res.pop()
        helper(0,target)
        return sol