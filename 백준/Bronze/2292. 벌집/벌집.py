import sys
input = sys.stdin.readline
N = int(input())
T = 1
X = 1
while X < N:
    X += T * 6
    T += 1
print(T)