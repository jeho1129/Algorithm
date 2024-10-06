T = int(input())
for test_case in range(1, T + 1):
    S = list(map(int, input().split()))
    print(f"#{test_case} {round((sum(S) - min(S) - max(S)) / 8)}")