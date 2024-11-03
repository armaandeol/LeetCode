class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        x = len(height)
        max_left = [0]*x
        max_right = [0]*x

        for i in range(x):
            j = -i-1
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        total = 0
        for i in range(x):
            pot = min(max_left[i], max_right[i])
            total += max(0,pot - height[i])
        return total
        