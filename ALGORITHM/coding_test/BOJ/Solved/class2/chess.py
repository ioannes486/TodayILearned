N = int(input())
arr = list(map(int, input().split()))


arr2 = []
max_num = max(arr)
for i in range(N):
    arr2.append(arr[i] / max_num * 100)
print(sum(arr2)/N)
