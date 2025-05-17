def solution(s):
    answer = ''
    word_index = 0  # 현재 단어 내에서의 인덱스

    for char in s:
        if char == ' ':
            # 공백을 만나면 공백을 결과에 추가하고 단어 인덱스를 초기화합니다.
            answer += ' '
            word_index = 0
        else:
            # 공백이 아니면 현재 단어 인덱스에 따라 대소문자를 변환합니다.
            if word_index % 2 == 0:
                # 짝수번째 (0부터 시작)는 대문자로
                answer += char.upper()
            else:
                # 홀수번째는 소문자로
                answer += char.lower()
            # 단어 내 인덱스를 1 증가시킵니다.
            word_index += 1

    return answer