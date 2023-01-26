# 1
# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(identification_number):
    identification_number = identification_number[:6] + ('*' * 7)
    return identification_number

print(de_identify('970103-1234567'))
print(de_identify('861123-2345678'))

################################################################################
#solving

def de_identify(identification_number):
    identification_number = identification_number.replace('-','')
    # 문자열의 슬라이싱을 이용한 방법
    return identification_number[:-7] + '****'

print(de_identify('970103-1234567'))

def de_identify(identification_number, slicing_num):
    # '-'룰 ''으로 대체
    identification_number = identification_number.replace('-','')
    str_list = list(identification_number)
    str_list[-slicing_num] = '****'
    print(str_list)
    return ''.join(str_list)
    
print(de_identify('970103-1234567'))

# 2
grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

max = 0
idx = 0
for i, grain in enumerate(grain_lst):
    if grain[1] > max:
        max = grain[1]
        idx = i
print(grain_lst[idx][0])
