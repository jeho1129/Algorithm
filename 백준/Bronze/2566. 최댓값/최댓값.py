import sys
input = sys.stdin.readline
N = [list(map(int, input().split())) for _ in range(9)]
num = -1
result = [0, 0]
for i in range(9):
    for j in range(9):
        if N[i][j] > num:
            num = N[i][j]
            result = [i + 1, j + 1]
print(num)
print(*result)