def solution(n):
    # 1. 자연수 n을 3진법으로 변환하되, 변환 과정에서 나머지를 뒤에 붙여나가면
    # 자동으로 뒤집힌 3진법 형태의 문자열이 만들어집니다.
    reversed_base3_str = ''
    while n > 0:
        remainder = n % 3  # 3으로 나눈 나머지
        reversed_base3_str += str(remainder) # 나머지를 문자열에 추가 (뒤집힌 순서)
        n //= 3 # n을 3으로 나눈 몫으로 업데이트

    # 예: n=45 일 경우, 45%3=0 (str='0'), n=15 -> 15%3=0 (str='00'), n=5 -> 5%3=2 (str='002'), n=1 -> 1%3=1 (str='0021')
    # 최종적으로 '0021'은 45의 3진법 표현(1200)을 뒤집은 형태입니다.

    # 2. 뒤집힌 3진법 문자열(reversed_base3_str)을 다시 10진법 숫자로 변환합니다.
    # Python의 int(string, base) 함수를 사용하면 편리하게 변환할 수 있습니다.
    answer = int(reversed_base3_str, 3)

    return answer