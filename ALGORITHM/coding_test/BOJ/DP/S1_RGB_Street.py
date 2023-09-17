'''

r g b
인덱스 0번 색을 택했으면 다음 루프에는 1번 집을 택할 수 없다.
모든 집을 칠하는 최솟값을 출력하기
집을 칠하는 비용은 1000보다 작거나 같은 자연수 => 초기 최솟값은 최댓값은 1000


'''

N = int(input)
arr = [map(int, input().split()) for _ in range(N)]

result = 1000
cost = 0

def recur(idx, sum):
    global result
    if idx == N-1:
        result = min(sum, result)
        return result

    recur(idx+1, sum+arr[idx][0])
    recur(idx+1, sum+arr[idx][1])
    recur(idx+1, sum+arr[idx][2])

recur(0, 0)
print(result)
