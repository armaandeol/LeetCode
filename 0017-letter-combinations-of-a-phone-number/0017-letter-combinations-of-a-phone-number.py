class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        ans,sol = [],[]

        letter_map = {
            '2':'abc','3':'def','4':'ghi','5':'jkl',
            '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }


        n= len(digits)

        def backtrack(a=0):
            if a ==n:
                ans.append("".join(sol))
                return
            for letter in letter_map[digits[a]]:
                sol.append(letter)
                backtrack(a+1)
                sol.pop()
        backtrack(0)
        return ans