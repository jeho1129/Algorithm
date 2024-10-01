import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    for j in range(M):
        A[i][j] = A[i][j] + B[i][j]
    print(*A[i])