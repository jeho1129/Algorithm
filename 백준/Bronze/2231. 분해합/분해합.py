import sys
input = sys.stdin.readline
N = int(input())
result = 0
while result <= N:
    S = list(str(result))
    T = 0
    for i in range(len(S)):
        T += int(S[i])
    if T + result == N:
        print(result)
        break
    else:
        result += 1
if result > N:
    print(0)