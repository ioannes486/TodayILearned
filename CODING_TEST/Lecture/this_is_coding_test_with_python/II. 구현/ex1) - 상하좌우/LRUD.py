import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:  # 이동 계획을 하나씩 확인
    for i in range(len(move_types)):  # 해당하는 이동방법을 찾고 해당하는 인덱스를 찾아서 움직이기
        if plan == move_types[i]:  #
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)

