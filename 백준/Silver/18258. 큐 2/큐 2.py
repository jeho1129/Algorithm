import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
queue = deque()
for i in range(N):
    x = input().strip()
    if x == 'pop':
        if queue:
            result = queue.popleft()
            print(result)
        else:
            print(-1)
    elif x == 'size':
        print(len(queue))
    elif x == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif x == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif x == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        queue.append(int(x[5:]))