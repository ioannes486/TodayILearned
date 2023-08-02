import sys
sys.stdin = open('input.txt', 'r')

N = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N+1)]

# 앞에서 부터 수를 더하는데 더한수보다 arr의 i번째 항이 큰 경우 숫자를 갱신하기
for i in range(N):
    prefix[i+1] = max(prefix[i] + arr[i], arr[i])

print(max(prefix))