import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [i for i in range(1, N + 1)]


def combinations(n, arr, c):
    if len(arr) == n:
        print(*arr)
        return
    for i in range(c, N):
        combinations(n, arr + [S[i]], i)


combinations(M, [], 0)