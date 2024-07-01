def solution(str1, str2):
    answer = ''
    n = 1
    while len(str1) + len(str2) >= n:
        if n % 2 == 0:
            answer += str2[n // 2 - 1]
        else:
            answer += str1[(n - 1) // 2]
        n += 1
    return answer