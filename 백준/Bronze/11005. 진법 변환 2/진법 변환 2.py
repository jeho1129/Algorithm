import sys
input = sys.stdin.readline
N, B = map(int, input().split())
result = ''
while N >= B:
    X = N % B
    N = N // B
    if X >= 10:
        Y = chr(X + 55)
    else:
        Y = str(X)
    result += Y
if N >= 10:
    Y = chr(N + 55)
else:
    Y = str(N)
result += Y
print(result[::-1])