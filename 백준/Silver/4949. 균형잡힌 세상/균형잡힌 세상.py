while True:
    x = input()
    arr = []
    result = "yes"
    if x == ".":
        break
    for i in range(len(x)):
        if x[i] == "(" or x[i] == "[":
            arr.append(x[i])
        elif x[i] == ")":
            if not arr:
                result = "no"
                break
            elif arr[-1] == "(":
                arr.pop()
            else:
                result = "no"
                break
        elif x[i] == "]":
            if not arr:
                result = "no"
                break
            elif arr[-1] == "[":
                arr.pop()
            else:
                result = "no"
                break
    if arr:
        result = "no"
    print(result)