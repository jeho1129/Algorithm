def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if ord(s[i]) + n > ord('z'):
            answer += chr(ord(s[i]) + n - 26)
        elif ord(s[i]) <= ord('Z') and ord(s[i]) + n > ord('Z'):
            answer += chr(ord(s[i]) + n - 26)
        elif ord(s[i]) < ord('A'):
            answer += s[i]
        else:
            answer += chr(ord(s[i]) + n)
    return answer