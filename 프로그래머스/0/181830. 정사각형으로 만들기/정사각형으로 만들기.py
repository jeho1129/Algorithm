def solution(arr):
    answer = [[]]
    a, b = len(arr), len(arr[0])
    if a > b:
        for i in range(len(arr)):
            for j in range(a - b):
                arr[i].append(0)
    elif a < b:
        for i in range(b - a):
            arr.append([0] * b)
    return arr