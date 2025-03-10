def solution(grid):
    h = len(grid[0])
    v = len(grid)
    
    array = [[[0, 0, 0, 0] for i in range(h)] for j in range(v)]
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    answer = []
    
    for i in range(v):
        for j in range(h):
            for k in range(4): 
                if array[i][j][k] == 0:
                    x,y,z = i,j,k
                    tmp = 0
                    while(array[x][y][z] == 0):
                        array[x][y][z] = 1
                        x, y = (x + direction[z][0]) % v, (y + direction[z][1]) % h
                        if grid[x][y] == 'R':
                            z = (z-2)%4
                            z = (z + 1) % 4
                        elif grid[x][y] == 'L':
                            z = (z-2)%4
                            z = (z - 1) % 4
                        tmp +=1
                    answer.append(tmp)
    return sorted(answer)