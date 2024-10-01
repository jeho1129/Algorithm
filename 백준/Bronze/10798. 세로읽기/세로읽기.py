import sys
input = sys.stdin.readline
N = [list(map(str, input().rstrip())) for _ in range(5)]
for i in range(15):
    for j in range(5):
        if len(N[j]) > i:
            print(N[j][i], end='')