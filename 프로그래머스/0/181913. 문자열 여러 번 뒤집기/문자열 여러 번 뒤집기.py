def solution(my_string, queries):
    for i in range(len(queries)):
        a, b = queries[i][0], queries[i][1]
        if a > 0:
            my_string = my_string[:a] + my_string[b:a - 1:-1] + my_string[b + 1:]
        else:
            my_string = my_string[b::-1] + my_string[b + 1:]
    return my_string