class Solution:
    def sortVowels(self, s: str) -> str:
        stack = ['a','e','i','o','u','A','E','I','O','U']
        temp = []
        count = []
        ans = []
        for i,j in enumerate(s):
            if j in stack:
                temp.append(j)
                count.append(i)
        temp = sorted(temp)
        for i in s:
            if i in stack:
                i = temp.pop(0)
            ans.append(i)
        return "".join(ans)
        