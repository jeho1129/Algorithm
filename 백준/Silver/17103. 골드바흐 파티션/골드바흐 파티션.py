import sys
input = sys.stdin.readline

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2 * i, 1000001, i):
            check[j] = 1

N = int(input())

for i in range(N):
    count = 0
    X = int(input())
    for j in prime:
        if j >= X:
            break
        if not check[X - j] and j <= X - j:
            count += 1
    print(count)