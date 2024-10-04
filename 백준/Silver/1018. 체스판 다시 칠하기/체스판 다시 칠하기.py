import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
result = 64

for i in range(N):
    board.append(input().rstrip())

for i in range(N - 7):
    for j in range(M - 7):
        draw1 = 0
        draw2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'B':
                        draw1 += 1
                    if board[k][l] != 'W':
                        draw2 += 1
                else:
                    if board[k][l] != 'W':
                        draw1 += 1
                    if board[k][l] != 'B':
                        draw2 += 1
        if min(draw1, draw2) < result:
            result = min(draw1, draw2)
print(result)