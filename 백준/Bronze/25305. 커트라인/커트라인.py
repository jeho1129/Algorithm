import sys
input = sys.stdin.readline

N, k = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
print(S[-k])