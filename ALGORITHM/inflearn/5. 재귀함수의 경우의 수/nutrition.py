import sys
sys.stdin = open('nutrition.txt', 'r')


def recur(idx, A, B, C, D, E):
    global answer
    if A <= a and B <= b and C <= c and D <= d:
        answer = min(answer, E)
        return
    if idx == N:
        return


    # 영양소를 선택하는 경우
    recur(idx+1, A+ingre[idx][0], B+ingre[idx][1], C+ingre[idx][2], D+ingre[idx][3], E+ingre[idx][4])

    # 선택하지 않은 경우
    recur(idx+1, A, B, C, D, E)


N =int(input())
a,b,c,d = list(map(int, input().split()))
ingre = [list(map(int, input().split())) for _ in range(N)]
answer = 9999999999
recur(0,0,0,0,0,0)
print(answer)

# git add
