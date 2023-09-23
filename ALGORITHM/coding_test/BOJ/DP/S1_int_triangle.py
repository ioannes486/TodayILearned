N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i+1):
        if 0 < j < i:
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        elif j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][0]
        else:
            dp[i][j] = dp[i][j] + dp[i - 1][i-1]

print(max(dp[N-1]))