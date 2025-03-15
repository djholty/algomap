class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: #if you find land add 4 to the perimeter
                    perimeter += 4
                    for i_off, j_off in [(0,1), (0,-1), (1, 0), (-1,0)]: 
                        #look at the squares to the sides and above/below and if they are in bounds and also land, then adjust the perimeter by subtracting 1
                        r, c = i + i_off, j + j_off
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                            perimeter -= 1
        return perimeter
        
