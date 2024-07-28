def solution(arr, queries):
    for i in queries:
        x, y = i
        for j in range(x, y + 1):
            arr[j] += 1
    return arr