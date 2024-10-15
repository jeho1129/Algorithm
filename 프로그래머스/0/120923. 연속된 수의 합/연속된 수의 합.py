from collections import deque

def solution(num, total):
    queue = deque([i for i in range(1, num + 1)])
    while sum(queue) != total:
        if sum(queue) > total:
            if len(queue) > 1:
                queue.pop()
                x = queue[0] - 1
                queue.appendleft(x)
            else:
                queue[0] -= 1
        elif sum(queue) < total:
            if len(queue) > 1:
                queue.popleft()
                x = queue[-1] + 1
                queue.append(x)
            else:
                queue[0] += 1
    return list(queue)