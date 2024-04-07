import sys
input = sys.stdin.readline

num = sorted(list(map(int, input().split())))
if sum(num) - num[2] > num[2]:
    print(sum(num))
else:
    print((sum(num) - num[2]) * 2 - 1)