T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    result = 1
    count = 1
    for i in range(1, N):
        if C[i - 1] < C[i]:
            count += 1
        else:
            result = max(result, count)
            count = 1
    else:
        result = max(result, count)
        
    print(f"#{test_case} {result}")