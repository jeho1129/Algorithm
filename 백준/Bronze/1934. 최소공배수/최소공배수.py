import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    result = A * B
    while B > 0:
        A, B = B, A % B
    print(result // A)