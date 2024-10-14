def solution(dots):
    max_x, max_y, min_x, min_y = dots[0][0], dots[0][1], dots[0][0], dots[0][1]
    for i in range(1, 4):
        x, y = dots[i][0], dots[i][1]
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    return (max_x - min_x) * (max_y - min_y)