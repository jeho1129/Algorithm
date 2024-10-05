import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
S = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    queue = deque([(x, y)])
    count = 1
    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            new_x, new_y = x1 + dx[i], y1 + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if S[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                    visited[new_x][new_y] = 1
                    count += 1
                    queue.append((new_x, new_y))

    result.append(count)


for i in range(N):
    for j in range(N):
        if S[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            BFS(i, j)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])