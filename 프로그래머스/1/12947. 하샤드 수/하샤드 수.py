def solution(x):
    y = sum([int(i) for i in str(x)])
    return True if x % y == 0 else False