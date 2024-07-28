def solution(myString, pat):
    answer = 0
    for i in range(len(myString) - len(pat) + 1):
        for j in range(len(pat)):
            if myString[i + j] != pat[j]:
                break
        else:
            answer += 1
    return answer