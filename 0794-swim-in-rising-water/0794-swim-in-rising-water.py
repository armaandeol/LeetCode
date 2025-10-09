class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        pq = [(grid[0][0], 0, 0)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while pq:
            elevation, r, c = heappop(pq)
            if (r, c) == (n-1, n-1):
                return elevation
            
            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_elev = max(elevation, grid[nr][nc])
                    heappush(pq, (new_elev, nr, nc))
