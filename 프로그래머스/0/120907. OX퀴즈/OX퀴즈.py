def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        problem = list(map(str, quiz[i].split()))
        if problem[1] == "+":
            if int(problem[0]) + int(problem[2]) == int(problem[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(problem[0]) - int(problem[2]) == int(problem[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer