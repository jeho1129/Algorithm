import sys
input = sys.stdin.readline

paper = [[0] * 100 for i in range(100)]
T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    for i in range(A, A + 10):
        for j in range(B, B + 10):
            paper[i][j] = 1
result = 0
for i in range(100):
    result += sum(paper[i])
print(result)