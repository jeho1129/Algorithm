def solution(x1, x2, x3, x4):
    if x1 == False and x2 == False:
        x = False
    else:
        x = True
    if x3 == False and x4 == False:
        y = False
    else:
        y = True
    if x == True and y == True:
        answer = True
    else:
        answer = False
    return answer