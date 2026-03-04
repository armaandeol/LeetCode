class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        m,n = len(mat),len(mat[0])
        def check(a,m,n,mat):
            ones = 0 
            for i in range(m):
                for j in range(1):
                    if mat[i][a] == 1:
                        ones += 1
            if ones > 1:
                return False
            else:
                return True

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if mat[i].count(1) <= 1 and check(j,m,n,mat):
                        count += 1
        return count 
