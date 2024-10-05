import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
num = 1
stack = []
for i in range(N):
    x = S[i]
    if num == x:
        num += 1
        while stack:
            if stack[-1] == num:
                stack.pop()
                num += 1
            else:
                break
    else:
        stack.append(x)
print("Nice" if not stack else "Sad")