A = [int(input()) for i in range(10)]
N = set()
for i in range(10):
    N.add(A[i] % 42)
print(len(N))