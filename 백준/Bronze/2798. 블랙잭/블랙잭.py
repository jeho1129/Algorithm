import sys

input = sys.stdin.readline
N, M = map(int, input().split())
S = list(map(int, input().split()))
result = 0


def combinations(n, new_arr, c):
    global result
    # 순서 상관 X, 중복 X
    if len(new_arr) == n:
        if result < sum(new_arr) <= M:
            result = sum(new_arr)
        return
    for i in range(c, len(S)):
        combinations(n, new_arr + [S[i]], i + 1)


combinations(3, [], 0)
print(result)