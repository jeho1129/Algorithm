import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [i for i in range(1, N + 1)]
visited = [False] * N


def permutations(n, arr):
    global S
    if len(arr) == n:
        print(*arr)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            permutations(n, arr + [S[i]])
            visited[i] = False


permutations(M, [])