import sys
sys.stdin = open('consultant.txt', 'r')

def recur(idx, price):

    global answer  # 재귀함수이므로 함수안에 answer를 정의할경우 재귀할때마다 변수가 초기화된다.
    if idx == N-1:
        answer = max(answer, price)
        return  # idx가 0부터 시작하므로
    if idx > N-1:
        return

    # 상담을 할 경우
    recur(idx + interview[idx][0], price+interview[idx][1])

    # 상담을 하지 않을 경우
    recur(idx+1, price)

N = int(input())
interview = [list(map(int, input().split())) for _ in range(N)]
answer = 0
recur(0,0)
print(interview)
print(answer)