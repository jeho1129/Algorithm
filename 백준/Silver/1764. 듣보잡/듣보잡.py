import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
dic2 = {}
for i in range(N):
    dic[input().rstrip()] = 0
S = sorted([input().rstrip() for i in range(M)])
for i in range(M):
    if S[i] in dic:
        dic2[S[i]] = 1
print(sum(dic2.values()))
for i in dic2.keys():
    print(i)