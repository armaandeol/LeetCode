class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        def get_diagonal(i, j):
            vals = []
            while i < n and j < n:
                vals.append(grid[i][j])
                i += 1
                j += 1
            return vals

        def set_diagonal(i, j, vals):
            k = 0
            while i < n and j < n:
                grid[i][j] = vals[k]
                k += 1
                i += 1
                j += 1

        for i in range(n):
            vals = get_diagonal(i, 0)
            vals.sort(reverse=True)  # descending
            set_diagonal(i, 0, vals)

        for j in range(1, n):
            vals = get_diagonal(0, j)
            vals.sort()  # ascending
            set_diagonal(0, j, vals)

        return grid
