graph = [list(map(int, input().split()))for _ in range(4)]
x1,y1,x2,y2 = map(int,input().split())
prefix = [[0 for _ in range(5)] for _ in range(5)]


# 누적합 그래프 만들기
for y in range(4):
    for x in range(4):
        prefix[y+1][x+1] = prefix[y][[x+1] + prefix[y+1][x] - prefix[y][x] + graph[y][x]
        # 누적합에서 겹치는 부분 빼주기
print(prefix)

answer = prefix[y2][x2] - prefix[y2][x1-1] - prefix[y1-1][x2] + prefix[y1-1][x1-1]

print(answer)