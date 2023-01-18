year = int(input('년도를 입력하세요: '))

# 4의 배수이면서 100의 배수가 아니면 윤년
# year % 4 == 0 and year % 100 != 0
# 400의 배수이면 윤년
# year % 400 == 0

if year % 400 == 0:
    print('윤년입니다')
elif year % 4 == 0 and year % 100 != 0:
    print('윤년입니다')
else:
    print('평년입니다')


# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 100 == 0)
#     print('윤년입니다')
# else:
#     print('평년입니다')