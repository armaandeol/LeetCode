class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first_output = []
        second_output = []
        for i in range(max(len(s), len(t))):
            if i < len(s):
                if s[i] != '#':
                    first_output.append(s[i])
                elif first_output:
                    first_output.pop()

            if i < len(t):
                if t[i] != '#':
                    second_output.append(t[i])
                elif second_output:
                    second_output.pop()
        return first_output == second_output
        