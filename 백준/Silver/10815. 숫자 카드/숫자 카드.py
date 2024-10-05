import sys
input = sys.stdin.readline

N = int(input())
S = sorted(list(map(int, input().split())))
M = int(input())
L = list(map(int, input().split()))
for i in range(M):
    low, high = 0, N - 1
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if S[mid] > L[i]:
            high = mid - 1
        elif S[mid] < L[i]:
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')