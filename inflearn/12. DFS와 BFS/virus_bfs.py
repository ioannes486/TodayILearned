'''
1.	바이러스( #2606 )
	노드와 간선이 주어집니다.
	아래 그림과 같이 점들이 연결된 관계가 주어졌을 때,
	1번 노드가 바이러스에 감염되었다면, 연결된 점들은 모두 바이러스에 감염됩니다.
	입력이 주어졌을 때, 1번 노드와 연결되어 감염된 노드들의 수를 출력하시오.
입력
7 노드 수
6 간선 수
1 2 노드간의 관계
2 3
1 5
5 2
5 6
4 7
출력
4
'''
from collections import deque
import sys
sys.stdin = open('virus.txt','r')
n = int(input())
m = int(input())

# 연결 리스트 형식으로 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
visited = [0 for _ in range(n+1)]
q = deque()
q.append(1)

while len(q) > 0:
    # ex) 방문하는 노드가 1번 노드인 경우
    node = q.popleft()  # 큐의 가장 왼쪽에 방문할 노드 지정 (1)
    visited[node] = 1  # 방문한 후 방문처리

    # 다음에 방문할 노드 결정하기
    # for 문을 통해 1과 병렬적으로 연결되어 있는 노드를 모두 방문 대기열 (q)에 추가한다.
    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        q.append(nxt)  # 다음 방문노드 추가

print(visited)