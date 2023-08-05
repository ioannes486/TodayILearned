import sys
sys.stdin = open('napsag.txt','r')

def recur(idx, weight, value):
    global answer

    # 최대 무게에 알맞게 선택한경우
    # if weight <= B:
    #     answer = max(answer, value)
    #     return

    # 가방이 터진 경우
    if weight > B:

        return

    # 아무것도 선택하지 않은 경우
    if idx == A:
        answer = max(answer, value)
        return

    # 담았을 때
    recur(idx + 1, weight + bags[idx][0], value + bags[idx][1])
    # 안담았을 때
    recur(idx + 1, weight, value)


A, B = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(A)]
answer = 0
recur(0,0,0)
# print(A, B, bags)
print(answer)