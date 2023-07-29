from collections import deque
n,m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

maxi = 0  # 가장 먼 두점의 거리

# bfs
for y in range(n):
    for x in range(m):
        if graph[y][x] == 'L':
            visited = [[0 for _ in range(m) for _ in range(n)]]
            dist = [[0 for _ in range(m) for _ in range(n)]]

            q = deque() # pop과 append가 양쪽에서 가능한 친구
            q.append([y,x])
            visited[y][x] = 1

            while q:
                ey, ex = q.popleft()

                for dy, dx in  [[0,1], [0,-1],[1,0],[-1,0]]:
                    ny, nx = ey + dy, ex + dx
                    if 0 <= ny < n and 0 <= nx < m:
                        if graph[ny][nx]=='L':
                            if visited[ny][nx] == 0:
                                dist[ny][nx] = dist[ey][ex] + 1
                                q.append(ny, nx)
                            if maxi < dist[ny][nx]:
                                maxi = dist[ny][nx]              
print(maxi)