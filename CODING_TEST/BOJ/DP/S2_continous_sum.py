import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))


def lcs(nums):
    current_value = 0
    max_value = -10**8
    for num in nums:
        current_value = max(current_value + num, num)
        # 현재 값과 다음 값의 가장 큰 
        max_value = max(max_value, current_value)
    return max_value

print(lcs(arr))
# dp =[[0 for _ in range(N+1)]for _ in range(N+1)]
# for i in range(N):
#     for j in range(i, N):
#         dp[i][i] = arr[i]
#         dp[i][j] = arr[j] + dp[i][j-1]
# # print(dp)
# print(max(map(max,dp)))