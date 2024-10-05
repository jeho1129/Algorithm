import sys
input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]
print(round(sum(S) / N))
S.sort()
print(S[(N - 1) // 2])
dic = {}
for i in range(N):
    if S[i] not in dic:
        dic[S[i]] = 1
    else:
        dic[S[i]] += 1
result = max(dic.values())
result_arr = []
for i in dic:
    if result == dic[i]:
        result_arr.append(i)
if len(result_arr) > 1:
    print(result_arr[1])
else:
    print(result_arr[0])
print(max(S) - min(S))