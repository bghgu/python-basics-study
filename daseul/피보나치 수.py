def fibonacci(num):
    f_1 = 0
    f_2 = 1
    answer = 0
    for i in range(num-1):
        answer = f_1 + f_2
        f_1 = f_2
        f_2 = answer
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))
