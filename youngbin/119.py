
# http://tryhelloworld.co.kr/challenge_codes/119
# 정수제곱근판별하기

import math

def nextSqure(n):
    squareroot = math.sqrt(n)
    if squareroot > int(squareroot): return 'no'
    else: return (int(squareroot) + 1)**2

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));
