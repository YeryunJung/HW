# fn_d(91) 
# 출력 예시 
# 101

# n을 d(n)의 제너레이터라고 한다
# d(91) = 9 + 1 + 91 = 101
# 101은 셀프 넘버가 아닌 숫자

# def fn_d(n):
#     n_list = [int(i) for i in str(n)] # 정수형으로 바꿔줘야 이터러블하게 바뀐다
#     n_list.append(n)
#     return sum(n_list)

def is_selfnumber(n):
    # 주어진 범위 내에서 반복하며, 제너레이터를 하나 이상 가지고 있는 경우 False 반환
    for m in range(1, n + 1):
        if fn_d(m) == n:
            return False
    return True # 반환 없이 반복문이 끝난 경우

# 람다를 담아서 변수 호출하듯이 사용
fn_d = lambda n: sum([int(i) for i in str(n)] + [n])
print(fn_d(91))

