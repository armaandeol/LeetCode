class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first_output = []
        second_output = []
        for i in s:
            if i != '#':
                first_output.append(i)
            else:
                if first_output:
                    first_output.pop()
        for i in t:
            if i != '#':
                second_output.append(i)
            else:
                if second_output:
                    second_output.pop()
        return first_output == second_output
        