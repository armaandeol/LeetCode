class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        numbers = candidates
        n = len(numbers)

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return

            if curr_sum > target or i == n:
                return

            backtrack(i+1, curr_sum)

            sol.append(numbers[i])
            backtrack(i, curr_sum+numbers[i])
            sol.pop()

        backtrack(0, 0)
        return res
