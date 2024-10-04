import sys
input = sys.stdin.readline

S = [int(input()) for _ in range(5)]
S.sort()
print(sum(S) // 5)
print(S[2])