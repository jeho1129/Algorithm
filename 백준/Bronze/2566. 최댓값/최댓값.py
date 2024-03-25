import sys
input = sys.stdin.readline

max_num = 0
result = [0, 0]
for i in range(9):
    X = list(map(int, input().split()))
    for j in range(9):
        if X[j] >= max_num:
            max_num = X[j]
            result = [i + 1, j + 1]
print(max_num)
print(*result)