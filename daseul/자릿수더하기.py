def sum_digit(number):
    #'''number의 각 자릿수를 더해서 return하세요'''
    s = str(number)
    r = 0
    for i in range(len(s)):
        r = r + int(s[i])
    return r
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));
