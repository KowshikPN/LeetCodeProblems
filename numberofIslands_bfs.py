import queue
def bfs(grid,q):
    cor = [[0,1],[1,0],[-1,0],[0,-1]]
    while q.qsize() != 0:
        cur = q.get()
        for i in range(len(cor)):
            x = cur[0]+cor[i][0]
            y = cur[1]+cor[i][1]
            
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "0":
                continue
                
            q.put([x,y])
            grid[x][y] = "0"
            
def numIslands(grid):
    if len(grid) == 0:
        return 0
    
    count = 0
    q = queue.Queue()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                count += 1
                grid[i][j] = "0"
                q.put([i,j])
                bfs(grid,q)
                
    return count

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
output = numIslands(grid)
print(output)


    