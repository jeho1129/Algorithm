def solution(num):
    n = 0
    while num != 1:
        n += 1
        if n == 501:
            return -1
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    return n