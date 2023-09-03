import sys
# sys.stdin = open('queue.txt','r')

from collections import deque
q = deque()
N  = int(input())
for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if command[0:4] == 'push':
        q.append(int(command[-1]))
    elif command == 'pop':
        print(q[0] if q else -1)
        q.popleft()
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        print(0 if q else 1)
    elif command == 'front':
        print(q[0] if q else -1)
    elif command == 'back':
        print(q[-1] if q else -1)

q = []
