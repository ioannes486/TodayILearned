N, M = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(M):
    i, j = map(int, input().split())
    result = arr[i-1]
    for a in range(i, j+1):
        result += arr[a]
    print(arr, result)

