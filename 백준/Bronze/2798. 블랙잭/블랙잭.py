import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
x = 0
result = 0
for i in range(N):
    result += num[i]
    for j in range(N):
        if i != j:
            result += num[j]
            for k in range(N):
                if i != k and j != k:
                    result += num[k]
                    if x < result <= M:
                        x = result
                    result -= num[k]
            result -= num[j]
    result -= num[i]
print(x)