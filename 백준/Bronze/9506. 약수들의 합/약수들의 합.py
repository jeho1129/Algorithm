while True:
    x = int(input())
    if x == -1:
        break
    num = []
    N = 0
    for i in range(1, x):
        if x % i == 0:
            num.append(i)
    if sum(num) == x:
        print(f"{x} = ", end='')
        for i in range(len(num)):
            if i == len(num) - 1:
                print(num[i])
            else:
                print(f"{num[i]} + ", end='')
    else:
        print(f"{x} is NOT perfect.")