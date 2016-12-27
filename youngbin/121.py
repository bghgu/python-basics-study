
# http://tryhelloworld.co.kr/challenge_codes/121
# 제일 작은 수 제거하기

def rm_small(mylist):
    # 함수를 완성하세요
    if len(mylist)<=1:
        return []
    smallest = mylist[0]
    items = mylist
    for i in items:
        if i<smallest:
            smallest=i
        print("%d %d" % (i, smallest))
    items.remove(smallest)
    return items


# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))
