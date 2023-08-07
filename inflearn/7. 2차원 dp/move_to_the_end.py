import sys
sys.stdin = open('move_to_the_end.txt','r')

def recur(y,x):
    # 구하려는 것 : 경우의 수

    if x == (m-1) and y == (n-1):
        return 1

    if dp[y][x] != -1:  # 이 조건을 0이 아닐 때로 해놓을 경우 계산 값이 0이면 이 부분의 순회를 다시 하게 된다. 따라서 -1로 해준다.
        # 이걸 -1로 해놓으면 0을 활용할 수 없지 않을까?
        # 조건을 만족하는 값에 대해 해당 dp좌표에 값을 더하는게 아니라 할당하는거라서 -1로 해놓아도 된다.
        return dp[y][x]

    point = 0  # 함수안에 있는 변수이므로 함수가 재귀적으로 반복됨에 따라서 계속 초기화 되지 않을까?
    # 재귀 되는 함수는 각 깊이 만의 스코프를 가지고 있다. 따라서 맨 바깥쪽 변수와는 상관이 없다.
    for dy, dx in [1,0],[-1,0],[0,1],[0,-1]:
        ey = y + dy
        ex = x + dx
        if 0 <= ey < n and 0 <= ex < m:
            if graph[y][x] > graph[ey][ex]:
                point += recur(ey, ex)
    dp[y][x] = point  # 계산을 할 때마다  포인트 값을 기억한 후 값을 할당한다.
    return dp[y][x]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]  #

print(recur(0,0))
print(dp)