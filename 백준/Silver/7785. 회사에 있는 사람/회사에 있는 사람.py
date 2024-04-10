import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for i in range(N):
    A, B = map(str, input().split())
    if B == 'enter':
        dic[A] = 1
    else:
        dic.pop(A)
dic = sorted(dic.keys(), reverse=True)
for i in dic:
    print(i)