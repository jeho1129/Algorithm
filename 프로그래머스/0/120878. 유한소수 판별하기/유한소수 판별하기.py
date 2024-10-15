import math

def solution(a, b):
    x = math.gcd(a, b)
    b = b // x
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
    return b if b == 1 else 2