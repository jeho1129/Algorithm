import sys
input = sys.stdin.readline

N = int(input())
S = set()
result = 0
for i in range(N):
    x = input().rstrip()
    if x == 'ENTER':
        result += len(S)
        S = set()
    else:
        S.add(x)
result += len(S)
print(result)