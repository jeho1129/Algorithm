num, result = 0, 0
for i in range(9):
    A = int(input())
    if A > num:
        num, result = A, i + 1
print(num)
print(result)