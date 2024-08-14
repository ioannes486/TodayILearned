import sys
sys.stdin = open('input.txt', 'r')

# 내 답안
data = []
n, m = map(int, input().split())

# data를 2차원 배열 형태로 먼저 저장
for _ in range(n):
    row = list(map(int, input().split()))
    data.append(row)

# for 문 사용
result = 0
for row in data:
    row.sort()
    min_num = row[0]
    if result < min_num:
        result = min_num
    else:
        continue

# 모범 답안 숏코딩
result = 0
for i in range(n):
    data = list(map(int, input().split))  # data를 따로 저장하기 전에 for문 돌림 - 동등한 레벨의 for문이 두개라면 한번만 쓰는 것을 고려해보자
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 변수 재할당이 아닌 최댓값 함수를 이용해서 바꾸기
    result = max(result, min_value)

# 이중 for 문을 쓰는 경우
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
        result = max(result, min_value)
print(result)

print(n, m, data)
print(result)