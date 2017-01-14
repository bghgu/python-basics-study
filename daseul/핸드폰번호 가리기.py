def hide_numbers(s):
    #함수를 완성해 별이를 도와주세요
    a = s[-4:]
    b = len(s)-4
    c = ""
    for i in range(0, b):
    	c = c + "*"
    return (c + a)
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));
