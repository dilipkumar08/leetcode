class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        log=set()

        def check(i,j):
            if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in log:
                return 0

            log.add((i,j))

            res=check(i,j+1)
            res+=check(i+1,j)
            res+=check(i,j-1)
            res+=check(i-1,j)

            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return check(i,j)
