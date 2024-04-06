import sys
input = sys.stdin.readline

A, B = map(int, input().split())
K = 1   # K번째
X = 1   # 나누는 수
while K < B:
    if X > A:
        X = 0
        break
    X += 1
    if A % X == 0:
        K += 1
print(X)