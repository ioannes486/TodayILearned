# import sys
# sys.stdin = open('top_down.txt', 'r')

def recur(idx):

    global answer  # 재귀함수이므로 함수안에 answer를 정의할경우 재귀할때마다 변수가 초기화된다.
    if idx == N:
        return  0  # 재귀 깊이가 최대치일 경우 0을 리턴, 가장 큰 인덱스(가장 깊은 재귀깊이)에서 부터 계산하면서 올라온다
                   # 7부터 계산하므로 dp테이블의 가장 마지막 인덱스부터 계산됨
    if idx > N:
        return -999999999  # 만약 인덱스를 넘어가면 -99999로 값을 리턴하여 max 연산을 실행했을때 값이 그대로 -1이 되게 한다.
    if dp[idx] != -1:
        return dp[idx]  # 이미 저장되어 있다면 다시 방문할 필요가 없다.

    # 상담을 받거나, 안받거나, 그 중에서 더 많은 돈을 버는 경우를 내 dp테이블에 저장하겠다!
    dp[idx] = max(recur(idx + interview[idx][0]) + interview[idx][1], recur(idx+1))  # 함수의 리턴값을 돈으로 설정해 생성한다

    return dp[idx]  # 상위재귀함수에 하위재귀함수를 더하려면 리턴값을 해당 idx로 해야한다.


N = int(input())
interview = [list(map(int, input().split())) for _ in range(N)]
dp = [-1 for _ in range(N)]
answer = 0
recur(0)
# print(dp)
print(dp[0])