import sys
input = sys.stdin.readline
while True:
    N = int(input())
    if N == -1:
        break
    M = [1]
    X = 2
    while N > X:
        if N % X == 0:
            M.append(X)
        X += 1
    if sum(M) == N:
        print(f"{N} = ", end='')
        for i in M:
            if i == M[-1]:
                print(i)
            else:
                print(f"{i} + ", end='')
    else:
        print(f"{N} is NOT perfect.")