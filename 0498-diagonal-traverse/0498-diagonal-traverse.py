class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        i, j = 0, 0
        Direction = 0  # 0 = UP, 1 = DOWN
        output = []

        while len(output) < n * m:
            output.append(mat[i][j])

            if Direction == 0:  # moving UP
                if j == m - 1:  # hit right boundary
                    i += 1
                    Direction = 1
                elif i == 0:  # hit top boundary
                    j += 1
                    Direction = 1
                else:  # normal up-right move
                    i -= 1
                    j += 1

            else:  # moving DOWN
                if i == n - 1:  # hit bottom boundary
                    j += 1
                    Direction = 0
                elif j == 0:  # hit left boundary
                    i += 1
                    Direction = 0
                else:  # normal down-left move
                    i += 1
                    j -= 1

        return output
