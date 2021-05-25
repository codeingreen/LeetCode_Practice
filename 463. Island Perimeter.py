class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # total borders for the cells 
        # if grid[i-1][j] != 1 and grid[i+1][j] != 1 
        # and grid[i][j-1] !=1 and grid[i][j+1] != 1:
        # then count +=4
        
        # Else
        # counter = 0
        # for x, y in zip([[i-1, j], [i+1, j], [i, j-1], [i, j+1]]):
        #            counter += grid[x][y]
        # total += 4 - counter
        
        
        i = 0
        j = 0
        
        total = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
            
                # add first and then subtract
                if grid[i][j] == 1:
                    total +=4
                    
                    if i > 0 and grid[i-1][j] == 1:
                        total -=2

                    if j > 0 and grid[i][j-1] == 1:
                        total -=2
                        
        return total
                    
                    
            
        
