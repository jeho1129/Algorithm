import sys, math
input = sys.stdin.readline
A, B, V = map(int, input().split())
N = A - B
B = 1
M = 0
if A < V:
    M = math.ceil((V - A) / N)
print(B + M)