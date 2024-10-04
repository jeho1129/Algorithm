import sys
input = sys.stdin.readline
N = int(input())
T = 0
X = 2
while T != N:
    T += 1
    X += X - 1
print(X ** 2)