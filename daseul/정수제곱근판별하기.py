def nextSqure(n):
    # 함수를 완성하세요
    a = n ** (1/2)
    if a == int(a):
        return (a+1) ** 2
    else:
        return 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));
