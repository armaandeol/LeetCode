class Solution:
    def checkValidString(self, s: str) -> bool:
        minn = maxx = 0
        for i in s:
            maxx = maxx - 1 if i == ')' else maxx + 1
            minn = minn + 1 if i == '(' else max(minn-1,0)
            if maxx < 0 :
                return False
        return minn == 0