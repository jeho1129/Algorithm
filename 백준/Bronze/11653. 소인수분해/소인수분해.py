import sys
input = sys.stdin.readline
N = int(input())
T = 2
while N != 1:
    if N % T == 0:
        print(T)
        N = N // T
        T = 2
    else:
        T += 1