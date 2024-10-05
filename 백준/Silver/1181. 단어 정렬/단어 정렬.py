import sys
input = sys.stdin.readline

N = int(input())
S = list(set(input().rstrip() for _ in range(N)))
S.sort(key=lambda x: [len(x), x])
for i in S:
    print(i)