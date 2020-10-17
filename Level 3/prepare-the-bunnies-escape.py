def solution(maze):
    n = len(maze)
    m = len(maze[0])

    # i -> row, j -> col, k -> wallBreak left or not
    vis = [[[False for k in range(2)] for j in range(m)] for i in range(n)]
    queue = [(0, 0, 1, 1)]

    vis[0][0][1] = True
    ans = 1

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    while queue:
        
        s = queue.pop(0) 

        if s[0] == n-1 and s[1] == m-1:
            return s[2]
            
        for i in range(4):

            nx = s[0] + dx[i]
            ny = s[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m:

                if vis[nx][ny][s[3]] == True:
                    continue
                
                if nx == n-1 and ny == m-1:
                    return s[2] + 1
            
                if maze[nx][ny] == 1 and s[3] == 1:
                    # if wall broken at nx, ny
                    vis[nx][ny][1] = True
                    queue.append((nx,ny,s[2] + 1, 0))
                
                elif maze[nx][ny] == 0:
                    vis[nx][ny][s[3]] = True
                    queue.append((nx,ny,s[2] + 1, s[3]))
    

if __name__ == "__main__":
    maze = [
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ]
    print(solution(maze))

    maze = [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0]
    ]
    print(solution(maze))