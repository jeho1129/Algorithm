T = int(input())
for test_case in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)
    distance = F * time
    print(f"#{test_case} {distance}")