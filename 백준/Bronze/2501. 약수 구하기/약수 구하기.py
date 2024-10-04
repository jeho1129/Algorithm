import sys
input = sys.stdin.readline
N, K = map(int, input().split())
M = []
T = N
while True:
    if len(M) == K:
        print(M[-1])
        break
    if T == 0:
        print(0)
        break
    if N % T == 0:
        A = N // T
        M.append(A)
    T = T - 1