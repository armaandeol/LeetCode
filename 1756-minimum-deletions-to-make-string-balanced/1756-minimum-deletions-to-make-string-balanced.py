class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        ans = []
        for i in range(1,len(s)+1):
            if s[-i] == 'b' and ans:
                if ans[-1] == 'a':
                    ans.pop()
                    count += 1
            else:
                ans.append(s[-i])
        return count