'''

r g b
인덱스 0번 색을 택했으면 다음 루프에는 1번 집을 택할 수 없다.
모든 집을 칠하는 최솟값을 출력하기
집을 칠하는 비용은 1000보다 작거나 같은 자연수 => 초기 최솟값은 최댓값은 1000


'''
# 재귀함수 풀이
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 1000*1000
dp = arr[0]

# def recur(idx, sum, ex):
#     global result
#     if idx == N:
#         dp.append(sum)
#         return
#
#     for i in range(3):
#         if ex != i:
#             recur(idx+1, sum+arr[idx][i], i)
# recur(0, 0, 0)
# recur(0,0,1)
# recur(0,0,2)
# print(min(dp))
# print(dp)

#