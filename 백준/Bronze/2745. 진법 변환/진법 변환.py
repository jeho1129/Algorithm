import sys
input = sys.stdin.readline
N, B = map(str, input().split())
B = int(B)
result = 0
for i in range(len(N)):
    if ord(N[i]) > 57:
        result += B ** (len(N) - i - 1) * (ord(N[i]) - 55)
    else:
        result += B ** (len(N) - i - 1) * int(N[i])
print(result)