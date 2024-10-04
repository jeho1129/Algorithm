import sys
input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()
for i in range(N):
    print(S[i])