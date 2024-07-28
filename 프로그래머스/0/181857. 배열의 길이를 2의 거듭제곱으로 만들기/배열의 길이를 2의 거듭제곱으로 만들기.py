def solution(arr):
    x = 0
    while True:
        if 2 ** x == len(arr):
            break
        elif 2 ** x < len(arr):
            x += 1
            if len(arr) <= 2 ** x:
                break
    for i in range(2 ** x - len(arr)):
        arr.append(0)
    return arr