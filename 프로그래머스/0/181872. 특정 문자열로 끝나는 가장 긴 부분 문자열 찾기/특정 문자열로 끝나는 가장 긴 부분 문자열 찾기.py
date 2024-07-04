def solution(myString, pat):
    t = 0
    for i in range(len(myString) - len(pat), -1, -1):
        t = 1
        for j in range(len(pat)):
            if myString[i + j] != pat[j]:
                t = 0
                break
        if t == 1:
            answer = myString[:i + len(pat)]
            break
    return answer