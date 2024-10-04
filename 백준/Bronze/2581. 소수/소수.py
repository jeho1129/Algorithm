import sys
input = sys.stdin.readline
M = int(input())
N = int(input())
S = []
for i in range(M, N + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        S.append(i)
if S:
    print(sum(S))
    print(S[0])
else:
    print(-1)