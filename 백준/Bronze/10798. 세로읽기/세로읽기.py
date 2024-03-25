T = 0
input_list = []
for i in range(5):
    X = list(map(str, input()))
    if T < len(X):
        T = len(X)
    input_list.append(X)
for i in range(T):
    for j in range(5):
        if len(input_list[j]) >= i + 1:
            print(input_list[j][i], end='')