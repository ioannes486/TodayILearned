'''
재귀함수를 사용할 때는 매개변수의 변화를 많이 활용할 것


'''

def recur(idx, sin, sun, use):
    global answer

    if idx == n:  # 인덱스가 n에 도달하면 재귀를 종료한다.
        if use > 0: # 하나 이상의 재료를 사용한 경우에만 단짠 차이를 구해준다.
            answer = min(answer, abs(sin - sun))
        return

    # 재료를 사용하는 경우와 사용하지 않는 경우 두가지를 나누기
    # 1. 사용하는 경우 짠맛에 1을 곱하고 단맛에 1을 더한다. 그 다음 인덱스를 하나 높여준다.
    recur(idx + 1, sin * foods[idx][0], sun + foods[idx][1], use+1)

    # 2. 사용하지 않는 경우 수치를 변화시키지 않고 인덱스만 하나 높여준다
    recur(idx + 1, sin, sun, use)

n = int(input())

foods = [() for _ in range(n)]

for i in range(n):
    a,b = map(int, input().split())
    foods[i] = (a,b)

answer = 1e9
recur(0,1,0,0)
print(answer)
