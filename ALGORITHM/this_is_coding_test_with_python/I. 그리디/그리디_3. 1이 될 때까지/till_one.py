import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
count = 0
while True:
    if N == 1:
        break

    if N % K == 0:
        N = N//K
        count+=1
    else:
        N = N - 1
        count+=1
print(count, N)