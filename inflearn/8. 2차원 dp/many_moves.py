import sys
sys.stdin = open('many_moves.txt','r')

def recur(y,x):

    for dy, dx in [[0,1],[0,-1],[1,0],[-1,0]]: # 움직이는 방향 설정
        ey = y + dy
        ex = x + dx

        if 0 <= ey < n and 0 <= ex < n:  # 움직인 후 그래프를 벗어나지 않을경우
            if graph[y][x] < graph[ey][ex]:  # 그 상태에서 움직인 좌표가 현재 좌표의 값보다 더 큰곳으로 이동할 때만

                return recur(ey,ex) + 1  # 조건을 만족하는 경우 이동횟수를 추가한다.
        return 0  # 모든 조건을 만족할 수 없을 경우 0을 반환한다.

# but, 이렇게 할 경우 한 가지 경우의 수만 계산 한 후 재귀함수는 돌아온다.
# 따라서 dp를 도입한다.

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