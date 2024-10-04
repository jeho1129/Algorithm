import sys
input = sys.stdin.readline

N = int(input())
result = -1
for i in range((N // 5) + 1):
    A = N - (5 * i)
    if A % 3 == 0:
        B = A // 3
        if result == -1:
            result = i + B
        elif result > i + B:
            result = i + B
print(result)