import sys
input = sys.stdin.readline
N = int(input())
M = list(map(int, input().split()))
result = 0
for i in range(N):
    if M[i] > 1:
        if M[i] == 2:
            result += 1
            continue
        else:
            X = 0
            for j in range(2, M[i]):
                if M[i] % j == 0:
                    X = 1
                    break
            if X == 0:
                result += 1
print(result)