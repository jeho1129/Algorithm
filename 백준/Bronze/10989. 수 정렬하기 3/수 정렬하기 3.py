import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 10000
for i in range(N):
    x = int(input())
    arr[x - 1] += 1
for i in range(10000):
    y = arr[i]
    for j in range(y):
        print(i + 1)