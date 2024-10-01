import sys
input = sys.stdin.readline
N = [[0] * 100 for _ in range(100)]
X = int(input())
for i in range(X):
    A, B = map(int, input().split())
    for j in range(A - 1, A + 9):
        for k in range(B - 1, B + 9):
            N[j][k] = 1
result = 0
for i in range(100):
    for j in range(100):
        if N[i][j] == 1:
            result += 1
print(result)