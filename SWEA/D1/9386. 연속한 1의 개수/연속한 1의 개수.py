T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = input()
    result = 0
    count = 0
    for i in range(N):
        if S[i] == '1':
            count += 1
        else:
            if count > result:
                result = count
                count = 0
    if count > result:
        result = count
    print(f"#{test_case} {result}")