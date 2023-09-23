N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]
l1 = []
l2 = []
cnt = 0
result = 0
for i in range(1, N, 2):
    l1.append(arr[i])
    result += arr[i]

for j in range(0, N, 2):
    l2.append(arr[j])



print(l1,l2, result)


# for i in range(2, N):
#     if i < N-1:
#         if cnt == 2:
#             dp[i] = dp[i] + arr[i+2]
#             cnt = 0
#         else:
#             if dp[i] + dp[i+1] >= dp[i] + dp[i+2]:
#                 dp[i] = dp[i] + arr[i+1]
#                 cnt += 1
#             else:
#                 dp[i] = dp[i] + arr[i + 2]
#                 cnt = 0
#     else:
#         dp