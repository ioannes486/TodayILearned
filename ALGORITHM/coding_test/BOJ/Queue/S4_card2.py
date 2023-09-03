N = int(input())
from collections import deque
q = deque()
for idx in range(1, N+1):
    q.append(idx)
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
else:
    print(q[0])