class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        # Group by row and column
        for x, y in buildings:
            rows[y].append(x)
            cols[x].append(y)
        
        # Sort each list for binary search or easy neighbor check
        for key in rows:
            rows[key].sort()
        for key in cols:
            cols[key].sort()
        
        covered_count = 0
        
        for x, y in buildings:
            row = rows[y]
            col = cols[x]
            
            # Locate x in its row
            i = bisect.bisect_left(row, x)
            # Check left + right existence
            has_left = (i > 0)
            has_right = (i < len(row) - 1)
            
            # Locate y in its column
            j = bisect.bisect_left(col, y)
            # Check below + above existence
            has_below = (j > 0)
            has_above = (j < len(col) - 1)
            
            if has_left and has_right and has_below and has_above:
                covered_count += 1
        
        return covered_count