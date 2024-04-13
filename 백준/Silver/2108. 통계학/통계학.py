import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
print(round(sum(arr) / N))
arr.sort()
print(arr[(N - 1) // 2])
dic = dict()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
result = max(dic.values())
result_arr = []
for i in dic:
    if result == dic[i]:
        result_arr.append(i)
if len(result_arr) > 1:
    print(result_arr[1])
else:
    print(result_arr[0])
print(max(arr) - min(arr))