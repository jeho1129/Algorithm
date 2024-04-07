import sys
input = sys.stdin.readline

N = int(input())
result = 0
for i in range(N - 1, 0, -1):
    x = list(str(i))
    s = i
    for j in x:
        s += int(j)
    if s == N:
        result = i
print(result)