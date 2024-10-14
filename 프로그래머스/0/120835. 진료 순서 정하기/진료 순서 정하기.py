def solution(emergency):
    check = sorted(emergency, reverse = True)
    return [check.index(i) + 1 for i in emergency]