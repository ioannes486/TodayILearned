import sys
import time


sys.stdin = open('column.txt', 'r')

start_time = time.time()    # 측정 시작

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


arr.sort()

lst = []
for i in arr:
    lst.append(i[1])
max_height = max(lst)

result = 0
for i in range(N):
    a = arr[0][0]
    height = arr[0][1]
    if height == max_height:
        break
    if arr[i+1][1] > height:
        b = arr[i+1][0]
        result += height * (b - a)
        height = arr[i+1][1]
        a = arr[i+1][0]

for i in range(N-1,-1,-1):
    a = arr[N-1][0]
    height = arr[N-1][1]
    if height == max_height:
        break
    if arr[i-1][1] > height:
        b = arr[i-1][0]
        result += height * (a-b)
        height = arr[i-1][1]
        a = arr[i-1][0]
result += max_height

print(result)
start_time = time.time()    # 측정 시작

# 프로그램 소스코드 ~~~~

end_time = time.time()    # 측정 종료

print("time : ", end_time - start_time)  # 수행시간 출력
print(result)