import sys
input = sys.stdin.readline

N = int(input())
S = []
x = 0
while True:
    X = str(x)
    if '666' in X:
        S.append(x)
        if len(S) == N:
            print(S[-1])
            break
    x += 1