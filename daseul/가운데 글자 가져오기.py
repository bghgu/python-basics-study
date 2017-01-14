def string_middle(str):
    # 함수를 완성하세요
    if(len(str) % 2 == 0):
        return str[len(str)//2-1:len(str)//2+1]
    else:
        return str[len(str)//2]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
