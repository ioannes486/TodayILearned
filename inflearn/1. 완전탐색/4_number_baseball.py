n = int(input())

hint = [list(map(int, input().split())) for _ in range(4)]  # 루프를 네번 돌아서 4줄의 입력을 하나의 배열 형태로 받아온다.

answer = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (i == j) or (i == k) or (j == k):  # 다른 숫자로 이루어진 세자리수 생성
                continue
            
            cnt = 0
            for arr in hint:
                number = arr[0]
                ball = arr[1]
                strike = arr[2]

                ball_count = 0
                strike_count = 0
                
                if ball == ball_count and strike == strike_count:
                    cnt +=1
            if cnt == 4:
                answer += 1
print(answer)

from itertools import permutations
def solution(baseball):
    perm = permutations([i for i in range(1,10)],3)
    sum = 0
    for p in perm:
        ans = list(p)
        cnt = 0
        for b in baseball:
            strike = 0
            ball = 0
            test = list(manp)
