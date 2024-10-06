T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A, B, C, D, E = 0, 0, 0, 0, 0
    while N % 2 == 0:
        N = N // 2
        A += 1
    while N % 3 == 0:
        N = N // 3
        B += 1
    while N % 5 == 0:
        N = N // 5
        C += 1
    while N % 7 == 0:
        N = N // 7
        D += 1
    while N % 11 == 0:
        N = N // 11
        E += 1
    print(f"#{test_case} {A} {B} {C} {D} {E}")