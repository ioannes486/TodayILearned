def recur_2(y, x):

    if dp[y][x] != 0:
        return dp[y][x]

    for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
        ey = y + dy
        ex = x + dx
        if 0 <= ey < n and 0 <= ex < n:
            if graph[y][x] < graph[ey][ex]:
                dp[y][x] = max(dp[y][x], recur_2(ey,ex) + 1)
    return dp[y][x]

n = int(input())
graph = [list(map(int, input().split()))for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        recur_2(y,x)

print(max(map(max, dp))+1)