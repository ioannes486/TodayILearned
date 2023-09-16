import sys
N = int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))

s = 0
e = N-1

gijun = abs(arr[s] + arr[e])
result = [arr[s], arr[e]]

while s < e:
  left, right = arr[s], arr[e]
  sum = left + right
  if abs(sum) < gijun:
    gijun = abs(sum)
    result = [left, right]
    if gijun == 0:
        break

  if sum < 0:
    s += 1
  else:
    e -= 1
print(result[0], result[1])
