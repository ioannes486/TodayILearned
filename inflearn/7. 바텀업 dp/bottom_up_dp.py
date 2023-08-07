import sys
sys.stdin = open('bottom_up.txt', 'r')

N = int(input())
interview = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for idx in range(N+1)[::-1]:
    # 인덱스가 N을 넘어가면 하나 더해라
    if idx + interview[idx][0] > N:
        dp[idx] = dp[idx+1]

    # 선택한 것과 선택하지 않은 것중 하나를 골라서 max에 넣어라
    else:
        dp[idx] = max(dp[idx + interview[idx][0]] + interview[idx][1], dp[idx+1])