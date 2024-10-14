def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        new_line = ''
        for j in range(len(picture[i])):
            new_line += picture[i][j] * k
        for j in range(k):
            answer.append(new_line)
    return answer