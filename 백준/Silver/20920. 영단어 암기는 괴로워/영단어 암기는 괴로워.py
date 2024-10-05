import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for i in range(N):
    x = input().rstrip()
    if len(x) >= M:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
dic = dict(sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
for i in dic.keys():
    print(i)