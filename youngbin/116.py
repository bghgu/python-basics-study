
# http://tryhelloworld.co.kr/challenge_codes/116
# 자릿수더하기

def sum_digit(number):
    nsum = 0
    for i in str(number): nsum += int(i)
    return nsum

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));
