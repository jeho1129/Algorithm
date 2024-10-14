def solution(my_string):
    answer = [0] * 52
    for i in range(len(my_string)):
        T = ord(my_string[i])
        if T <= 90:
            answer[T - 65] += 1
        else:
            answer[T - 71] += 1
    return answer