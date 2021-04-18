from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

answer = 0

def bfs(maze, pos, visited):
    global answer
    global n, m
    y, x = pos
    visited[y][x] = True

    queue = deque()
    queue.append((y, x))
   
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        y, x = queue.popleft()
       
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                maze[ny][nx] = maze[y][x] + 1
                queue.append((ny, nx))
            
    return maze[n-1][m-1]
    
visited = [[False] * m for _ in range(n)]
print(bfs(maze, [0, 0], visited))
