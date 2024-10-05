import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


def BFS(start):
    visited = [False] * (N + 1)
    visited[start] = True
    queue = deque([start])
    count = 0

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1

    return count


print(BFS(1))