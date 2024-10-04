import sys
input = sys.stdin.readline
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    if N >= 25:
        A = N // 25
        N = N % 25
    else:
        A = 0
    if N >= 10:
        B = N // 10
        N = N % 10
    else:
        B = 0
    if N >= 5:
        C = N // 5
        N = N % 5
    else:
        C = 0
    if N >= 1:
        D = N // 1
    else:
        D = 0
    print(A, B, C, D)