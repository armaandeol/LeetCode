class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n = len(dimensions)
        diagonal,area = [0]*n,[0]*n
        for i in range(n):
            length,width = dimensions[i][0],dimensions[i][1]
            diagonal[i] = length**2 + width**2
            area[i] = length*width
        
        a = max(diagonal)
        indexes = [i for i, val in enumerate(diagonal) if val == a]

        maxi = -1
        for i in indexes:
            maxi = max(area[i],maxi)

        return maxi