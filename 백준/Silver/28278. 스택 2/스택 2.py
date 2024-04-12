import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    x = input().strip()
    if len(x) == 1:
        if int(x) == 2:
            if arr:
                result = arr.pop()
                print(result)
            else:
                print(-1)
        elif int(x) == 3:
            print(len(arr))
        elif int(x) == 4:
            if arr:
                print(0)
            else:
                print(1)
        else:
            if arr:
                print(arr[-1])
            else:
                print(-1)
    else:
        y = int(x[2:])
        arr.append(y)