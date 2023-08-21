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

visited = [0 for _ in range(n+1 )]
def recur(node):
    visited[node] = 1  # 재귀해서 들어가서 방문처리한다.

    for nxt in graph[node]:  # 한 노드에 연결되어 있는 모든 노드에 대해
        if visited[nxt] == 1:
            continue
        recur(nxt)  # 재귀함수를 호출하여 방문한다. 이때 재귀해서 들어갈 수록 깊이가 깊어지며 이때문에 깊이 우선 탐색이라고 한다.
print(graph)