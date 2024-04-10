import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic1 = {}
dic2 = {}
for i in range(N):
    x = input().rstrip()
    dic1[x] = i + 1
    dic2[i + 1] = x
for i in range(M):
    x = input().rstrip()
    if x.isdigit():
        print(dic2[int(x)])
    else:
        print(dic1[x])