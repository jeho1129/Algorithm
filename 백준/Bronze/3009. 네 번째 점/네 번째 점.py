import sys
input = sys.stdin.readline
A, B = map(int, input().split())
C, D = map(int, input().split())
E, F = map(int, input().split())
if A == C:
    X = E
elif C == E:
    X = A
else:
    X = C
if B == D:
    Y = F
elif D == F:
    Y = B
else:
    Y = D
print(X, Y)