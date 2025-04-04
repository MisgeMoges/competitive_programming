class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        xy_area = 0
        
        xz_area = 0
        
        yz_area = 0
        
        for i in range(n):
            max_row = 0
            max_col = 0
            
            for j in range(n):
                if grid[i][j] > 0:
                    xy_area += 1
                max_row = max(max_row, grid[i][j])
                max_col = max(max_col, grid[j][i])
            xz_area += max_row
            yz_area += max_col
        return xy_area + xz_area + yz_area