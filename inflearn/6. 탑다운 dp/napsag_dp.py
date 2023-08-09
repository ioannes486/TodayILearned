import sys
sys.stdin = open('napsag.txt','r')

# 냅색문제 :
def recur(idx, weight):
    # 고려할 요소 = 인덱스와 가방의 무게
    # 산출값 = 물건의 가치 최댓값
    # 고려해야 할 요소가 두가지이기 때문에 2차원 dp를 활용한다.

    if weight > B:
        return -999999999
    if idx == A:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx][weight] = max(recur(idx + 1, weight + bags[idx][0]) + bags[idx][1], recur(idx + 1, weight))

    return dp[idx][weight]

A, B = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(A)]
dp = [[-1 for _ in range(100001)] for _ in range(A)]
# weight를 처리하기 위해 dp테이블을 2차원으로 만들어준다.
# 임의의 weight가 범위를 10001로 가지고 있다고 생각하고 설정하기

recur(0,0)

print(dp[0][0])