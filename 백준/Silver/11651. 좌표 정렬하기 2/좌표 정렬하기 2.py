import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for i in range(N)]
S.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(*S[i])