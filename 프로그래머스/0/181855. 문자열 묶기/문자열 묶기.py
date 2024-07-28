def solution(strArr):
    long = [0] * 30
    for i in strArr:
        long[len(i) - 1] += 1 
    return max(long)