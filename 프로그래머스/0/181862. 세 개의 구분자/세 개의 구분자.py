def solution(myStr):
    answer = []
    word = ''
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            if len(word) > 0:
                answer.append(word)
                word = ''
        else:
            word += i
    if len(word) > 0:
        answer.append(word)
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer