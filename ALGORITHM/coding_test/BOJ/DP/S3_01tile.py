N = int(input())

dp = [0 for _ in range(N)]
if N == 1:
    dp[-1] = 1
else:
    dp[0] = 1
    dp[1] = 2
    for i in range(2, N):
        dp[i] = dp[i-1] + dp[i-2]
        if dp[i] >= 15746:
            dp[i] = dp[i] % 15746  # 15746보다 커지면 계산 시간 늘어나므로 미리 나머지 계산
print(dp[-1])