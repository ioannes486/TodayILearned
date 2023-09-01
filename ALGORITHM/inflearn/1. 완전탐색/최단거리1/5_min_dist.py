import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

coordinates = [list(map(int, input().split())) for i in range(N)]

print(coordinates)
# 좌표 생성
# 각 점간의 x거리 구하기
x_dist_list = []
for i in range(len(coordinates)):
    lst = []
    for j in range(len(coordinates)):
        lst.append(abs(coordinates[i][0] - coordinates[j][0]))
    x_dist_list.append(lst)

# 각 점간의 y거리 구하기
y_dist_list = []
for i in range(len(coordinates)):
    lst = []
    for j in range(len(coordinates)):

        lst.append(abs(coordinates[i][1] - coordinates[j][1]))
    y_dist_list.append(lst)

print(x_dist_list)
print(y_dist_list)
# for x in range(1000001):
#     for y in range(1000001):
#         dist = 10000000
#         dist_sum = 0
#
#         # 거리 합 구하기
#         for i in range(N):
#             dist_sum += (int(coordinates[i][0])-x)**2 + \
#                 (int(coordinates[i][1])-y)**2
#
#         # 비교해서 더 짧은 거리 구하기
#         dist = min(dist, dist_sum)
#print(dist)
