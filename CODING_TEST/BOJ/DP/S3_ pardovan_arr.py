T = int(input())



for _ in range(T):
    N = int(input())
    if N <= 10:
        dp = [1,1,1,2,2,3,4,5,7,9]
        print(dp[N-1])
    else:
        dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
        dp.extend([0]*(N-10))
        for i in range(10, N):
            dp[i] = dp[i-3] + dp[i-2]
        print(dp)



