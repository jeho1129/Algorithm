import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [i for i in range(1, N + 1)]


def product(n, arr):
    if len(arr) == n:
        print(*arr)
        return
    for i in range(N):
        product(n, arr + [S[i]])


product(M, [])