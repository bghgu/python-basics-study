def water_melon(n):
    # 함수를 완성하세요.
    a = ""
    for i in range(n):
        if(i%2==0):
            a = a + "수"
        else:
            a = a + "박"
    return a


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
