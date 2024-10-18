from collections import deque

def solution(arr):
    arr = deque(arr)
    x = min(arr)
    answer = []
    if len(arr) == 1:
        return [-1]
    else:
        for i in range(len(arr)):
            y = arr.popleft()
            if x != y:
                answer.append(y)
        return answer